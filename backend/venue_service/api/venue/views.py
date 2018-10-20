from rest_framework import views
from rest_framework.response import Response
from .serializers import VenuesSerializer
from .models import Venue
import requests as req

class ListVenuesView(views.APIView):
    def get(self, request):
        api_key = "io09K9l3ebJxmxe2"
        city = request.GET["city"]
        size = int(request.GET["size"])

        request = req.get("https://api.songkick.com/api/3.0/search/venues.json?query={}&apikey={}".format(city,api_key))
        venues = request.json()["resultsPage"]["results"]["venue"]
        venue_coords = []
        for venue in venues[0:size]:
            venue_coords.append(Venue(venue["displayName"], venue["lat"], venue["lng"]))

        results = VenuesSerializer(venue_coords, many=True).data
        return Response(results)