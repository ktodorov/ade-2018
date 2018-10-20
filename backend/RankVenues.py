from VenueFinder import find_venues
import numpy as np
import math

def best_venue(optimum, venues):
    # make pairs of (venue, optimum)
    loc_pairs = [((venue[1], venue[2]), optimum_bijlmer) for venue in venues]
    # find pair with shortest straight distance, return corresponding venue
    best_venue = loc_pairs[np.argmin([math.sqrt(math.pow(v[0]-o[0],2) + math.pow(v[1]-o[1],2)) for (v, o) in loc_pairs])][0]
    long_lats = [(i[1], i[2]) for i in venues]
    best_index = long_lats.index((best_venue[0], best_venue[1]))
    return venues[best_index], best_index

def rank_venues(optimum, top_n):
    ranked_high_low = []
    for i in range(top_n):
        venue, index = best_venue(optimum, venues)
        ranked_high_low.append(venue)
        del venues[index]
    return ranked_high_low

# get find n=20 venues in "amsterdam"
venues = find_venues("amsterdam",20)

# mock examples
optimum_amstel = (52.360503, 4.905650)
optimum_bijlmer = (52.323174, 4.943041)

ranked = rank_venues(optimum_bijlmer, 5)
print(ranked)
