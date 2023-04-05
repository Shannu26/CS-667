import math

def getInputFromFile():
	dataset = []
	with open("urbanGB.centr.txt") as dataFile:
		data = dataFile.read()
		data = data.split("\n")
		for coordinates in data:
			coordinates = coordinates.split(",")
			dataset.append((float(coordinates[0]), float(coordinates[1])))

	return dataset

def averageLinkageDistance(cluster1, cluster2):
	distance = 0
	numberOfPairs = 0
	for x1, y1 in cluster1:
		for x2, y2 in cluster2:
			numberOfPairs += 1
			distance += math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

	averageDistance = distance / numberOfPairs
	return averageDistance

def formNewClusters(clusters, index1, index2):
	newClusters = {}
	newClusters[0] = clusters[index1] + clusters[index2]
	newClustersSize = 1
	for index in clusters:
		if index == index1 or index == index2: continue
		newClusters[newClustersSize] = clusters[index]
		newClustersSize += 1

	return newClusters

def printClusterInfo(iteration, cluster1, cluster2, distance):
	string = "\n|\t\t" + str(iteration) + "\t\t|\t\t\t" + str(len(cluster1)) + "\t\t\t|\t\t\t" + str(len(cluster2)) + "\t\t\t|\t\t" + str(distance) + "\t\t|"
	string += "\n"
	string += "-" * 177
	return string

def writeOutputDataToFile(outputData):
	with open('OutputFile.txt', mode ='w') as outputFile:
		outputFile.writelines(outputData)

def hierarchialClustering():
	dataset = getInputFromFile()
	clusters = {}
	for index in range(len(dataset)):
		clusters[index] = [dataset[index]]

	outputData = []
	outputData.append("-" * 177)
	outputData.append("\n|\t\tIteration\t|\tNumber of Items in First Cluster\t|\tNumber of Items in Second Cluster\t|\t\tDistance Between Clusters\t|\n")
	outputData.append("-" * 177)

	iteration = 1
	while len(clusters) != 1:
		minDistance = math.inf
		minClusterPair = [0, 0]
		for index1 in clusters.keys():
			for index2 in clusters.keys():
				if index1 >= index2: continue
				distance = averageLinkageDistance(clusters[index1], clusters[index2])
				if distance < minDistance:
					minDistance = distance
					minClusterPair = [index1, index2]

		string = printClusterInfo(iteration, clusters[minClusterPair[0]], clusters[minClusterPair[1]], minDistance)
		outputData.append(string)
		clusters = formNewClusters(clusters, minClusterPair[0], minClusterPair[1])
		iteration += 1
		
	writeOutputDataToFile(outputData)

if __name__ == "__main__":
	hierarchialClustering()