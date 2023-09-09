import random
import math
class GeneticAlgorithm:
    def __init__(self, func, population_size, generations, mutation_rate, crossover_rate, mutation_scale):
        self.func = func
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.mutation_scale = mutation_scale
        self.population = [random.uniform(-100, 100) for _ in range(self.population_size)]
        self.fitness_cache = {}
        self.best_ever = None

    def cache_key(self, x):
        return (x, int(x * 10000))

    def fitness(self, x):
        key = self.cache_key(x)
        if key not in self.fitness_cache:
            self.fitness_cache[key] = max(abs(self.func(x)), round(abs(self.func(x)),3))
        return self.fitness_cache[key]

    def tournament_selection(self, k=5):
        return min(random.choices(self.population, k=k), key=self.fitness)

    def double_point_crossover(self, parent1, parent2):
        alpha, beta = sorted(random.sample(range(len(str(parent1))), 2))
        child = parent1[:alpha] + parent2[alpha:beta] + parent1[beta:]
        return child

    def evolve(self):
        stagnant_generations = 0
        for generation in range(self.generations):
            self.population.sort(key=self.fitness)
            
            current_best = min(self.population, key=self.fitness)
            if self.best_ever is None or self.fitness(current_best) < self.fitness(self.best_ever):
                self.best_ever = current_best
            else:
                stagnant_generations += 1

            if stagnant_generations > 0.1 * self.generations:
                print("Converged")
                return

            elites = list(set(self.population[:self.population_size // 10]))
            next_generation = elites[:]

            if generation > 0.8 * self.generations:
                self.mutation_rate /= 1.1

            crossover_count = int(self.crossover_rate * (self.population_size - len(elites)))
            mutation_count = self.population_size - len(elites) - crossover_count

            for _ in range(crossover_count):
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                child = (parent1 + parent2) / 2
                next_generation.append(child)

            for individual in random.sample(self.population, mutation_count):
                next_generation.append(individual + random.uniform(-self.mutation_scale, self.mutation_scale))
            
            self.population = next_generation

    def best_solution(self):
        best = min(self.population, key=self.fitness)
        return best, self.func(best)

if __name__ == '__main__':
    def f(x):
        return 3 * x + 2

    ga = GeneticAlgorithm(f, population_size=100, generations=10000, mutation_rate=0.05, crossover_rate=0.7, mutation_scale=2)
    ga.evolve()
    best, result = ga.best_solution()

    print(f"root: {best}, plugged in: {result}")
    print(f"round: {round(best,3)}, plugged in: {f(round(best,3))}")
