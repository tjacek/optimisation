import population
import fitness
import variation

class PlotBuilder(object):
    def __init__(self,n_exper,indiv_dim,step=10):
        self.indiv_dim=indiv_dim
        self.step=step

#    def init_exper(self):
        
class Experiment(object):
    def __init__(self, n_popul,indiv_dim,fitness_fun,variation):
        self.n_popul=n_popul
        self.indiv_dim=indiv_dim
        self.fitness_fun=fitness_fun
        self.variation=variation
        self.popul=None
        self.all_iters=0

    def __call__(self,n_iters):
        if(self.popul==None):
            self.popul=population.make_population(self.n_popul,self.indiv_dim)
        for i in range(n_iters):
            self.popul=self.variation.new_population(self.fitness_fun,self.popul)
            print(len(self.popul))
            print(self.popul.average_fitness(self.fitness_fun))
        self.all_iters+=n_iters
        return self.popul
    
    def reset(self):
        self.popul=None
        self.all_iters=0

exp=Experiment(n_popul=100,indiv_dim=1000,
               fitness_fun=fitness.simple_sum,
               variation= variation.CrossoverVariation())
exp(50)
