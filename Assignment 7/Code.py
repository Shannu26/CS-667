import math

def findEntropy(values):
	entropy = 0

	for value in values:
		entropy += -1 * value * math.log2(value)

	return entropy

def findGain(entropyOfS, values):
	gain = entropyOfS

	for value in values:
		gain -= value[0] * value[1]

	return gain

print(findEntropy([0.6, 0.2, 0.1, 0.1]))
print(findEntropy([2/4, 2/4]))
print(findEntropy([3/4, 1/4]))
print(findEntropy([1/2, 1/2]))
entropyOfS = findEntropy([0.6, 0.2, 0.1, 0.1])
gain = findGain(entropyOfS, [(4/10, findEntropy([2/4, 2/4])), 
							 (4/10, findEntropy([3/4, 1/4])), 
							 (2/10, findEntropy([1/2, 1/2]))])
print(gain)
print()

print(findEntropy([5/5]))
print(findEntropy([2/5,1/5,1/5,1/5]))
gain = findGain(entropyOfS, [(5/10, findEntropy([5/5])),
							 (5/10, findEntropy([2/5,1/5,1/5,1/5]))])
print(gain)
print()

print(findEntropy([4/8, 2/8, 1/8, 1/8]))
print(findEntropy([2/2]))
gain = findGain(entropyOfS, [(8/10, findEntropy([4/8, 2/8, 1/8, 1/8])), 
						   (2/10, findEntropy([2/2]))])
print(gain)
print()

entropyOfS = 1
print(findEntropy([2/4, 2/4]))
print(findEntropy([2/3, 1/3]))
print()

print(findEntropy([5/14, 9/14]))
print(findEntropy([3/5, 2/5]))
print()

print(findEntropy([1/7, 6/7]))
print(findEntropy([3/7, 4/7]))
