board = [str(i + 1) for i in range(9)]
turn = "X"
def print_board():
    print("|---|---|---|")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|-----------|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|-----------|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("|---|---|---|")
def check_winner():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(space in ['X', 'O'] for space in board):
        return "draw"

    return None
def main():
    global turn
    print("Welcome to  johnny's 3x3 Tic Tac Toe!")
    print_board()
    print("X will play first. Enter a slot number (1-9) to place your mark:")

    winner = None
    while winner is None:
        try:
            move = int(input(f"{turn}'s turn: ")) - 1
            if move < 0 or move > 9:
                print("Invalid input; enter a number from 1 to 9.")
                continue
            if board[move] in ['X', 'O']:
                print("Slot already taken; try another.")
                continue
            board[move] = turn
            print_board()

            winner = check_winner()
            turn = "O" if turn == "X" else "X"

        except ValueError:
            print("Invalid input; please enter a number.")
        if winner == "draw":
        	print("It's a draw! Thanks for playing.")
        else:
        	print(f"Congratulations! {winner} has won!")


main()


