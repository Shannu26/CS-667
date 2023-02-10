import random
import csv

def genereateChromosome():
	chromosome = []
	genes = set([i for i in range(1, 27)])
	while genes:
		gene = random.choice(list(genes))
		chromosome.append(gene)
		# chromosome.append(str(gene))
		genes.remove(gene)
	# chromosome = " ".join(chromosome)
	return chromosome

def generatePopulation(adjacencyMatrix):
	population = []
	while len(population) != 1000:
		chromosome = genereateChromosome()
		if chromosome not in population: 
			fitness = calculateFitness(chromosome, adjacencyMatrix)
			population.append([chromosome, fitness])

	return population

def calculateFitness(chromosome, adjacencyMatrix):
	fitness = adjacencyMatrix[0][chromosome[0]] + adjacencyMatrix[0][chromosome[-1]]
	for i in range(25):
		fitness += adjacencyMatrix[i][i + 1]

	return fitness
	# print(chromosome, fitness)

def getDistanceMatrixFromFile():
	adjacencyMatrix = [[0] * 27 for _ in range(27)]
	adjacencyMatrix[0][0] = 1
	numberToCityMapping = {}

	with open('input.csv', mode ='r') as inputFile:
		inputData = csv.reader(inputFile)
		row = 0
		for line in inputData:
			if row == 0: 
				for index in range(len(line)):
					numberToCityMapping[index] = line[index]
			else:
				for col in range(len(line)):
					adjacencyMatrix[row - 1][col] = int(line[col])
					adjacencyMatrix[col][row - 1] = int(line[col])

			row += 1

	return adjacencyMatrix, numberToCityMapping

def performCrossover(parent1, parent2):
	locus = random.randint(1, 23)
	print(locus)
	child1 = [-1] * 26
	child2 = [-1] * 26

	for index in range(locus, locus + 3):
		child1[index] = parent1[index]
		child2[index] = parent2[index]

	parent2Index = locus + 3
	child1Index = locus + 3
	while child1Index != locus:
		if child1Index == 26: 
			child1Index = 0
			continue
		if parent2Index == 26:
			parent2Index = 0
		if parent2[parent2Index] not in child1: 
			child1[child1Index] = parent2[parent2Index]
			child1Index += 1
		parent2Index += 1

	parent1Index = locus + 3
	child2Index = locus + 3
	while child2Index != locus:
		if child2Index == 26:
			child2Index = 0
			continue
		if parent1Index == 26:
			parent1Index = 0
		if parent1[parent1Index] not in child2:
			child2[child2Index] = parent1[parent1Index]
			child2Index += 1
		parent1Index += 1

	return child1, child2

def mapFitnessToRank(population):
	fitnessToRankMapping = {}
	population = sorted(population, key = lambda row: row[1])
	rank = 1
	for index in range(len(population)):
		if index != 0 and population[index][1] == population[index - 1][1]: continue
		fitnessToRankMapping[population[index][1]] = rank
		rank += 1
	return fitnessToRankMapping

def main():
	adjacencyMatrix, numberToCityMapping = getDistanceMatrixFromFile()
	population = generatePopulation(adjacencyMatrix)
	#print(population[:10])
	# print(population[0], population[-1])
	# print(numberToCityMapping)
	#print(adjacencyMatrix)
	fitnessToRankMapping = mapFitnessToRank(population)
	# print(fitnessToRankMapping)
	print(population[0][0])
	print(population[1][0])
	child1, child2 = performCrossover(population[0][0], population[1][0])
	print(child1)
	print(child2)


if __name__ == "__main__":
	main()