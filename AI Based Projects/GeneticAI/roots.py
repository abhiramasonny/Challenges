import random
import math
def f(x):
    return math.cos(x)
def fitness(x):
    return abs(f(x))

population_size = 100
population = [random.uniform(-10, 10) for _ in range(population_size)]

generations = 1000
mutation_rate = 0.05
crossover_rate = 0.7

for generation in range(generations):
    population = sorted(population, key=fitness)[:population_size//2]

    next_generation = []
    for i in range(population_size//2):
        if random.random() < crossover_rate:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = (parent1 + parent2) / 2
            next_generation.append(child)
        else:
            next_generation.append(random.choice(population))

    for i in range(len(next_generation)):
        if random.random() < mutation_rate:
            next_generation[i] += random.uniform(-1, 1)
            
    population += next_generation

best_solution = min(population, key=fitness)
print(f"root: {best_solution}, pluged in: {f(best_solution)}")

