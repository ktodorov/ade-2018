import random
import numpy as np

class Individual(object):
    def __init__(self, lat, long, left_bound,right_bound, upper_bound, lower_bound):
        self.genotype = [lat, long]
        self.fitness = 0
        self.mutation_rate = 1./len(self.genotype)
        self.sigma = 0.1
        self.reproduction_prob = 0
        self.left_bound = 0
        self.right_bound = 0
        self.upper_bound = 0
        self.lower_bound = 0

    def non_uniform_mutation(self):
        [lat,long] = self.genotype
        self.try_to_mutate("lat",self.sigma)
        self.try_to_mutate("long",self.sigma)

    def try_to_mutate(self,gene,sigma,mean = 0):
        if gene == "lat":
            gene = self.genotype[0]
        elif gene == "long":
            gene = self.genotype[1]

        rand_num = np.random.uniform(0, 1.)
        new_gene = 0
        if rand_num < self.mutation_rate:
            within_bounds = False
            while not within_bounds:
                mut = np.random.normal(mean, sigma)
                new_gene = gene + mut
                if gene == "lat":
                    within_bounds = self.check_within_lat(new_gene)
                elif gene == "long":
                    within_bounds = self.check_within_long(new_gene)

        if gene == "lat":
            self.genotype[0] = new_gene
        elif gene == "long":
            self.genotype[1] = new_gene

    def check_within_lat(self,num):
        return self.lower_bound < num < self.upper_bound

    def check_within_long(self,num):
        return self.left_bound < num < self.right_bound

    def mate(self, mate_partner, alfa = 0.5):
        lat1 = self.genotype[0]*alfa + (1-alfa)*self.genotype[0]
        lat2 = self.genotype[0]*(1-alfa) + alfa*self.genotype[0]

        long1 = self.genotype[1] * alfa + (1 - alfa) * self.genotype[1]
        long2 = self.genotype[1] * (1 - alfa) + alfa * self.genotype[1]

        child1 = Individual(lat1,long1,self.left_bound, self.right_bound, self.upper_bound, self.lower_bound)
        child2 = Individual(lat1,long1,self.left_bound, self.right_bound, self.upper_bound, self.lower_bound)

        return [child1,child2]

#Suppliers -> (lat,long,freq)
class Population(object):
    def __init__(self,n_pop, suppliers):
        self.pop = []
        self.size = n_pop
        self.suppliers = suppliers
        self.mating_pool = []
        self.offsprings = []
        self.offspring_size = n_pop
        self.mating_pool_size = n_pop


    def init_pop(self):
        northern_most = 0
        southern_most = 0
        western_most = 0
        eastern_most = 0

        for supplier in self.suppliers:
            [lat,long,_] = supplier

            if lat > northern_most:
                upper_bound = lat

            if lat < southern_most:
                lower_bound = lat

            if long > eastern_most:
                right_bound = long

            if long < western_most:
                left_bound = long

        for _ in range(self.size):
            lat = random.uniform(lower_bound,upper_bound)
            long = random.uniform(left_bound,right_bound)
            assert southern_most <= lat <= northern_most
            assert western_most <= long <= eastern_most
            self.pop.append(Individual(lat,long,left_bound,right_bound, upper_bound, lower_bound))

    def evaluate_population(self, evaluation_func):
        for individual in self.pop:
            individual.fitness = evaluation_func(individual.genotype)

    def sort_pop_by_fitness(self):
        self.pop.sort(key=lambda x: x.fitness, reverse=True)

    def calculate_reproduction_prob(self,s = 1.5):
        self.sort_pop_by_fitness()
        mu = len(self.pop)
        for i in range(len(self.pop)):
            self.pop[i].reproduction_prob = (2.-s)/mu + 2*i*(s-1)/(mu*(mu-1))

    def tournament_selection(self,k):
        current_member = 0
        mating_pool = [None for _ in range(len(self.mating_pool_size))]
        self.calculate_reproduction_prob()
        while current_member <= self.mating_pool_size:
            picked = np.random.choice(self.pop,k)
            picked.sort(key=lambda x: x.fitness)
            best = picked[0]
            mating_pool[current_member] = best
            current_member += 1

        assert len(mating_pool) == self.mating_pool_size

    def make_babies(self):
        while(len(self.offsprings != self.offspring_size)):
            [father,mother] = np.random.choice(self.pop,2,replace=False)
            kids = father.mate(mother)
            for kid in kids:
                self.offsprings.append(kid)

    def select_survivors(self):
        all = []
        for offspring in self.offsprings:
            all.append(offspring)

        for parent in self.mating_pool:
            all.append(parent)

        all.sort(key=lambda x: x.fitness, reverse=True)

        self.pop = []


        while(len(self.pop)):
            self.pop.append(all.pop(0))


POP_SIZE = 3
