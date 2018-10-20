from .songkick_client import SongkickClient
import numpy as np
import math
import geopy.distance
from .models import Venue, ScoredVenue

class VenueClient:
    songkickClient = SongkickClient()

    def getTopVenue(self, optimum, venues):
        scoredVenues = self.getTopVenues(optimum, venues)
        return scoredVenues[0]

    def getTopVenues(self, optimum, venues, size = -1):
        scoredVenues = []
        for venue in venues:
            score = math.sqrt(math.pow(venue.latitude - optimum.latitude, 2) + math.pow(venue.longitude - optimum.longitude, 2))
            scoredVenue = ScoredVenue(venue, score)
            scoredVenues.append(scoredVenue)

        scoredVenues.sort(key=lambda x: x.score)
        return scoredVenues