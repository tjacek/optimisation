import numpy as np

class Variation(object):
    def __init__(self, n_descendants):
        self.n_descendants = n_descendants

    def new_population(self,fitness,population):
        multipled_population=self.next_generation(population)
        selected_population=multipled_population.select(fitness,self.n_descendants)
        return selected_population

class MutationVariation(Variation):
    def __init__(self, n_descendants=2):
        super(MutationVariation,self).__init__(n_descendants)

    def next_generation(self,popul):
        new_individuals=[]
        for indiv_i in popul:
            new_individuals+=[indiv_i.mutate() 
                                for i in range(super.n_descendants)]
        return population.Population(new_individuals)

class CrossoverVariation(Variation):
    def __init__(self, n_descendants=4):
        super(CrossoverVariation,self).__init__(n_descendants)

    def multiply_crossover(self,popul):
        new_individuals=[]
        pairs=random_pairs(popul)
        parent_pairs=[CrossoverPair(pair_i)
                        for pair_i in pairs]
        for pair_i in parent_pairs:             
            new_individuals+=[ pair_i() 
                                for t in range(self.n_descendants)]
        return population.Population(new_individuals)

class CrossoverPair(object):
    def __init__(self,pair):
        self.pair=pair
    
    def __call__(self):
        dim=len(self.pair[0])
        genes=[self.get_gene(j) 
                for j in range(dim)]
        return Individual(np.array(genes))

    def get_gene(self,j):
        choice_j=random.choice([0, 1])
        return self.pair_i[choice_j][j]

def random_pairs(popul):
    n_pairs=len(popul)/2
    def get_pair(i):
        return (popul[2*i],popul[2*i+1])
    random.shuffle(popul)
    pairs=[get_pair(i) 
            for i in range(n_pairs)]
    return pairs