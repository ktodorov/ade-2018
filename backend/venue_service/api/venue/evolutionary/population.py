import sys
import random
import numpy as np
from .individual import Individual

#Suppliers -> (lat,long,freq)
class Population(object):
    def __init__(self,n_pop, suppliers, gmapsClient):
        self.pop = []
        self.size = n_pop
        self.suppliers = suppliers
        self.mating_pool = []
        self.offsprings = []
        self.offspring_size = n_pop
        self.mating_pool_size = n_pop
        self.gmapsClient = gmapsClient


    def init_pop(self):
        upper_bound = -sys.maxsize
        lower_bound = +sys.maxsize
        left_bound = +sys.maxsize
        right_bound = -sys.maxsize

        for supplier in self.suppliers:
            lat = float(supplier[-2])
            long = float(supplier[-1])

            if lat > upper_bound:
                upper_bound = lat

            if lat < lower_bound:
                lower_bound = lat

            if long > right_bound:
                right_bound = long

            if long < left_bound:
                left_bound = long

        for _ in range(self.size):
            lat = random.uniform(lower_bound,upper_bound)
            long = random.uniform(left_bound,right_bound)
            assert lower_bound <= lat <= upper_bound
            assert left_bound <= long <= right_bound
            self.pop.append(Individual(lat,long,left_bound,right_bound, upper_bound, lower_bound))

    def evaluate_group(self,group, evaluation_func, frequencies, coords):
        for individual in group:
            individual.fitness = evaluation_func(individual.genotype,frequencies,coords, self.gmapsClient)

    def sort_pop_by_fitness(self):
        self.pop.sort(key=lambda x: x.fitness, reverse=True)

    def calculate_reproduction_prob(self,s = 1.5):
        self.sort_pop_by_fitness()
        mu = len(self.pop)
        for i in range(len(self.pop)):
            self.pop[i].reproduction_prob = (2.-s)/mu + 2*i*(s-1)/(mu*(mu-1))

    def tournament_selection(self,k):
        current_member = 0
        mating_pool = [None for _ in range(self.mating_pool_size)]
        self.calculate_reproduction_prob()
        while current_member < self.mating_pool_size:
            picked = list(np.random.choice(self.pop,k))
            picked.sort(key=lambda x: x.fitness, reverse=True)
            best = picked[0]
            mating_pool[current_member] = best
            current_member += 1


        assert len(mating_pool) == self.mating_pool_size
        self.mating_pool = mating_pool

    def make_babies(self):
        while(len(self.offsprings) != self.offspring_size):
            [father,mother] = np.random.choice(self.pop,2,replace=False)
            kids = father.mate(mother)
            for kid in kids:
                kid.non_uniform_mutation()
                self.offsprings.append(kid)

    def select_survivors(self):
        all = []
        for offspring in self.offsprings:
            all.append(offspring)

        for parent in self.mating_pool:
            all.append(parent)

        all.sort(key=lambda x: x.fitness, reverse=True)

        self.pop = []
        self.offsprings = []

        while(len(self.pop) < self.size):
            self.pop.append(all.pop(0))

    def substitute_gen(self):
        self.pop = []
        for i in range(len(self.offsprings)):
            self.pop.append(self.offsprings[i])

        self.offsprings = []

    def print_population(self):
        for i in range(len(self.pop)):
            print("Individual with genotype {} with fitness {}".format(self.pop[i].genotype,self.pop[i].fitness))


    def check_convergence(self,old_pop, new_pop):
        sum = 0
        for i in range(len(old_pop)):
            sum += (old_pop[i].genotype[0] - new_pop[i].genotype[0]) + (old_pop[i].genotype[1] - new_pop[i].genotype[1])

        if sum == 0:
            return True
        else:
            return False


    def evolve(self, evaluation, frequencies, long_lats, k):
        old_pop = copy.deepcopy(self.pop)
        self.evaluate_group(self.pop, evaluation, frequencies, long_lats)
        self.calculate_reproduction_prob()
        self.tournament_selection(k)
        self.make_babies()
        self.evaluate_group(self.offsprings, evaluation, frequencies, long_lats)
        self.select_survivors()
        new_pop = copy.deepcopy(self.pop)
        converged = self.check_convergence(old_pop,new_pop)
        return self.pop[0], converged
