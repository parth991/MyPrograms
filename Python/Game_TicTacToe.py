
# Tic-Tac-Toe Python Program
#
# Copyright @ Parth Shah

# Tic TacToe board
current_ticTacToe = {"1":'1', "2": '2', "3": '3', "4": '4', "5": '5', "6": '6', "7": '7', "8": '8', "9": '9'}

# It can take two symbols 'X' and 'O'
userSymbol = {"1": ' ', "2": ' '}

# Dictionary to save Player's name
username = {"1":'Player1', "2": 'Player2'}

whoseTurn = 1
isResultKnown = False

# Draw Tic-Tac-Toe board
def drawBoard():
	print('\n\n')
	print('\t -------------')
	print(f'\t | {current_ticTacToe["7"]} | {current_ticTacToe["8"]} | {current_ticTacToe["9"]} |')
	print('\t -------------')
	print(f'\t | {current_ticTacToe["4"]} | {current_ticTacToe["5"]} | {current_ticTacToe["6"]} |')
	print('\t -------------')
	print(f'\t | {current_ticTacToe["1"]} | {current_ticTacToe["2"]} | {current_ticTacToe["3"]} |')
	print('\t -------------')

# Help function prints instruction
def help():
	print('Instructions')
	print('1. Enter Player1 and Player2 name when requested')
	print("2. Player1 and Player2 select respective symbol 'X' or 'O'")
	print("3. Select the Cell number to put the symbol")

# check for winner
def checkWinner():
	global isResultKnown
	if ((current_ticTacToe["7"] == 'X' and current_ticTacToe["8"] == 'X' and current_ticTacToe["9"] == 'X') or
		(current_ticTacToe["4"] == 'X' and current_ticTacToe["5"] == 'X' and current_ticTacToe["6"] == 'X') or
		(current_ticTacToe["1"] == 'X' and current_ticTacToe["2"] == 'X' and current_ticTacToe["3"] == 'X') or
		(current_ticTacToe["1"] == 'X' and current_ticTacToe["4"] == 'X' and current_ticTacToe["7"] == 'X') or
		(current_ticTacToe["2"] == 'X' and current_ticTacToe["5"] == 'X' and current_ticTacToe["8"] == 'X') or
		(current_ticTacToe["3"] == 'X' and current_ticTacToe["6"] == 'X' and current_ticTacToe["9"] == 'X') or
		(current_ticTacToe["1"] == 'X' and current_ticTacToe["5"] == 'X' and current_ticTacToe["9"] == 'X') or
		(current_ticTacToe["3"] == 'X' and current_ticTacToe["5"] == 'X' and current_ticTacToe["7"] == 'X')):
		# Player with 'X' is a winner

			isResultKnown = True
			for userindex, symbol in userSymbol.items():
				if symbol == 'X':
					print(f'Congratulations!!! {username[userindex]} is a winner')
				else:
					pass
	elif ((current_ticTacToe["7"] == 'O' and current_ticTacToe["8"] == 'O' and current_ticTacToe["9"] == 'O') or
		(current_ticTacToe["4"] == 'O' and current_ticTacToe["5"] == 'O' and current_ticTacToe["6"] == 'O') or
		(current_ticTacToe["1"] == 'O' and current_ticTacToe["2"] == 'O' and current_ticTacToe["3"] == 'O') or
		(current_ticTacToe["1"] == 'O' and current_ticTacToe["4"] == 'O' and current_ticTacToe["7"] == 'O') or
		(current_ticTacToe["2"] == 'O' and current_ticTacToe["5"] == 'O' and current_ticTacToe["8"] == 'O') or
		(current_ticTacToe["3"] == 'O' and current_ticTacToe["6"] == 'O' and current_ticTacToe["9"] == 'O') or
		(current_ticTacToe["1"] == 'O' and current_ticTacToe["5"] == 'O' and current_ticTacToe["9"] == 'O') or
		(current_ticTacToe["3"] == 'O' and current_ticTacToe["5"] == 'O' and current_ticTacToe["7"] == 'O')):
		#Player with 'O' is a winner

			isResultKnown = True
			for userindex, symbol in userSymbol.items():
				if symbol == 'O':
					print(f'Congratulations!!! {username[userindex]} is a winner')
				else:
					pass
	else:	

		# check for Draw
		for key,value in current_ticTacToe.items():
			if current_ticTacToe[key] != 'X' and current_ticTacToe[key] != 'O':
				break
		else:	
			print('Well Played!! It is a Draw')
			isResultKnown = True
	
# Take a symbol from user
def selectSymbol():
	print('\n')
	char = input(f'{username["1"]} select X or O : ')
	if char.upper() != 'X' and char.upper() !='O':
		print('Please select X or O')
		return False

	userSymbol["1"] = char.upper()

	if char.upper() == 'X':
		userSymbol["2"] = 'O'
	else:
		userSymbol["2"] = 'X'

	print('\n')	
	print(f'{username["1"]} has selected {userSymbol["1"]}')
	print(f'{username["2"]} has selected {userSymbol["2"]}')
	print('\n')
	return True

# Take input from player and check for winner
def letsPlay():
	global whoseTurn
	drawBoard()
	print('\n')
	while isResultKnown == False:
		if whoseTurn == 1: 
			char = input(f'{username["1"]} select the cell number : ')
			if current_ticTacToe[char] != 'X' and current_ticTacToe[char] != 'O':
				current_ticTacToe[char] = userSymbol["1"]
				whoseTurn = 2
			else:
				print('This cell is already used, Please select another cell') 
		else:
			char = input(f'{username["2"]} select the cell number : ')
			if current_ticTacToe[char] != 'X' and current_ticTacToe[char] != 'O':
				current_ticTacToe[char] = userSymbol["2"]
				whoseTurn = 1
			else:
				print('This cell is already used, Please select another cell') 	
		drawBoard()
		print('\n')
		checkWinner()		

print("Hello!! Let's play Tic Tac Toe")
# Draw Empty board
drawBoard()
# Print Instructions
help()
print('\n')

# Get Player1 name
username["1"] = input('Hello! Player1 Enter your name : ')

# Get Player2 name
username["2"] = input('Hello! Player2 Enter your name : ')

# Select correct symbole for Player1 and Player2
while selectSymbol() != True: pass

# Start The game
letsPlay()
