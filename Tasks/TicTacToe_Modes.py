# IMPLEMENTED TWO MODES: Player vs Player and Player vs Computer (Easy)
import random


# Display the game board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")


# Check whether a player has won
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in win_conditions
    )


# Check whether the game is a draw
def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)


# Take input from a human player
def player_move(board, player):

    while True:
        mark = input(f"Player {player}, enter position (1-9): ")

        if not mark.isdigit():
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        mark = int(mark) - 1

        if mark < 0 or mark > 8:
            print("Invalid position. Choose between 1 and 9.")
            continue

        if board[mark] in ['X', 'O']:
            print("Position already taken. Try again.")
            continue

        board[mark] = player
        break


# Get all available positions
def get_available_moves(board):
    return [
        i for i in range(9)
        if board[i] not in ['X', 'O']
    ]


# Easy computer: Select a random position
def easy_computer_move(board):

    available_moves = get_available_moves(board)

    position = random.choice(available_moves)

    board[position] = 'O'

    print(f"Computer selected position {position + 1}")


# Main game logic
def play_game(mode):

    board = [i + 1 for i in range(9)]

    player = 'X'
    count = 0

    while True:

        print_board(board)

        # Player vs Player
        if mode == '1':
            player_move(board, player)

        # Player vs Computer (Easy)
        elif mode == '2':

            if player == 'X':
                player_move(board, 'X')

            else:
                easy_computer_move(board)

        count += 1

        # Check winner
        if check_winner(board, player):

            print_board(board)

            if player == 'O' and mode == '2':
                print("Computer wins!")

            else:
                print(f"Congratulations! Player {player} wins!")

            break

        # Check draw
        if count == 9:

            print_board(board)
            print("It's a draw!")
            break

        # Switch turns
        player = 'O' if player == 'X' else 'X'


# Main menu
def main():

    print("\n===== TIC TAC TOE =====")
    print("1. Player vs Player")
    print("2. Player vs Computer (Easy)")

    while True:

        mode = input("\nChoose your game mode (1-2): ")

        if mode in ['1', '2']:
            break

        print("Invalid choice! Please select 1 or 2.")

    play_game(mode)


main()
