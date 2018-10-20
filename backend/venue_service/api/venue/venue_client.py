from .songkick_client import SongkickClient
import numpy as np
import math
import geopy.distance

class VenueClient:
    def findBestVenue(self, optimum, venues):
        # make pairs of (venue, optimum)
        loc_pairs = [((venue[1], venue[2]), optimum) for venue in venues]
        
        # find pair with shortest straight distance, return corresponding venue
        best_venue = loc_pairs[np.argmin([math.sqrt(math.pow(v[0]-o[0],2) + math.pow(v[1]-o[1],2)) for (v, o) in loc_pairs])][0]
        long_lats = [(i[1], i[2]) for i in venues]
        best_index = long_lats.index((best_venue[0], best_venue[1]))

        return venues[best_index], best_index

    def rankVenues(self, optimum, top_n, venues):
        ranked_high_low = []
        for _ in range(top_n):
            venue, index = self.findBestVenue(optimum, venues)
            ranked_high_low.append(venue)
            del venues[index]

        return ranked_high_low