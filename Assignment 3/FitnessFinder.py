inputs = [
	(False,False,False,False), 
	(False,False,True,False), 
	(False,True,False,False), 
	(False,True,True,True), 
	(True,False,False,False), 
	(True,False,True,True), 
	(True,True,False,True), 
	(True,True,True,True)]

print("----------Generation 2----------")
# Generation 2
# (OR 1 (OR 2 (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (input[1] or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR 2 (OR 1 3))) --> ", fitnessScore)

# (OR 1 (OR 2 (OR (OR 2 3) 1)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (input[1] or ((input[1] or input[2]) or input[0])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR 2 (OR (OR 2 3) 1))) --> ", fitnessScore)

# (OR 1 (OR (AND (AND 1 3) 1) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (((input[0] and input[2]) and input[0]) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR (AND (AND 1 3) 1) (OR 1 3))) --> ", fitnessScore)

# (OR (AND 1 1) (OR (AND (OR 2 3) 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[0]) or (((input[1] or input[2]) and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 1) (OR (AND (OR 2 3) 1) (AND 2 3))) --> ", fitnessScore)

# (OR (OR (AND 2 2) (AND 2 3)) (OR 2 1))
fitnessScore = 0
for input in inputs:
	equation = (((input[1] and input[1]) or (input[1] and input[2])) or (input[1] or input[0]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR (AND 2 2) (AND 2 3)) (OR 2 1)) --> ", fitnessScore)

# (AND (OR 2 3) 1)
fitnessScore = 0
for input in inputs:
	equation = ((input[1] or input[2]) and input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (OR 2 3) 1) --> ", fitnessScore)


print("----------Generation 1----------")
# Generation 1
# (OR 1 (OR (AND (OR 2 3) 1) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (((input[1] or input[2]) and input[0]) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR (AND (OR 2 3) 1) (OR 1 3))) --> ", fitnessScore)

# (OR 1 (OR 2 1))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (input[1] or input[0]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR 2 1)) --> ", fitnessScore)

# (OR (AND 1 1) (OR (AND (OR 2 3) 1) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[0]) or (((input[1] or input[2]) and input[0]) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 1) (OR (AND (OR 2 3) 1) (OR 1 3))) --> ", fitnessScore)

# (AND (AND 2 3) (OR (AND 1 2) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[2]) and ((input[0] and input[1]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (AND 2 3) (OR (AND 1 2) (AND 2 3))) --> ", fitnessScore)

# (OR (OR 1 3) 3)
fitnessScore = 0
for input in inputs:
	equation = ((input[0] or input[2]) or input[2])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR 1 3) 3) --> ", fitnessScore)

# (OR (OR (OR 1 2) 1) 2)
fitnessScore = 0
for input in inputs:
	equation = (((input[0] or input[1]) or input[0]) or input[1])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR (OR 1 2) 1) 2) --> ", fitnessScore)

print("----------Generation 0----------")
# Generation 0
# (OR (AND 2 1) (OR (AND (OR 2 3) 1) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[0]) or (((input[1] or input[2]) and input[0]) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 2 1) (OR (AND (OR 2 3) 1) (OR 1 3))) --> ", fitnessScore)

# (OR 1 3)
fitnessScore = 0
for input in inputs:
	equation = (input[0] or input[2])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 3) --> ", fitnessScore)

# (AND (AND 2 3) (OR (AND 1 2) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[2]) and ((input[0] and input[1]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (AND 2 3) (OR (AND 1 2) (AND 2 3))) --> ", fitnessScore)

# (OR (OR (OR 1 2) 1) (AND 1 3)) 
fitnessScore = 0
for input in inputs:
	equation = (((input[0] or input[1]) or input[0]) or (input[0] and input[2]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR (OR 1 2) 1) (AND 1 3)) --> ", fitnessScore)

# (AND (AND 1 3) 2)
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[2]) and input[1])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (AND 1 3) 2) --> ", fitnessScore)

# (OR (AND 1 1) (OR 3 2))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[0]) or (input[2] or input[1]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 1) (OR 3 2)) --> ", fitnessScore)