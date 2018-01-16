def done_or_not(board): #board[i][j]
	valid = [i for i in range(1,10)] # List of valid numbers(0-9)

	# Check if numbers in the board are valid
	for i in range(0,9):
		for j in range(0,9):
			if board[i][j] not in valid:
				return "Try again!"

	# Check rows			
	for i in range(0,9):
		seen = set()
		for x in board[i]:
			if x not in seen:
				seen.add(x)
			else:
				return "Try again!"

	# Check columns
	for i in range(0,9):
		seen = set()
		for j in range(0,9):
			if board[j][i] not in seen:
				seen.add(board[j][i])
			else:
				return "Try again!"

	# Check all 3x3 subregions
	for i in range(1,9,3):	
		for j in range(1,9,3):
			seen = set()
			for x in range(i-1,i+2):
				for y in range(j-1,j+2):
					if board[x][y] not in seen:
						seen.add(board[x][y])
						print(seen)
					else:
						return "Try again!"
					print(board[x][y])
	return "Finished!"