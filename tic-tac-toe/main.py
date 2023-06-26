# enter the player's position within the game field;
def input_move():
    user_row = int(input("Enter a num between 0 and 2 : "))
    user_column = int(input("Enter a num between 0 and 2 : "))
    user_input = (user_row, user_column)
    return user_input


# check whether the input follows certain conditions;
def input_check():
    user_input = input_move()
    if user_input[0] < 0 or user_input[0] > 2:
        print("Your input does not follow the rules. Try one more time.")
        user_input = input_move()
    if user_input[1] < 0 or user_input[1] > 2:
        print("Your input does not follow the rules. Try one more time.")
        user_input = input_move()
    # if the case is not empty;
    if game_field[user_input[0]][user_input[1]] != "_":
        print("This square is not empty. Try one more time.")
        user_input = input_move()
    return user_input


# print the game field;
def print_field():
    print("-----------")
    for x in range(3):
        print("| ", game_field[x][0], game_field[x][1], game_field[x][2], " |")
    print("-----------")
    return


# check whether one of the players won the game;
def check_winner():
    for x in range(3):
        # row win combination;
        if game_field[x][0] == game_field[x][1] == game_field[x][2] != "_":
            return game_field[x][0]
    for y in range(3):
        # column win combination;
        if game_field[0][y] == game_field[1][y] == game_field[2][y] != "_":
            return game_field[0][y]
    # left diagonal win combo;
    if game_field[0][0] == game_field[1][1] == game_field[2][2] != "_":
        return game_field[0][0]
    # right diagonal win combo;
    if game_field[0][2] == game_field[1][1] == game_field[2][0] != "_":
        return game_field[0][2]
    return None


# congrats message;
def congratulate_player(player):
    print("Congrats player", player)
    print("You won this game!")
    return


# one full game;
def switch_turns():
    # first player is first to make a move;
    current_player = first_player
    winner = None
    while winner is None:
        row, column = input_check()
        game_field[row][column] = current_player
        print_field()
        winner = check_winner()
        # no more empty squares;
        if not any("_" in sublist for sublist in game_field):
            print("Draw")
            return
        current_player = first_player if current_player == second_player else second_player
    congratulate_player(winner)
    return


# MAIN PROGRAM;

first_player = 'X'
second_player = 'O'

game_field = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

user_answer = "y"
while user_answer == "y":
    switch_turns()
    print("Do you want to continue playing?")
    user_answer = input("y/n : ")
    if user_answer == "y":
        game_field = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]
print("Thanks for playing, bye.")
