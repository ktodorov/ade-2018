import googlemaps
import sys
from .models.location import Location
from .models.distance import Distance
from .exceptions.invalid_use_error import InvalidUseError
from .exceptions.server_error import ServerError
from .models.db_distance import DbDistance

class GMapsService:
    googleMapsClient = None
    GOOGLE_MAPS_API_KEY = 'AIzaSyDXgDfHfSIf7pmZI7_MiANSJ9L2iD4lOE8'

    cachedDistances = {}
    distanceRoundSize = 3

    def __init__(self):
        self.googleMapsClient = googlemaps.Client(key=self.GOOGLE_MAPS_API_KEY)
        distances = DbDistance.objects.all()
        print ("distances found in db - ", len(distances))

        for distance in distances:
            key = (round(distance.sourceLatitude, self.distanceRoundSize), 
                   round(distance.sourceLongitude, self.distanceRoundSize), 
                   round(distance.destinationLatitude, self.distanceRoundSize), 
                   round(distance.destinationLongitude, self.distanceRoundSize))

            self.cachedDistances[key] = Distance(distance.kilometers, distance.minutes)

    def calculateDistance(self, location1, location2):
        distanceMapMode = "driving"
    
        origin = (location1.latitude, location1.longitude)
        destination = (location2.latitude, location2.longitude)

        hashKey = (round(origin[0], self.distanceRoundSize), 
                   round(origin[1], self.distanceRoundSize), 
                   round(destination[0], self.distanceRoundSize), 
                   round(destination[1], self.distanceRoundSize))

        if hashKey in self.cachedDistances:
            distance = self.cachedDistances[hashKey]
            return distance
        
        matrix = self.googleMapsClient.distance_matrix(origin, destination, mode=distanceMapMode)
        
        rowsKey = "rows"
        elementsKey = "elements"
        distanceKey = "distance"
        durationKey = "duration"
        valueKey = "value"

        # make a check if the json returned from google api contains everything we need
        if (matrix is None or rowsKey not in matrix or len(matrix[rowsKey]) <= 0 or 
            elementsKey not in matrix[rowsKey][0] or len(matrix[rowsKey][0][elementsKey]) <= 0 or 
            durationKey not in matrix[rowsKey][0][elementsKey][0] or 
            distanceKey not in matrix[rowsKey][0][elementsKey][0] or 
            valueKey not in matrix[rowsKey][0][elementsKey][0][durationKey] or 
            valueKey not in matrix[rowsKey][0][elementsKey][0][distanceKey]):
            return None
        
        meters = matrix[rowsKey][0][elementsKey][0][distanceKey][valueKey]
        seconds = matrix[rowsKey][0][elementsKey][0][durationKey][valueKey]
        if not meters or not seconds:
            return None

        kilometers = meters / 1000 # distance is in meters
        minutes =  round(seconds / 60, 2) # duration is in seconds

        result = Distance(kilometers, minutes)
        self.cachedDistances[hashKey] = result
        
        newDistance = DbDistance()
        newDistance.populate(origin[0], origin[1], destination[0], destination[1], kilometers, minutes)
        newDistance.save()
        
        return result

    def getClosestAddressableLocations(self, location):
        reverseGeocodeResults = []
        try:
            reverseGeocodeResults = self.googleMapsClient.reverse_geocode((location.latitude, location.longitude))
        except googlemaps.exceptions.HTTPError as httpError:
            if httpError.status_code == 400:
                raise InvalidUseError("Invalid parameters ")
            else:
                raise ServerError("")

        addresses = self.parseAddresses(reverseGeocodeResults)
        return addresses

    def parseAddresses(self, geocodeResults):
        addressComponentsKey = "address_components"
        cityLocationType = "locality"
        secondLevelAdministrativeAreaType = "administrative_area_level_2"
        firstLevelAdministrativeAreaType = "administrative_area_level_1"
        
        # flatten the list of objects, each with list of address_components to one big list of all address_components
        addressComponents = [item for sublist in [address[addressComponentsKey] for address in geocodeResults] for item in sublist]
        cityAddresses = self.getAddressComponentsByType(addressComponents, cityLocationType)
        if len(cityAddresses) > 0:
            return cityAddresses

        # if no cities are found, fall back to administrative areas of level 2
        regionLevel2Addresses = self.getAddressComponentsByType(addressComponents, secondLevelAdministrativeAreaType)
        if len(regionLevel2Addresses) > 0:
            return regionLevel2Addresses
            
        # if no administrative areas of level 2 are found, fall back to administrative areas of level 1
        regionLevel1Addresses = self.getAddressComponentsByType(addressComponents, firstLevelAdministrativeAreaType)
        if len(regionLevel1Addresses) > 0:
            return regionLevel1Addresses
        
    def getAddressComponentsByType(self, addressComponents, addressType):
        typesKey = "types"
        longNameKey = "long_name"

        addresses = []
        for addressComponent in addressComponents:
            if addressType in addressComponent[typesKey]:
                addresses.append(addressComponent[longNameKey])
        
        return list(set(addresses)) # this is done in order to distinct the values
