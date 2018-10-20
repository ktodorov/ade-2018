import requests as req
from .models import Venue

class SongkickClient:
    def find_venues(self, city, size):
        api_key = "io09K9l3ebJxmxe2"
        request = req.get("https://api.songkick.com/api/3.0/search/venues.json?query={}&apikey={}".format(city,api_key))
        venues = request.json()["resultsPage"]["results"]["venue"]
        venue_coords = []
        for venue in venues[0 : size]:
            venue_coords.append(Venue(venue["displayName"], venue["lat"], venue["lng"]))

        return venue_coords