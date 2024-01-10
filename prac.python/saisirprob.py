#Code to play tic tac toe   game 

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # it checks rows n colums and diagnols to win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("------------------- Welcome to Tic Tac Toe! -------------------\n")
    print_board(board)

    def play_tic_tac_toe():
     board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    # print("Welcome to Tic Tac Toe!")
    
    while True:
        

        # Player input
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player

            # Check for a winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already occupied. Try again.")
        print_board(board)

if __name__ == "__main__":
    play_tic_tac_toe()