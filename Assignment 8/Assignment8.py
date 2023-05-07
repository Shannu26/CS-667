import heapq

class Board:
	def __init__(self, state):
		self.board = []
		self.board.append(state[:3])
		self.board.append(state[3:6])
		self.board.append(state[6:])
		self.movesFromStartState = []
		
	def __lt__(self, otherBoard):
		return len(self.movesFromStartState) < len(otherBoard.movesFromStartState)

def getGoalBoardPositions(goalBoard):
	goalBoardPositions = {}
	for row in range(3):
		for col in range(3):
			goalBoardPositions[goalBoard[row][col]] = (row, col)
	return goalBoardPositions

def getZeroPiecePosition(board):
		for row in range(3):
			for col in range(3):
				if board[row][col] == 0:
					return (row, col)

def getManhattanDistance(board, goalBoardPositions):
	manhattanDistance = 0
	for row in range(3):
		for col in range(3):
			if board[row][col] == 0: continue
			goalRow, goalCol = goalBoardPositions[board[row][col]]
			manhattanDistance += abs(row - goalRow) + abs(col - goalCol)
	return manhattanDistance

def solveEightPuzzleProblem(startState, goalState):
	startBoard = Board(startState)
	goalBoard = Board(goalState)
	goalBoardPositions = getGoalBoardPositions(goalBoard.board)
	manhattanDistance = getManhattanDistance(startBoard.board, goalBoardPositions)
	openList = [(manhattanDistance, startBoard)]
	startBoard.movesFromStartState = [("Start Board", startBoard.board)]
	closedList = []
	closedList.append(startBoard.board)
	possibleNextMoves = {}
	possibleNextMoves[(-1, 0)] = "Up"
	possibleNextMoves[(1, 0)] = "Down"
	possibleNextMoves[(0, -1)] = "Left"
	possibleNextMoves[(0, 1)] = "Right"

	while openList:
		heuristic, currentBoard = heapq.heappop(openList)
		closedList.append(currentBoard.board)
		if currentBoard.board == goalBoard.board:
			movesFromStartState = currentBoard.movesFromStartState[:]
			movesFromStartState.append(("Reached Goal Board", currentBoard.board))
			return movesFromStartState
		zeroPieceRow, zeroPieceCol = getZeroPiecePosition(currentBoard.board)
		for possibleNextMoveRow, possibleNextMoveCol in possibleNextMoves.keys():
			if 0 <= zeroPieceRow + possibleNextMoveRow <= 2 and 0 <= zeroPieceCol + possibleNextMoveCol <= 2:
				nextZeroPieceRow = zeroPieceRow + possibleNextMoveRow
				nextZeroPieceCol = zeroPieceCol + possibleNextMoveCol
				nextState = currentBoard.board[0] + currentBoard.board[1] + currentBoard.board[2]
				nextBoard = Board(nextState)
				nextBoard.board[nextZeroPieceRow][nextZeroPieceCol], nextBoard.board[zeroPieceRow][zeroPieceCol] = nextBoard.board[zeroPieceRow][zeroPieceCol], nextBoard.board[nextZeroPieceRow][nextZeroPieceCol]
				heuristic = len(currentBoard.movesFromStartState) + getManhattanDistance(nextBoard.board, goalBoardPositions)
				nextBoard.movesFromStartState = currentBoard.movesFromStartState[:]
				moveInfo = "Move Zero " + possibleNextMoves[(possibleNextMoveRow, possibleNextMoveCol)]
				nextBoard.movesFromStartState.append((moveInfo, nextBoard.board))
				if nextBoard.board not in closedList:
					heapq.heappush(openList, (heuristic, nextBoard))

	return []

def checkIfStateIsLegal(state):
	state = state.split(" ")
	if len(state) != 9:
		return []
	for index in range(9):
		if not 0 <= int(state[index]) <= 8:
			return []
		if int(state[index]) in state:
			return []
		state[index] = int(state[index])

	return state

def printMoves(startState, goalState, moves):
	string = ""
	string += "Given,\n"
	string += "\tStart State: "
	for value in startState:
		string += str(value) + " "
	string += "\n\tGoal State: "
	for value in goalState:
		string += str(value) + " "
	string += "\n\n\tStart Board"
	string += "\n\t-------------"
	for index in range(0, 9, 3):
		string += "\n\t| " + str(startState[index]) + " | " + str(startState[index + 1]) + " | " + str(startState[index + 2]) + " |\n"
		string += "\t-------------"
	string += "\n\n\tGoal Board"
	string += "\n\t-------------"
	for index in range(0, 9, 3):
		string += "\n\t| " + str(goalState[index]) + " | " + str(goalState[index + 1]) + " | " + str(goalState[index + 2]) + " |\n"
		string += "\t-------------"
	string += "\n\nSteps To Follow:\n\n"
	for index, move in enumerate(moves):
		moveInfo, board = move
		string += "\t" + moveInfo + "\n"
		string += "\n\t\t|"
		string += "\n\t\tV"
		string += "\n\n"
		string += "\t-------------\n"
		for row in board:
			string += "\t| " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " |\n"
			string += "\t-------------\n"
		if index != len(moves) - 1:
			string += "\n\t\t|"
			string += "\n\t\tV"
			string += "\n\n"

	return string

def writeOutputDataToFile(string):
	with open('EightPuzzleOutput.txt', mode ='w') as outputFile:
		outputFile.writelines(string)

if __name__ == "__main__":
	startState = []
	goalState = []

	while True:
		state = input("Enter the Start State: ")
		startState = checkIfStateIsLegal(state)
		if len(startState) != 0: break
		print("State is Not Legal. Enter a Legal Start State that contains digits from 0-8 only once")

	while True:
		state = input("Enter the Goal State: ")
		goalState = checkIfStateIsLegal(state)
		if len(goalState) != 0: break
		print("State is Not Legal. Enter a Legal End State that contains digits from 0-8 only once")

	movesFromStartState = solveEightPuzzleProblem(startState, goalState)
	string = printMoves(startState, goalState, movesFromStartState)
	writeOutputDataToFile(string)
