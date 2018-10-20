import requests as req
from .models import Venue

class SongkickClient:
    def findVenues(self, city, size = 30):
        api_key = "io09K9l3ebJxmxe2"
        request = req.get("https://api.songkick.com/api/3.0/search/venues.json?query={}&apikey={}".format(city,api_key))
        requestJson = request.json()

        resultsPageKey = "resultsPage"
        resultsKey = "results"
        venueKey = "venue"
        if (not requestJson or not requestJson[resultsPageKey] or
            not requestJson[resultsPageKey][resultsKey] or
            not requestJson[resultsPageKey][resultsKey][venueKey]):
            return []

        venues = requestJson[resultsPageKey][resultsKey][venueKey]
        venue_coords = []
        for venue in venues[0 : size]:
            latitude = venue["lat"]
            longitude = venue["lng"]
            if latitude is None or longitude is None:
                continue

            newVenue = Venue(venue["displayName"], latitude, longitude)
            venue_coords.append(newVenue)

        return venue_coords