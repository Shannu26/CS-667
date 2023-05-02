import heapq

class Board:
	def __init__(self, state):
		self.board = []
		self.board.append(state[:3])
		self.board.append(state[3:6])
		self.board.append(state[6:])
		self.movesFromStartState = []
		self.zeroPiecePosition = self.getZeroPiecePosition(self.board)

	def __lt__(self, otherState):
		return 0

	def getZeroPiecePosition(self, board):
		for row in range(3):
			for col in range(3):
				if board[row][col] == 0:
					return (row, col)

def getGoalBoardPositions(goalBoard):
	goalBoardPositions = {}
	for row in range(3):
		for col in range(3):
			goalBoardPositions[goalBoard[row][col]] = (row, col)
	return goalBoardPositions

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
	startBoard.movesFromStartState = [startBoard.board]
	openList = [(manhattanDistance, startBoard)]
	closedList = []
	closedList.append(startBoard.board)
	possibleNextMoves = {(-1, 0), (1, 0), (0, -1), (0, 1)}

	while openList:
		# print(openList)
		heuristic, currentBoard = heapq.heappop(openList)
		# print(heuristic)
		closedList.append(currentBoard.board)
		if currentBoard.board == goalBoard.board:
			return currentBoard.movesFromStartState
		zeroPieceRow, zeroPieceCol = currentBoard.zeroPiecePosition
		for possibleNextMoveRow, possibleNextMoveCol in possibleNextMoves:
			# print(openList)
			if 0 <= zeroPieceRow + possibleNextMoveRow <= 2 and 0 <= zeroPieceCol + possibleNextMoveCol <= 2:
				nextZeroPieceRow = zeroPieceRow + possibleNextMoveRow
				nextZeroPieceCol = zeroPieceCol + possibleNextMoveCol
				nextState = currentBoard.board[0] + currentBoard.board[1] + currentBoard.board[2]
				nextBoard = Board(nextState)
				nextBoard.board[nextZeroPieceRow][nextZeroPieceCol], nextBoard.board[zeroPieceRow][zeroPieceCol] = nextBoard.board[zeroPieceRow][zeroPieceCol], nextBoard.board[nextZeroPieceRow][nextZeroPieceCol]
				heuristic = len(currentBoard.movesFromStartState) + getManhattanDistance(nextBoard.board, goalBoardPositions)
				nextBoard.movesFromStartState = currentBoard.movesFromStartState[:]
				nextBoard.movesFromStartState.append(nextBoard.board)

				heapq.heappush(openList, (heuristic, nextBoard))
				# print(openList)

	return []

	# print(goalBoard.board in closedList)
	# print(startBoard.board)
	# print(goalBoard.board)

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

	# print(startState)
	# print(goalState)
	movesFromStartState = solveEightPuzzleProblem(startState, goalState)
	print(movesFromStartState)
