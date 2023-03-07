import csv
import random
import math

def getDistanceMatrixFromFile():
	distanceMatrix = [[0] * 27 for _ in range(27)]
	distanceMatrix[0][0] = 1
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
					distanceMatrix[row - 1][col] = int(line[col])
					distanceMatrix[col][row - 1] = int(line[col])

			row += 1

	return distanceMatrix, numberToCityMapping

def performTour(distanceMatrix, visibilityMatrix, pheromoneMatrix, startingCity, beta, randomCityChoosingRate):
	tour = [startingCity]

	while len(tour) != 27:
		currentCity = tour[-1]
		nextCity = -1
		nextCityProbability = -1
		probabilityDenominator = 0

		shallWeChooseCityRandomly = random.random()
		if shallWeChooseCityRandomly < randomCityChoosingRate:
			remainingCities = [city for city in range(27) if city not in tour]
			nextCity = random.choice(remainingCities)
		else:
			for city in range(27):
				if city not in tour: 
					probabilityDenominator += pheromoneMatrix[currentCity][city] * pow(visibilityMatrix[currentCity][city], beta)

			for city in range(27):
				if city not in tour:
					probability = (pheromoneMatrix[currentCity][city] * pow(visibilityMatrix[currentCity][city], beta)) / probabilityDenominator
					if probability > nextCityProbability:
						nextCityProbability = probability
						nextCity = city
		tour.append(nextCity)

	return tour

def calculateTourLength(tour, distanceMatrix):
	tourLength = 0
	for i in range(26):
		tourLength += distanceMatrix[tour[i]][tour[i + 1]]
	tourLength += distanceMatrix[tour[-1]][tour[0]]
	return tourLength

def addPheromoneTrace(tour, tourLength, numberOfTimesThatTourOccured, pheromoneMatrix, Q):
	for i in range(26):
		pheromoneMatrix[tour[i]][tour[i + 1]] += Q * numberOfTimesThatTourOccured / tourLength
	pheromoneMatrix[tour[-1]][tour[0]] += Q * numberOfTimesThatTourOccured / tourLength

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

def checkIfTourAlreadyExists(antTours, currentTour, currentTourLength):
	for antTour in antTours:
		if antTour[1] == currentTourLength:
			cityIndex = currentTour.index(antTour[0][0])
			isSameTour = True
			for city in antTour[0]:
				if city != currentTour[cityIndex]:
					isSameTour = False
					break
				if cityIndex == 26: cityIndex = -1
				cityIndex += 1

			if isSameTour:
				antTour[-1] += 1
				return True
	return False

def implementAntColonyOptimizationAlgorithm(numberOfAnts, numberOfIterations, alpha, beta, rho, Q, randomCityChoosingRate, bestAntPheromoneLayingRate):
	distanceMatrix, numberToCityMapping = getDistanceMatrixFromFile()
	visibilityMatrix = [[math.inf] * 27 for _ in range(27)]
	pheromoneMatrix = [[alpha] * 27 for _ in range(27)]
	outputData = []
	outputData.append("-" * 215 + "\n")
	for row in range(27):
		for col in range(27):
			if row != col:
				visibilityMatrix[row][col] = 1 / distanceMatrix[row][col]

	iterationCount = 0
	antTours = []

	while len(antTours) != 1 and iterationCount < numberOfIterations:
		# print(pheromoneMatrix)
		iterationCount += 1
		antTours = []
		for antNumber in range(numberOfAnts):
			startingCity = random.randint(0, 26)
			tour = performTour(distanceMatrix, visibilityMatrix, pheromoneMatrix, startingCity, beta, randomCityChoosingRate)
			tourLength = calculateTourLength(tour, distanceMatrix)
			if not checkIfTourAlreadyExists(antTours, tour, tourLength):
				antTours.append([tour, tourLength, 1])

		minTour, minTourCost, numberOfTimesBestTourOccured = findLeastTour(antTours)
		# print(minTour, minTourCost)
		outputData.append("Iteration " + str(iterationCount) + "\n")
		outputData.append(printLeastTour(minTour, minTourCost, numberToCityMapping))
		performPheromoneEvaporation(pheromoneMatrix, rho)

		shallWeLetOnlyBestAntToLayPheromone = random.random()
		if shallWeLetOnlyBestAntToLayPheromone < bestAntPheromoneLayingRate:
			addPheromoneTrace(minTour, minTourCost, numberOfTimesBestTourOccured, pheromoneMatrix, Q)
		else:
			for tour, tourLength, numberOfTimesThatTourOccured in antTours:
				addPheromoneTrace(tour, tourLength, numberOfTimesThatTourOccured, pheromoneMatrix, Q)

	writeOutputDataToFile(outputData)

if __name__ == "__main__":
	numberOfAnts = 100
	numberOfIterations = 1000
	randomCityChoosingRate = 0.01
	bestAntPheromoneLayingRate = 0.5
	alpha = 10
	beta = 2
	rho = 0.5
	Q = 10000
	implementAntColonyOptimizationAlgorithm(numberOfAnts, numberOfIterations, alpha, beta, rho, Q, randomCityChoosingRate, bestAntPheromoneLayingRate)
