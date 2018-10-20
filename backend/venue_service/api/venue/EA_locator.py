from .evolutionary import Population,Individual
import geopy.distance

def evaluation(solution, frequencies, data):
    sum = 0.000
    for i in range(len(frequencies)):
        sum += frequencies[i] * geopy.distance.vincenty(solution, data[i]).km

    return 1000000/sum


# Returns the best location based on a number of suppliers and their respective weights (frequencies)
# Evaluation: the function that evaluates how good a coordinate is
# frequencies: a list of how frequently each supplier needs to go back and forth to the festival
# data: a list of the data for each supplier in the form of ['Address', 'zip code', "frequencies", 'lat', 'long']
def get_best_location(evaluation, data):
    coords = [[float(i[-2]), float(i[-1])] for i in data]
    frequencies = [float(i[-3])for i in data]
    
    popSize = 50
    pop = Population(popSize, data)
    pop.init_pop()
    for i in range(100):
        best,converged = pop.evolve(evaluation,frequencies,coords,2)
        if converged:
            return best.genotype