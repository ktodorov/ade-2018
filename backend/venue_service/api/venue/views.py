import csv
import numpy as np
import json
import random
import requests as req

from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, JsonResponse

from .serializers.venues_serializer import VenuesSerializer
from .serializers.scored_venues_serializer import ScoredVenuesSerializer

from .gmaps_service import GMapsService
from .venue_service import VenueService
from .songkick_service import SongkickService
from .evolutionary_service import EvolutionaryService

from .models.location import Location
from .models.supplier import Supplier

class VenuesView(views.APIView):
    venueService = VenueService()
    songkickService = SongkickService()
    gmapsService = GMapsService()
    evolutionaryService = EvolutionaryService()

    def post(self, request):
        if not request.body:
            return HttpResponseBadRequest("No body provided")

        # parse coordinates from the POST body
        jsonData = json.loads(request.body)
        coordinatesKey = "coordinates"
        suppliers = []
        if not jsonData or coordinatesKey not in jsonData:
            return HttpResponseBadRequest("Invalid body provided")

        for currentCoordinates in jsonData[coordinatesKey]:
            frequency = random.randint(1, 10)
            supplierLocation = Location(currentCoordinates[0], currentCoordinates[1])
            currentSupplier = Supplier(supplierLocation, frequency)
            suppliers.append(currentSupplier)

        optimumLocation = self.evolutionaryService.getBestLocation(suppliers, self.gmapsService)

        cities = self.gmapsService.getClosestAddressableLocations(optimumLocation)

        sizeKey = "size"
        if sizeKey not in request.GET or not request.GET[sizeKey].isdigit():
            return HttpResponseBadRequest("")

        size = int(request.GET[sizeKey])
        if size == 1:
            bestVenue = None
            for city in cities:
                venues = self.songkickService.findVenues(city)
                currentBestVenue = self.venueService.getTopVenue(optimumLocation, venues)
                if not bestVenue or currentBestVenue.score > bestVenue.score:
                    bestVenue = currentBestVenue

            results = ScoredVenuesSerializer(bestVenue).data
            return Response(results)


        bestVenues = []
        for city in cities:
            venues = self.songkickService.findVenues(city)
            currentBestVenues = self.venueService.getTopVenues(optimumLocation, venues)
            bestVenues.extend(currentBestVenues)

        bestVenues.sort(key=lambda x: x.score)
        bestVenues = bestVenues[:size]

        results = ScoredVenuesSerializer(bestVenues, many=True).data
        return Response(results)
