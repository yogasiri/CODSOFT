print(" ==========================================")
print( "TIC TAC TOE GAME" )
print("==========================================")

import math

# Create empty board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check if board full
def is_full():
    return " " not in board

# Minimax
def minimax(is_maximizing):
    if check_winner(ai):
        return 1
    if check_winner(player):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = ai

# ================= GAME START =================

print("🎮 TIC TAC TOE - Play Against AI")
print("Board positions are numbered 1 to 9 like this:\n")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9\n")

# Player chooses symbol
choice = input("Choose X or O: ").upper()

while choice not in ["X", "O"]:
    choice = input("Invalid choice. Choose X or O: ").upper()

player = choice
ai = "O" if player == "X" else "X"

print(f"\nYou are {player}")
print(f"AI is {ai}")

# If AI is X, AI goes first
if ai == "X":
    ai_move()

# Game Loop
while True:

    print_board()

    # Player move
    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = player

    if check_winner(player):
        print_board()
        print("🎉 You win!")
        break

    if is_full():
        print_board()
        print("It's a draw!")
        break

    # AI move
    ai_move()

    if check_winner(ai):
        print_board()
        print("🤖 AI wins!")
        break

    if is_full():
        print_board()
        print("It's a draw!")
        break
