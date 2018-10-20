import numpy as np
import csv

N_VISITORS = 45000
def visiters_per_city(visitors):
    uniques, counts = np.unique(visitors, return_counts=True)
    uniquecounts = zip(uniques, counts)

def pick_visitors(n):
    with open("NL_demographics.csv", 'rt') as file:
        rows = []
        file = csv.reader(file, delimiter='\n', quotechar='|')
        for i in file:
            i = i[0].split(",")
            i[1] = int(i[1])
            rows.append(i)

        inhabits = [float(row[1]) for row in rows]
        total_inhabits = sum(inhabits)
        probs = [x / float(total_inhabits) for x in inhabits]
        cities = [city[0] for city in rows]
        picked = np.random.choice(cities, n, p=probs)
    return picked

def count_occ(n):
    city_count, counts = np.unique(pick_visitors(n), return_counts=True)
    return zip(city_count, counts)

# example call
# print(count_occ(N_VISITORS))
