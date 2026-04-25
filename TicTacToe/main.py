import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i] == b[j] == b[k] and b[i] != " ":
            return b[i]
    if " " not in b:
        return "Draw"
    return None

def minimax(b, is_max):
    result = check_winner(b)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def play():
    print("Positions are 0 to 8")
    while True:
        print_board()
        try:
            user = int(input("Enter position (0-8): "))
            if user < 0 or user > 8 or board[user] != " ":
                print("Invalid move, try again.")
                continue
        except:
            print("Enter a valid number.")
            continue

        board[user] = "X"

        if check_winner(board):
            break

        ai_move()

        if check_winner(board):
            break

    print_board()
    print("Result:", check_winner(board))

play()
