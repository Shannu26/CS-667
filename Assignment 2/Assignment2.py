import random
import csv

population = []

def generatePopulation():
	while len(population) != 1000:
		chromosome = []
		genes = set([i for i in range(1, 27)])
		while genes:
			gene = random.choice(list(genes))
			chromosome.append(str(gene))
			genes.remove(gene)
		chromosome = " ".join(chromosome)
		if chromosome not in population: population.append(chromosome)

generatePopulation()
# print(population)

adjacencyMatrix = [[0] * 27 for _ in range(27)]
adjacencyMatrix[0][0] = 1
# print(adjacencyMatrix)

with open('input.csv', mode ='r') as inputFile:
	inputData = csv.reader(inputFile)
	i = 0
	for line in inputData:
		if i == 0:
			
		print(lines, len(lines))