import sys
import random
import numpy as np

class Individual(object):
    def __init__(self, lat, long, left_bound,right_bound, upper_bound, lower_bound):
        self.genotype = [lat, long]
        self.fitness = 0
        self.mutation_rate = 1./len(self.genotype)
        self.sigma_lat = 0.01
        self.sigma_long = self.sigma_lat*2
        self.reproduction_prob = 0
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def non_uniform_mutation(self):
        self.try_to_mutate("lat")
        self.try_to_mutate("long")

    def try_to_mutate(self,dir,mean = 0):
        if dir == "lat":
            gene = self.genotype[0]
        elif dir == "long":
            gene = self.genotype[1]

        rand_num = np.random.uniform(0.,1.)
        new_gene = gene
        if rand_num < self.mutation_rate:
            within_bounds = False
            if dir == "lat":
                mutation = np.random.normal(mean, self.sigma_lat)
            elif dir == "long":
                mutation = np.random.normal(mean, self.sigma_long)


            new_gene = gene + mutation

            if dir == "lat":
                within_bounds = self.check_within_lat(new_gene)
            elif dir == "long":
                within_bounds = self.check_within_long(new_gene)

            if not within_bounds:
                new_gene = gene - mutation

        if dir == "lat":
            self.genotype[0] = new_gene
        elif dir == "long":
            self.genotype[1] = new_gene

    def check_within_lat(self,num):
        return self.lower_bound <= num <= self.upper_bound

    def check_within_long(self,num):
        return self.left_bound <= num <= self.right_bound

    def mate(self, mate_partner, alfa = 0.5):
        lat1 = self.genotype[0]*alfa + (1-alfa)*mate_partner.genotype[0]
        lat2 = self.genotype[0]*(1-alfa) + alfa*mate_partner.genotype[0]

        long1 = self.genotype[1] * alfa + (1 - alfa) * mate_partner.genotype[1]
        long2 = self.genotype[1] * (1 - alfa) + alfa * mate_partner.genotype[1]

        child1 = Individual(lat1,long1,self.left_bound, self.right_bound, self.upper_bound, self.lower_bound)
        child2 = Individual(lat2,long2,self.left_bound, self.right_bound, self.upper_bound, self.lower_bound)

        return [child1,child2]