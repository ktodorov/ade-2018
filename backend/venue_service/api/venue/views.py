from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from .serializers import VenuesSerializer, ScoredVenuesSerializer
from .gmaps_client import GMapsClient
from .venue_client import VenueClient
from .songkick_client import SongkickClient
from .location import Location

# from .models import Venue
import requests as req

class VenuesView(views.APIView):
    venueClient = VenueClient()
    songkickClient = SongkickClient()
    gmapsClient = GMapsClient()

    def get(self, request):
        dummy_optimum = Location(52.360503, 4.905650)
        
        cities = self.gmapsClient.getClosestAddressableLocations(dummy_optimum.latitude, dummy_optimum.longitude)

        sizeKey = "size"
        if sizeKey not in request.GET or not request.GET[sizeKey].isdigit():
            return HttpResponseBadRequest("")

        size = int(request.GET[sizeKey])
        if size == 1:
            bestVenue = None
            for city in cities:
                venues = self.songkickClient.findVenues(city)
                currentBestVenue = self.venueClient.getTopVenue(dummy_optimum, venues)
                if not bestVenue or currentBestVenue.score > bestVenue.score:
                    bestVenue = currentBestVenue
            
            results = ScoredVenuesSerializer(bestVenue).data
            return Response(results)


        bestVenues = []
        for city in cities:
            venues = self.songkickClient.findVenues(city)
            currentBestVenues = self.venueClient.getTopVenues(dummy_optimum, venues)
            bestVenues.extend(currentBestVenues)

        bestVenues.sort(key=lambda x: x.score)
        bestVenues = bestVenues[:size]

        results = ScoredVenuesSerializer(bestVenues, many=True).data
        return Response(results)