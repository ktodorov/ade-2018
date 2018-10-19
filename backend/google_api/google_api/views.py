from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from .location import Location 
from .responses.distance import Distance
import googlemaps
import json

# Create your views here.

# def index(request):
#     gmaps = googlemaps.Client(key='AIzaSyDXgDfHfSIf7pmZI7_MiANSJ9L2iD4lOE8')

#     # Geocoding an address
#     # geocode_result = gmaps.geocode('Variant Loodsenbouw')
#     # print (geocode_result)

#     # Look up an address with reverse geocoding
#     reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#     return JsonResponse(reverse_geocode_result, safe=False)

@csrf_exempt
def getDistanceBetweenTwoPoints(request):
    print ("received request")
    if request.method == 'POST':
        if not request.body:
            return HttpResponseBadRequest("No body provided")

        jsonData=json.loads(request.body)

        location1Key = "location1"
        location2Key = "location2"
        if not jsonData or location1Key not in jsonData or location2Key not in jsonData:
            return HttpResponseBadRequest("Invalid body provided")

        location1 = Location(jsonData["location1"])
        location2 = Location(jsonData["location2"])

        distance = calculateDistanceBetweenTwoPoints(location1, location2)
        if distance is None:
            return HttpResponseServerError("")

        return JsonResponse(distance.toJson(), safe=False)
    else: #GET
        return HttpResponseNotAllowed("")
    # return JsonResponse("hello, world", safe=False)

def getCitiesByCoordinates(request):
    return JsonResponse("hello, world", safe=False)

def calculateDistanceBetweenTwoPoints(location1, location2):
    googleMapsClient = googlemaps.Client(key='AIzaSyDXgDfHfSIf7pmZI7_MiANSJ9L2iD4lOE8')
    origin = (location1.latitude, location1.longitude)
    destination = (location2.latitude, location2.longitude)
    matrix = googleMapsClient.distance_matrix(origin, destination, mode="driving")
    if matrix is None:
        return None

    kilometers = matrix["rows"][0]["elements"][0]["distance"]["value"] / 1000 # distance is in meters
    minutes =  round(matrix["rows"][0]["elements"][0]["duration"]["value"] / 60, 2) # duration is in seconds

    return Distance(kilometers, minutes)