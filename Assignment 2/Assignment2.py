import random

population = []

def generatePopulation():
	while len(population) != 1000:
		chromosome = []
		genes = set([i for i in range(1, 20)])
		while genes:
			gene = random.choice(list(genes))
			chromosome.append(str(gene))
			genes.remove(gene)
		chromosome = " ".join(chromosome)
		if chromosome not in population: population.append(chromosome)

generatePopulation()
print(population)