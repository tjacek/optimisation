import numpy as np 

class Population(object):
    def __init__(self, individuals):
        self.individuals = individuals

    def __len__(self):
        return len(self.individuals)
        
    def __getitem__(self,index):
        return self.individuals[index]

    def dim(self):
        return len(self.individuals[0])

    def select(self,fitness_fun,k=None):
        if(k==None):
            k=len(self)/2
        fitness=np.array(self.fitness_list(fitness_fun))
        indexes=np.flip(np.argsort(fitness),axis=0)
        selected_indexes=indexes[0:k]
        selected_individuals=[self.individuals[i] 
                                for i in selected_indexes]
        return Population(selected_individuals)

    def average_fitness(self, fitness_fun):
        total_fitness=sum(self.fitness_list(fitness_fun))
        size=float(len(self))
        return (total_fitness/size)

    def fitness_list(self,fitness_fun):
        return [ fitness_fun(individual_i)
                            for individual_i in self.individuals]	

class Individual(object):
    def __init__(self,genes):
        self.genes=genes
		
    def __len__(self):
        return self.genes.shape[0]

    def __getitem__(self,index):
        return self.genes[index]

    def mutate(self,threshold=0.1):
        bits=self.genes.astype(bool)	
        def flip(bit_i):
            rscalar=np.random.rand()
            if(rscalar<threshold):
                return (not bit_i)
            return bit_i
        new_genes=[ flip(bit_i) for bit_i in bits]
        new_genes=np.array(new_genes).astype(float)
        return Individual(new_genes)

class Crossover(object):
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

def make_population(n,dim):
    individuals=[ make_individual(dim)  
                    for i in range(n)]
    return Population(individuals)

def make_individual(dim):	
    genes=np.random.rand(dim)
    genes[0.5<genes]=1.0
    genes[genes!=1.0]=0.0
    return Individual(genes)