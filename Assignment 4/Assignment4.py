import csv
import random
import math

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

def performTour(distanceMatrix, visibilityMatrix, pheromoneMatrix, startingCity, beta):
	tour = [startingCity]

	while len(tour) != 27:
		currentCity = tour[-1]
		nextCity = -1
		nextCityProbability = -1
		probabilityDenominator = 0
		for city in range(27):
			if city not in tour: 
				probabilityDenominator += pheromoneMatrix[currentCity][city] * pow(visibilityMatrix[currentCity][city], beta)

		for city in range(27):
			if city not in tour:
				probability = (pheromoneMatrix[currentCity][city] * pow(visibilityMatrix[currentCity][city], beta)) / probabilityDenominator
				# print(city, probability)
				if probability > nextCityProbability:
					nextCityProbability = probability
					nextCity = city

		# print(nextCity, nextCityProbability)
		# print()
		tour.append(nextCity)

	return tour

def calculateTourLength(tour, distanceMatrix):
	tourLength = 0
	for i in range(26):
		tourLength += distanceMatrix[tour[i]][tour[i + 1]]
	tourLength += distanceMatrix[tour[-1]][tour[0]]
	return tourLength

def addPheromoneTrace(tour, tourLength, pheromoneMatrix, Q):
	for i in range(26):
		pheromoneMatrix[tour[i]][tour[i + 1]] += Q / tourLength
	pheromoneMatrix[tour[-1]][tour[0]] += Q / tourLength

def performPheromoneEvaporation(pheromoneMatrix, rho):
	for row in range(27):
		for col in range(27):
			pheromoneMatrix[row][col] = rho * pheromoneMatrix[row][col]

def findLeastTour(antTours):
	minTourCost = math.inf
	minTour = None

	for tour in antTours:
		if tour[1] < minTourCost:
			minTourCost = tour[1]
			minTour = tour

	return minTour

def printLeastTour(tour, tourLength, numberToCityMapping):
	string = "-" * 215
	string += "\n"
	string += "The minimum cost to perform the task is " + str(tourLength) + "\n"
	string += "The Minimum Cost Path: " + "\n"
	for city in tour:
		string += numberToCityMapping[city] + "  ->  "
	string += numberToCityMapping[tour[0]]
	string += "\n"
	string += "-" * 215
	string += "\n"

	return string

def writeOutputDataToFile(outputData):
	with open('output.txt', mode ='w') as outputFile:
		outputFile.writelines(outputData)

def implementAntColonyOptimizationAlgorithm(numberOfAnts, numberOfIterations, alpha, beta, rho, Q):
	distanceMatrix, numberToCityMapping = getDistanceMatrixFromFile()
	visibilityMatrix = [[math.inf] * 27 for _ in range(27)]
	pheromoneMatrix = [[alpha] * 27 for _ in range(27)]
	outputData = []
	outputData.append("-" * 215 + "\n")
	for row in range(27):
		for col in range(27):
			if row != col:
				visibilityMatrix[row][col] = 1 / distanceMatrix[row][col]

	for i in range(numberOfIterations):
		# print(pheromoneMatrix)
		antTours = []
		for antNumber in range(numberOfAnts):
			startingCity = random.randint(0, 26)
			tour = performTour(distanceMatrix, visibilityMatrix, pheromoneMatrix, startingCity, beta)
			tourLength = calculateTourLength(tour, distanceMatrix)
			antTours.append([tour, tourLength])

		minTour, minTourCost = findLeastTour(antTours)
		# print(minTour, minTourCost)
		outputData.append("Iteration " + str(i + 1) + "\n")
		outputData.append(printLeastTour(minTour, minTourCost, numberToCityMapping))
		performPheromoneEvaporation(pheromoneMatrix, rho)
		for tour, tourLength in antTours:
			addPheromoneTrace(tour, tourLength, pheromoneMatrix, Q)

	writeOutputDataToFile(outputData)

if __name__ == "__main__":
	numberOfAnts = 27
	numberOfIterations = 1000
	alpha = 10
	beta = 2
	rho = 0.5
	Q = 10000
	implementAntColonyOptimizationAlgorithm(numberOfAnts, numberOfIterations, alpha, beta, rho, Q)
