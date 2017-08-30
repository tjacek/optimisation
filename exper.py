import population
import fitness
import random

def experiment(fitness_fun,popul,iter=50):
    for i in range(iter):
        popul=new_population(fitness_fun,popul,k=2)
        print(i)
        print(popul.average_fitness(fitness_fun))
    return popul

popul=population.make_population(100,1000)
fitness_fun=fitness.simple_sum
experiment(fitness_fun,popul)
#new_pop=multiply(popul)
#print(len(new_pop))
#print(popul.avrage_fitness(fitness.simple_sum))