from .evolutionary import Population,Individual
from .location import Location
from .gmaps_client import GMapsClient
import geopy.distance


def evaluation(solution, frequencies, data, gmapsClient):
    sum = 0.000
    for i in range(len(frequencies)):
        candidate = Location(solution[0],solution[1])
        supplier = Location(data[i][0],data[i][1])
        distance = gmapsClient.calculateDistance(candidate, supplier)
        if not distance:
            continue

        sum += frequencies[i] * distance.kilometers

    if sum == 0:
        return -1
    
    return 1000000/sum


# Returns the best location based on a number of suppliers and their respective weights (frequencies)
# Evaluation: the function that evaluates how good a coordinate is
# frequencies: a list of how frequently each supplier needs to go back and forth to the festival
# data: a list of the data for each supplier in the form of ['Address', 'zip code', "frequencies", 'lat', 'long']
def get_best_location(evaluation, data, gmapsClient):
    coords = [[float(i[-2]), float(i[-1])] for i in data]
    frequencies = [float(i[-3])for i in data]
    
    popSize = 10
    pop = Population(popSize, data, gmapsClient)
    pop.init_pop()
    for i in range(100):
        best,converged = pop.evolve(evaluation,frequencies,coords,2)
        if converged:
            return best.genotype
        
        print ("best for cycle ", i, " is ", best.genotype)