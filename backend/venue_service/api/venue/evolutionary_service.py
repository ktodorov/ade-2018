from .evolutionary.population import Population
from .evolutionary.individual import Individual
from .models.location import Location
from .gmaps_service import GMapsService
import geopy.distance

class EvolutionaryService:
    def evaluation(self, solution, suppliers, gmapsService):
        sum = 0.000
        for supplier in suppliers:
            candidate = Location(solution[0], solution[1])
            distance = gmapsService.calculateDistance(candidate, supplier.location)
            if not distance:
                continue

            sum += supplier.frequency * distance.kilometers

        if sum == 0:
            return -1
        
        return 1000000/sum

    def getBestLocation(self, suppliers, gmapsService):
        '''
            Returns the best location based on a number of suppliers and their respective weights (frequencies)
            Evaluation: the function that evaluates how good a coordinate is
            frequencies: a list of how frequently each supplier needs to go back and forth to the festival
            data: a list of the data for each supplier in the form of ['Address', 'zip code', "frequencies", 'lat', 'long']
        '''
        
        popSize = 10
        maxCycles = 100
        pop = Population(popSize, suppliers, gmapsService)
        pop.init_pop()
        for i in range(maxCycles):
            best,converged = pop.evolve(self.evaluation, 2)
            if converged:
                return Location(best.genotype[0], best.genotype[1])
            
            print ("best for cycle ", i, " is ", best.genotype)