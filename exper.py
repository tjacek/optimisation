import population
import fitness

def experiment(fitness_fun,popul,iter=50):
    for i in range(iter):
        popul=new_population(fitness_fun,popul,k=2)
        print(i)
        print(popul.average_fitness(fitness_fun))
    return popul

def new_population(fitness,population,k=2):
    multipled_population=multiply(population,k)
    print(len(multipled_population))
    selected_population=multipled_population.select(fitness)
    return selected_population

def multiply(popul,k=2):
    new_individuals=[]
    def make_children(indiv_i):
        return [indiv_i.mutate() for i in range(k)]
    for indiv_i in popul:
        new_individuals+=make_children(indiv_i)
    return population.Population(new_individuals)

popul=population.make_population(100,1000)
fitness_fun=fitness.simple_sum
experiment(fitness_fun,popul)
#new_pop=multiply(popul)
#print(len(new_pop))
#print(popul.avrage_fitness(fitness.simple_sum))