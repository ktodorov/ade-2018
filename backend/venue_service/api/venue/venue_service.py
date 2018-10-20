import math
from .models.venue import Venue
from .models.scored_venue import ScoredVenue

class VenueService:
    def getTopVenue(self, optimum, venues):
        scoredVenues = self.getTopVenues(optimum, venues)
        if not scoredVenues or  len(scoredVenues) <= 0:
            return None
        
        return scoredVenues[0]

    def getTopVenues(self, optimum, venues, size = -1):

        scoredVenues = []
        for venue in venues:
            score = math.sqrt(math.pow(venue.latitude - optimum.latitude, 2) + math.pow(venue.longitude - optimum.longitude, 2))
            scoredVenue = ScoredVenue(venue, score)
            scoredVenues.append(scoredVenue)

        scoredVenues.sort(key=lambda x: x.score)
        return scoredVenues