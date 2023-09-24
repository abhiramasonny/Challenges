import random

class GeneticAlgorithm:
    def __init__(self, func, population_size, generations, mutation_rate, crossover_rate, bit_length=32):
        self.func = func
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.bit_length = bit_length
        self.population = [self.float_to_binary(random.uniform(-100, 100)) for _ in range(self.population_size)]
        self.fitness_cache = {}
        self.best_ever = None

    def cache_key(self, x):
        return (x, int(x * 10000))

    def float_to_binary(self, value):
        int_part = int(value)
        frac_part = value - int_part
        binary_int = format(int_part if int_part >= 0 else 256 + int_part, '08b')
        binary_frac = format(int(frac_part * (2 ** (self.bit_length - 8))), f'0{self.bit_length - 8}b')
        return binary_int + binary_frac

    def binary_to_float(self, binary):
        binary_int = binary[:8]
        binary_frac = binary[8:]
        int_part = int(binary_int, 2)
        frac_part = int(binary_frac, 2) / (2 ** (self.bit_length - 8))
        if int_part >= 128:
            int_part -= 256
        return int_part + frac_part

    def fitness(self, binary_x):
        x = self.binary_to_float(binary_x)
        key = self.cache_key(x)
        if key not in self.fitness_cache:
            self.fitness_cache[key] = max(abs(self.func(x)), round(abs(self.func(x)), 1))
        return self.fitness_cache[key]

    def tournament_selection(self, k=5):
        return min(random.choices(self.population, k=k), key=self.fitness)

    def double_point_crossover(self, parent1, parent2):
        alpha, beta = sorted(random.sample(range(len(parent1)), 2))
        child = parent1[:alpha] + parent2[alpha:beta] + parent1[beta:]
        return child

    def mutate(self, binary):
        index = random.randrange(len(binary))
        mutated = list(binary)
        mutated[index] = '1' if binary[index] == '0' else '0'
        return ''.join(mutated)

    def evolve(self):
        for generation in range(self.generations):
            self.population.sort(key=self.fitness)
            current_best = min(self.population, key=self.fitness)
            
            if self.best_ever is None or self.fitness(current_best) < self.fitness(self.best_ever):
                self.best_ever = current_best

            current_best_fitness = self.fitness(current_best)
            if current_best_fitness < 1e-3:
                print("Converged")
                return

            elites = list(set(self.population[:self.population_size // 10]))
            next_generation = elites[:]
            
            if generation > 0.8 * self.generations:
                self.mutation_rate /= 1.1

            direct_count = int(0.1 * self.population_size)
            crossover_count = int(self.crossover_rate * (self.population_size - len(elites) - direct_count))
            mutation_count = self.population_size - len(elites) - crossover_count - direct_count

            next_generation.extend(self.population[:direct_count])

            for _ in range(crossover_count):
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                child = self.double_point_crossover(parent1, parent2)
                next_generation.append(child)

            for _ in range(mutation_count):
                individual = random.choice(self.population)
                next_generation.append(self.mutate(individual))
            
            self.population = next_generation

    def best_solution(self):
        best = min(self.population, key=self.fitness)
        return self.binary_to_float(best), self.func(self.binary_to_float(best))


if __name__ == '__main__':
    def f(x):
        return x**5 + x**4 + x**3 + x**2 + x + 1

    ga = GeneticAlgorithm(f, population_size=1000, generations=10000, mutation_rate=0.05, crossover_rate=0.7)
    ga.evolve()
    best, result = ga.best_solution()

    print(f"Root: {best}, Value: {result}")
    print(f"Round: {round(best,3)}, Value: {f(round(best,3))}")
