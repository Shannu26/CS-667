import random
import math
import csv

def genereateChromosome():
	chromosome = []
	genes = set([i for i in range(1, 27)])
	while genes:
		gene = random.choice(list(genes))
		chromosome.append(gene)
		genes.remove(gene)
	return chromosome

def generatePopulation(adjacencyMatrix):
	population = []
	while len(population) != 1000:
		chromosome = genereateChromosome()
		if chromosome not in population: 
			fitness = calculateFitness(chromosome, adjacencyMatrix)
			population.append([chromosome, fitness, 0, 0])
	return population

def calculateFitness(chromosome, adjacencyMatrix):
	fitness = adjacencyMatrix[0][chromosome[0]] + adjacencyMatrix[0][chromosome[-1]]
	for i in range(25):
		fitness += adjacencyMatrix[chromosome[i]][chromosome[i + 1]]

	return fitness

def fillRankAndSelectionProbabilityColumn(population, fitnessToRankMapping):
	sumOfRanks = 1000 * 1001 // 2
	prevProbValue = 0
	for row in population:
		row[2] = fitnessToRankMapping[row[1]][0]
		fitnessToRankMapping[row[1]][0] += 1
		row[3] = prevProbValue + (row[2] / sumOfRanks)
		prevProbValue = row[3]

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

def performSelection(population):
	selectionWheelValue = random.random()

	for index, row in enumerate(population):
		if selectionWheelValue <= row[3]:
			return row[0]

def performCrossover(parent1, parent2):
	locus = random.randint(1, 23)
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

def performMutation(chromosome):
	locus1 = random.randint(0, 25)
	locus2 = random.randint(0, 25)
	chromosome[locus1], chromosome[locus2] = chromosome[locus2], chromosome[locus1]

def mapFitnessToRank(population):
	fitnessToRankMapping = {}
	population = sorted(population, key = lambda row: -row[1])
	for index in range(len(population)):
		if population[index][1] not in fitnessToRankMapping:
			fitnessToRankMapping[population[index][1]] = [index + 1, 0]
		fitnessToRankMapping[population[index][1]][1] += 1
	return fitnessToRankMapping

def findLeastPath(population):
	minPathCost = math.inf
	minPathRow = None

	for row in population:
		if row[1] < minPathCost:
			minPathCost = row[1]
			minPathRow = row

	return minPathRow

def printLeastPath(minPathRow, numberToCityMapping):
	string = "-" * 215
	string += "\n"
	string += "The minimum cost to perform the task is " + str(minPathRow[1]) + "\n"
	string += "The Minimum Cost Path: " + "\n"
	string += numberToCityMapping[0] + "  ->  "
	for i in range(len(minPathRow[0])):
		string += numberToCityMapping[minPathRow[0][i]] + "  ->  "
	string += numberToCityMapping[0]
	string += "\n"
	string += "-" * 215
	string += "\n"

	return string

def writeOutputDataToFile(outputData):
	with open('output' + str(random.random()) + '.txt', mode ='w') as outputFile:
		outputFile.writelines(outputData)

def implementGeneticAlgorithm():
	adjacencyMatrix, numberToCityMapping = getDistanceMatrixFromFile()
	population = generatePopulation(adjacencyMatrix)
	numberOfGenerations = 200
	counts = {}
	outputData = []
	outputData.append("-" * 215 + "\n")

	while numberOfGenerations != 0:
		fitnessToRankMapping = mapFitnessToRank(population)
		fillRankAndSelectionProbabilityColumn(population, fitnessToRankMapping)
		minPathRow = findLeastPath(population)
		if minPathRow[1] not in counts: counts[minPathRow[1]] = 0
		counts[minPathRow[1]] += 1
		outputData.append("Generation " + str(200 - numberOfGenerations + 1) + "\n" + printLeastPath(minPathRow, numberToCityMapping))
		nextGenerationPopulation = []
		crossoverRate = random.randrange(40, 60) / 100
		for _ in range(500):
			parent1 = performSelection(population)
			parent2 = performSelection(population)
			shallWePerformCrossover = random.random()
			if shallWePerformCrossover < crossoverRate:
				child1, child2 = performCrossover(parent1, parent2)
				shallWeMutateChild1 = random.random()
				if shallWeMutateChild1 < 0.01:
					performMutation(child1)
				shallWeMutateChild2 = random.random()
				if shallWeMutateChild2 < 0.01:
					performMutation(child2)
				nextGenerationPopulation.append([child1, calculateFitness(child1, adjacencyMatrix), 0, 0])
				nextGenerationPopulation.append([child2, calculateFitness(child2, adjacencyMatrix), 0, 0])
			else:
				nextGenerationPopulation.append([parent1, calculateFitness(parent1, adjacencyMatrix), 0, 0])
				nextGenerationPopulation.append([parent2, calculateFitness(parent2, adjacencyMatrix), 0, 0])
		population = nextGenerationPopulation
		numberOfGenerations -= 1

	outputData.append("-" * 215 + "\n")
	writeOutputDataToFile(outputData)


def main():
	implementGeneticAlgorithm()

if __name__ == "__main__":
	implementGeneticAlgorithm()

	