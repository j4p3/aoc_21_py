import utils.input as input


def one(filename):
    population = parse_input(filename)
    projected_population = project(population, 80)
    return sum(projected_population.values())


def two(filename):
    population = parse_input(filename)
    projected_population = project(population, 256)
    return sum(projected_population.values())


def project(population, days):
    day = 0
    while day < days:
        spawning = population[0]
        for age in range(1, 9):
            population[age - 1] = population[age]
        population[6] += spawning
        population[8] = spawning
        day += 1
    return population


def parse_input(filename):
    [line] = input.file_lines(f"/days/six/{filename}.txt")
    fish = [int(c) for c in line.split(",")]
    population = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for f in fish:
        population[f] += 1
    return population
