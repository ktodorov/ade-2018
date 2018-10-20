from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from .location import Location 
from .responses.distance import Distance
from .gmaps_client import GMapsClient
from .exceptions.invalid_use_error import InvalidUseError
from .exceptions.server_error import ServerError
import json

@csrf_exempt
def getDistanceBetweenTwoPoints(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed("")

    if not request.body:
        return HttpResponseBadRequest("No body provided")

    jsonData=json.loads(request.body)

    location1Key = "location1"
    location2Key = "location2"
    if not jsonData or location1Key not in jsonData or location2Key not in jsonData:
        return HttpResponseBadRequest("Invalid body provided")

    location1 = Location(jsonData[location1Key])
    location2 = Location(jsonData[location2Key])

    gmapsClient = GMapsClient()
    distance = gmapsClient.calculateDistance(location1, location2)
    if distance is None:
        return HttpResponseServerError("")

    return JsonResponse(distance.toJson(), safe=False)

def getClosestAddressableLocationsByCoordinates(request):
    gmapsClient = GMapsClient()

    latitudeKey = "latitude"
    longitudeKey = "longitude"
    latitude = float(request.GET[latitudeKey])
    longitude = float(request.GET[longitudeKey])

    try:
        closestAddressableLocations = gmapsClient.getClosestAddressableLocations(latitude, longitude)
        return JsonResponse(closestAddressableLocations, safe=False)
    except ServerError as serverError:
        return HttpResponseServerError(str(serverError))
    except InvalidUseError as invalidUseError:
        return HttpResponseBadRequest(str(invalidUseError))