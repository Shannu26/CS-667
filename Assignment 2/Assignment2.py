import itertools
import random

# population = list(itertools.permutations([i for i in range(1, 20)]))
# print(population)
# print()
# print()
# population = random.sample(population, 1000)
# print(population)

population = []

# def generatePopulation():
# 	queue = [[]]
# 	while len(population) != 1000:
# 		sample = queue.pop()
# 		if len(sample) == 19: 
# 			population.append(" ".join([str(num) for num in sample]))
# 		else:
# 			for i in range(1, 20):
# 				if i not in sample: queue.append(sample + [i])

def generatePopulation():
	queue = [[]]
	while len(population) != 1000:
		sample = queue.pop()
		if len(sample) == 19: 
			population.append(" ".join([str(num) for num in sample]))
		else:
			genes = set([i for i in range(1, 20)]) - set(sample)
			while genes:
				num = random.choice(list(genes))
				queue.append(sample + [num])
				genes.remove(num)

generatePopulation()
print(population)	