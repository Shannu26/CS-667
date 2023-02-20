inputs = [
	(False,False,False,False), 
	(False,False,True,False), 
	(False,True,False,False), 
	(False,True,True,True), 
	(True,False,False,False), 
	(True,False,True,True), 
	(True,True,False,True), 
	(True,True,True,True)]

print("----------Generation 9----------")
# Generation 9
# (OR (OR 1 (OR 3 1)) 1)
fitnessScore = 0
for input in inputs:
	equation = ((input[0] or (input[2] or input[0])) or input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR 1 (OR 3 1)) 1) --> ", fitnessScore)

# (OR (AND (OR (AND 3 1) (AND 2 3)) 2) (AND (AND (OR 2 3) 1) (AND 2 (OR 1 1))))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) or (input[1] and input[2])) and input[1]) or (((input[1] or input[2]) and input[0]) and (input[1] and (input[0] or input[0]))))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (OR (AND 3 1) (AND 2 3)) 2) (AND (AND (OR 2 3) 1) (AND 2 (OR 1 1)))) --> ", fitnessScore)

# (OR (AND 2 (AND 3 1)) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and (input[2] and input[0])) or ((input[2] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 2 (AND 3 1)) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND (AND (AND 3 1) 2) 3) (OR (OR 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and input[1]) and input[2]) or ((input[2] or input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) 2) 3) (OR (OR 3 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND 1 2) (OR (OR (OR 2 3) 1) (AND 3 1)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or (((input[1] or input[2]) or input[0]) or (input[2] and input[0])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (OR (OR 2 3) 1) (AND 3 1))) --> ", fitnessScore)

# (OR (AND (AND (AND 2 (OR 1 1)) (AND 2 3)) 2) (OR 3 (OR 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[1] and (input[0] or input[0])) and (input[1] and input[2])) and input[1]) or (input[2] or (input[1] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 2 (OR 1 1)) (AND 2 3)) 2) (OR 3 (OR 2 3))) --> ", fitnessScore)

print("----------Generation 8----------")
# Generation 8
# (OR (AND 1 (OR 3 1)) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and (input[2] or input[0])) or ((input[2] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 (OR 3 1)) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)	

# (OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR 3 (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and (input[1] and input[2])) and input[1]) or (input[2] or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR 3 (AND 2 3))) --> ", fitnessScore)

# (OR (AND 1 2) (OR (AND 3 1) 1)
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or ((input[2] and input[0]) or input[0]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (AND 3 1) 1) --> ", fitnessScore)

# (OR (AND 1 2) (OR (AND (OR 2 3) 1) (AND 2 (OR 1 1))))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or (((input[1] or input[2]) and input[0]) or (input[1] and (input[0] or input[0]))))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (AND (OR 2 3) 1) (AND 2 (OR 1 1)))) --> ", fitnessScore)

# (OR (AND (AND (AND 3 1) 2) 2) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and input[1]) and input[1]) or ((input[2] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) 2) 2) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND 2 3) (OR (AND 3 1) (AND 3 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[2]) or ((input[2] and input[0]) or (input[2] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 2 3) (OR (AND 3 1) (AND 3 3))) --> ", fitnessScore)

print("----------Generation 7----------")
# Generation 7
# (OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR (AND 2 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and (input[1] and input[2])) and input[1]) or ((input[1] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR (AND 2 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND 1 2) (OR (AND 3 1) (AND 2 (OR 1 1))))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or ((input[2] and input[0]) or (input[1] and (input[0] or input[0]))))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (AND 3 1) (AND 2 (OR 1 1)))) --> ", fitnessScore)

# (OR 1 (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or ((input[2] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND (AND (AND 3 1) (AND 2 3)) 2) 2)
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and (input[2] and input[0])) and input[1]) or input[1])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) (AND 2 3)) 2) 2) --> ", fitnessScore)

print("----------Generation 6----------")
# Generation 6
# (OR (AND 1 2) 2)
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or input[1])
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) 2) --> ", fitnessScore)

# (OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((((input[2] and input[0]) and (input[1] and input[2])) and input[1]) or ((input[2] and input[0]) or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND (AND (AND 3 1) (AND 2 3)) 2) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND 1 1) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[0]) or ((input[2] and input[0]) or (input[1] and input[3])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

print("----------Generation 5----------")
# Generation 5
# (OR (AND 2 2) (OR 3 (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[1]) or (input[2] or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 2 2) (OR 3 (AND 2 3))) --> ", fitnessScore)

# (AND 1 1)
fitnessScore = 0
for input in inputs:
	equation = (input[0] and input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND 1 1) --> ", fitnessScore)


print("----------Generation 4----------")
# Generation 4
# (OR (AND 2 2) (OR 1 (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[1]) or (input[0] or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 2 2) (OR 1 (AND 2 3))) --> ", fitnessScore)

# ((OR (AND 3 2) (AND (AND (OR 2 3) 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[2] and input[1]) or (((input[1] or input[2]) and input[0]) and (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 3 2) (AND (AND (OR 2 3) 1) (AND 2 3))) --> ", fitnessScore)

# (OR (AND 1 2) (OR (AND 3 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or ((input[2] and input[0]) or (input[1] and input[3])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR (AND 3 1) (AND 2 3))) --> ", fitnessScore)

# (AND 2 1)
fitnessScore = 0
for input in inputs:
	equation = (input[1] and input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND 2 1) --> ", fitnessScore)

# (OR (AND 3 1) (OR (OR 1 3) (AND (OR 2 3) 1)))
fitnessScore = 0
for input in inputs:
	equation = ((input[2] and input[0]) or ((input[0] or input[2]) or ((input[1] or input[2]) and input[0])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 3 1) (OR (OR 1 3) (AND (OR 2 3) 1))) --> ", fitnessScore)

# (OR 1 (OR (OR (AND (OR 2 3) 1) (AND 2 3)) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or ((((input[1] or input[2]) and input[0]) or (input[1] and input[2])) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR (OR (AND (OR 2 3) 1) (AND 2 3)) (OR 1 3))) --> ", fitnessScore)


print("----------Generation 3----------")
# Generation 3
# (OR (AND 3 1) (AND (AND (OR 2 3) 1) (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[2] and input[0]) or (((input[1] or input[2]) and input[0]) and (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 3 1) (AND (AND (OR 2 3) 1) (AND 2 3))) --> ", fitnessScore)

# (AND (OR 3 1) 1)
fitnessScore = 0
for input in inputs:
	equation = ((input[2] or input[0]) and input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (OR 3 1) 1) --> ", fitnessScore)

# (OR (AND 1 2) (OR 1 (AND 2 3)))
fitnessScore = 0
for input in inputs:
	equation = ((input[0] and input[1]) or (input[0] or (input[1] and input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (AND 1 2) (OR 1 (AND 2 3))) --> ", fitnessScore)

# (OR 1 (OR (AND (OR 1 3) (AND (OR 2 3) 1)) (OR 1 3)))
fitnessScore = 0
for input in inputs:
	equation = (input[0] or (((input[0] or input[2]) and ((input[1] or input[2]) and input[0])) or (input[0] or input[2])))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR 1 (OR (AND (OR 1 3) (AND (OR 2 3) 1)) (OR 1 3))) --> ", fitnessScore)

# (AND (AND 2 1) 1)
fitnessScore = 0
for input in inputs:
	equation = ((input[1] and input[0]) and input[0])
	if not (equation ^ input[3]): fitnessScore += 1
print("(AND (AND 2 1) 1) --> ", fitnessScore)

# (OR (OR (AND 2 2) (AND 2 3)) (AND 2 3))
fitnessScore = 0
for input in inputs:
	equation = (((input[1] and input[1]) or (input[1] and input[2])) or (input[1] and input[2]))
	if not (equation ^ input[3]): fitnessScore += 1
print("(OR (OR (AND 2 2) (AND 2 3)) (AND 2 3)) --> ", fitnessScore)

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