def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]

    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

print("It's Tic Tac Toe!")
print("Player 1 is 'X' and Player 2 is 'O'.")
print("Enter a num (1-9) to place your mark.")

board = [i+1 for i in range(9)]  
player = 'X' 
count = 0 

while True:

    print_board(board)

    mark = input(f"Player {player}, enter your mark: ") 

    if not mark.isdigit():
        print("Invalid input. Please enter a number between 1 and 9 \n")
        continue
    
    mark = int(mark) - 1
    if board[mark] in ['X', 'O']:
        print("Place already taken. Try again \n")
        continue
    if (mark < 0 or mark > 8):
        print("Invalid input. Enter a number between 1 and 9 \n")
        continue

    board[mark] = player
    count += 1

    if check_winner(board, player):
        print_board(board)
        print(f"Congratulations, Player {player} wins!")
        break

    if count == 9:
        print_board(board)
        print("It's a tie!")
        break

    player = 'O' if player == 'X' else 'X'





