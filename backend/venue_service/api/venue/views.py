from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from .serializers import VenuesSerializer, ScoredVenuesSerializer
from .gmaps_client import GMapsClient
from .venue_client import VenueClient
from .songkick_client import SongkickClient
from .location import Location
from .EA_locator import evaluation, get_best_location
import csv
import numpy as np
import json
import random

# from .models import Venue
import requests as req

class VenuesView(views.APIView):
    venueClient = VenueClient()
    songkickClient = SongkickClient()
    gmapsClient = GMapsClient()

    def post(self, request):
        if not request.body:
            return HttpResponseBadRequest("No body provided")

        # parse coordinates from the POST body
        jsonData = json.loads(request.body)
        coordinatesKey = "coordinates"
        coordinates = []
        if not jsonData or coordinatesKey not in jsonData:
            return HttpResponseBadRequest("Invalid body provided")

        for currentCoordinates in jsonData[coordinatesKey]:
            coordinates.append(["", "", random.randint(1, 10), currentCoordinates[0], currentCoordinates[1]])

        optimumResult = get_best_location(evaluation, coordinates, self.gmapsClient)
        optimum = Location(optimumResult[0], optimumResult[1])

        cities = self.gmapsClient.getClosestAddressableLocations(optimum.latitude, optimum.longitude)

        sizeKey = "size"
        if sizeKey not in request.GET or not request.GET[sizeKey].isdigit():
            return HttpResponseBadRequest("")

        size = int(request.GET[sizeKey])
        if size == 1:
            bestVenue = None
            for city in cities:
                venues = self.songkickClient.findVenues(city)
                currentBestVenue = self.venueClient.getTopVenue(optimum, venues)
                if not bestVenue or currentBestVenue.score > bestVenue.score:
                    bestVenue = currentBestVenue
            
            results = ScoredVenuesSerializer(bestVenue).data
            return Response(results)


        bestVenues = []
        for city in cities:
            venues = self.songkickClient.findVenues(city)
            currentBestVenues = self.venueClient.getTopVenues(optimum, venues)
            bestVenues.extend(currentBestVenues)

        bestVenues.sort(key=lambda x: x.score)
        bestVenues = bestVenues[:size]

        results = ScoredVenuesSerializer(bestVenues, many=True).data
        return Response(results)