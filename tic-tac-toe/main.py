from art import logo

print(logo)

board = [0, 1, 2, 
         3, 4, 5, 
         6, 7, 8]

game_is_on = True
rounds = 0

while game_is_on:
    print(f"{board[0]} | {board[1]} | {board[2]}\n"
            "---------\n"
            f"{board[3]} | {board[4]} | {board[5]}\n"
            "---------\n"
            f"{board[6]} | {board[7]} | {board[8]}\n")

    location = int(input("Enter location: "))
    answer = input("Enter X or O: ")

    if location in board:
        board[location] = answer

    # First Row Horizontal
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Second Row Horizontal
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Third Row Horizontal
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("\nX won!\n")
        game_is_on = False



    # First Column Vertical
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Second Column Vertical
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Third Column Vertical
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("\nO won!\n")
        game_is_on = False

    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Top Left, Bottom Right Diagonal
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("\nX won!\n")
        game_is_on = False

    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("\nX won!\n")
        game_is_on = False

    # Top Right, Bottom Left Diagonal
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("\nX won!\n")
        game_is_on = False

    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("\nX won!\n")
        game_is_on = False

    rounds + 1

    if round == 9:
        print("DRAW, NO WINNER THIS TIME! TRY AGAIN")

print(f"{board[0]} | {board[1]} | {board[2]}\n"
        "---------\n"
        f"{board[3]} | {board[4]} | {board[5]}\n"
        "---------\n"
        f"{board[6]} | {board[7]} | {board[8]}\n")