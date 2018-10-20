from evolutionary import Population,Individual
from DataReader import open_file
import random
import geopy.distance
import time


def evaluation(solution, frequencies, data):
    assert len(data) == len(frequencies)
    sum = 0.000
    for i in range(len(frequencies)):
        sum += frequencies[i]*geopy.distance.vincenty(solution,data[i]).km

    return 1000000/sum



data = open_file("test_data.csv")

# Mock frequencies
# frequency 1 represents a back and forth
frequencies = []
for i in range(len(data)-1):
    frequencies.append(random.randint(1,10))
frequencies.append(50)

# Returns the best location based on a number of suppliers and their respective weights (frequencies)
# Evaluation: the function that evaluates how good a coordinate is
# frequencies: a list of how frequently each supplier needs to go back and forth to the festival
# data: a list of the data for each supplier in the form of ['Address', 'zip code', 'lat', 'long']
def get_best_location(evaluation, frequencies, data):
    coords = [[float(i[-2]), float(i[-1])] for i in data]
    popSize = 50
    pop = Population(popSize, data)
    pop.init_pop()
    for i in range(100):
        best,converged = pop.evolve(evaluation,frequencies,coords,2)
        if converged:
            return best.genotype

print(get_best_location(evaluation, frequencies, data))

