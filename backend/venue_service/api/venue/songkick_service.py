import requests as req
from .models.venue import Venue
import numpy as np

class SongkickService:
    def findVenues(self, city, size = 30):
        # api_key = "io09K9l3ebJxmxe2"
        # request = req.get("https://api.songkick.com/api/3.0/search/venues.json?query={}&apikey={}".format(city,api_key))
        # requestJson = request.json()

        # resultsPageKey = "resultsPage"
        # resultsKey = "results"
        # venueKey = "venue"
        # if (not requestJson or not requestJson[resultsPageKey] or
        #     not requestJson[resultsPageKey][resultsKey] or
        #     not requestJson[resultsPageKey][resultsKey][venueKey]):
        #     return []

        # venues = requestJson[resultsPageKey][resultsKey][venueKey]

        venue_coords = []
        for venue in self.oldVenues[0 : size]:
            latitude = venue["lat"]
            longitude = venue["lng"]
            if latitude is None or longitude is None:
                continue

            newVenue = Venue(venue["displayName"], latitude, longitude)
            venue_coords.append(newVenue)

        return venue_coords

    # dummy data from previous festivals
    oldVenues = [
        {'displayName': 'PLOEGENDIENST', 'lng': 51.6248573, 'lat': 4.7389255},
        {'displayName': 'VESTROCK', 'lng': 51.283112, 'lat': 4.0283127},
        {'displayName': 'THE FLYING DUTCH - ROTTERDAM', 'lng': 51.8808041, 'lat': 4.4808997},
        {'displayName': 'THE FLYING DUTCH - EINDHOVEN', 'lng': 51.347275, 'lat': 5.3167355},
        {'displayName': 'THE FLYING DUTCH - AMSTERDAM', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'AMSTERDAM OPEN AIR', 'lng': 52.3065615, 'lat': 4.9933607},
        {'displayName': 'FULL MOON FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'OMG! FESTIVAL', 'lng': 51.40993, 'lat': 5.9814482},
        {'displayName': 'PUSSY LOUNGE AT THE PARK', 'lng': 51.6248573, 'lat': 4.7389255},
        {'displayName': 'KOMM SCHON ALTER FESTIVAL', 'lng': 52.3765795, 'lat': 4.783460199999999},
        {'displayName': 'DRIFT FESTIVAL', 'lng': 51.8532423, 'lat': 5.8346224},
        {'displayName': 'BOOTHSTOCK', 'lng': 51.9262323, 'lat': 4.5193922},
        {'displayName': 'OHM FESTIVAL', 'lng': 52.0043623, 'lat': 4.3779313},
        {'displayName': 'BEATCOIN FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'CREATIONS - FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'ATMOZ OUTDOOR', 'lng': 51.4570505, 'lat': 5.503711699999999},
        {'displayName': 'THE LIVING VILLAGE', 'lng': 52.52525, 'lat': 6.288808299999999},
        {'displayName': 'DEFQON1', 'lng': 52.4605804, 'lat': 5.6627062},
        {'displayName': 'CAMP MOONRISE', 'lng': 52.2177917, 'lat': 6.146942},
        {'displayName': 'STRANGE SOUNDS FROM BEYOND', 'lng': 52.4095854, 'lat': 4.8868895},
        {'displayName': 'INDIAN SUMMER FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'PITCH FESTIVAL', 'lng': 52.39230449999999, 'lat': 4.8558842},
        {'displayName': 'LAKESIDE FESTIVAL', 'lng': 52.1333569, 'lat': 4.672636199999999},
        {'displayName': 'BKJN VS PARTYRAISER FESTIVAL', 'lng': 52.05471660000001, 'lat': 4.5090727},
        {'displayName': 'NOMADS FESTIVAL', 'lng': 52.3517216, 'lat': 4.8371533},
        {'displayName': 'STEREO SUNDAY', 'lng': 51.3723862, 'lat': 6.1721338},
        {'displayName': 'EXTREMA OUTDOOR - NETHERLANDS', 'lng': 51.6550094, 'lat': 5.8293974},
        {'displayName': 'IN RETRAITE', 'lng': 51.7154414, 'lat': 5.994456899999999},
        {'displayName': 'WE ARE ELECTRIC', 'lng': 51.347275, 'lat': 5.3167355},
        {'displayName': 'OUTLANDS', 'lng': 51.5990689, 'lat': 5.995824499999999},
        {'displayName': 'ESSENTIAL FESTIVAL', 'lng': 50.8675626, 'lat': 5.9726234},
        {'displayName': 'BY THE CREEK', 'lng': 51.9815011, 'lat': 5.0697869},
        {'displayName': 'GEORGIES WUNDERGARTEN', 'lng': 52.34319319999999, 'lat': 4.817434},
        {'displayName': 'HELLBOUND FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'WASTELAND SUMMERFEST', 'lng': 52.39230449999999, 'lat': 4.8558842},
        {'displayName': 'FESTIFOORT FESTIVAL', 'lng': 52.1624, 'lat': 5.365198299999999},
        {'displayName': 'ELECTRONIC PICNIC', 'lng': 52.4989741, 'lat': 4.9881531},
        {'displayName': 'EXPEDITION FESTIVAL', 'lng': 51.9262323, 'lat': 4.5193922},
        {'displayName': 'VOGELVRIJ FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'DAYLIGHT FESTIVAL', 'lng': 51.5613331, 'lat': 4.545243},
        {'displayName': 'FULL MOON FESTIVAL TILBURG', 'lng': 51.5565973, 'lat': 5.078740799999999},
        {'displayName': 'WE ARE THE FUTURE', 'lng': 52.3087775, 'lat': 4.940659699999999},
        {'displayName': 'WILDEBURG', 'lng': 52.652138, 'lat': 5.906661499999999},
        {'displayName': '18HRS FESTIVAL', 'lng': 52.4419029, 'lat': 4.818048399999999},
        {'displayName': 'INTIEM OUTDOOR FESTIVAL', 'lng': 50.9361951, 'lat': 5.803277},
        {'displayName': 'SUBMERGED - AMSTERDAM', 'lng': 52.39230449999999, 'lat': 4.8558842},
        {'displayName': 'SUNBEATS BEACH FESTIVAL', 'lng': 53.0853945, 'lat': 4.7586682},
        {'displayName': 'DANCE BOULEVARD', 'lng': 51.47135480000001, 'lat': 4.3483687},
        {'displayName': 'SUMMER OF LOVE', 'lng': 52.39230449999999, 'lat': 4.8558842},
        {'displayName': 'EXPLOSION FESTIVAL', 'lng': 52.4938566, 'lat': 6.4734585},
        {'displayName': 'MILKSHAKE FESTIVAL', 'lng': 52.132633, 'lat': 5.291265999999999},
        {'displayName': 'EDELWISE FESTIVAL', 'lng': 52.3670713, 'lat': 4.853111699999999},
        {'displayName': 'ELECTRONIC FAMILY', 'lng': 51.7048327, 'lat': 5.3953314},
        {'displayName': 'FATALITY THE RAW', 'lng': 51.7468601, 'lat': 5.5152837},
        {'displayName': 'VERKNIPT FESTIVAL', 'lng': 52.3517216, 'lat': 4.8371533},
        {'displayName': 'LA REVE FESTIVAL', 'lng': 52.39230449999999, 'lat': 4.8558842},
        {'displayName': 'KARMA OUTDOOR', 'lng': 51.4570505, 'lat': 5.503711699999999},
        {'displayName': 'GAASPERPLEASURE', 'lng': 52.3065615, 'lat': 4.9933607},
        {'displayName': 'DANCETOUR - GOES', 'lng': 51.5057781, 'lat': 3.892463599999999},
        {'displayName': 'GUILTY PLEASURE FESTIVAL', 'lng': 52.3065615, 'lat': 4.993360}
    ]