game_on = True
game_list: list[int | str] = [0, 1, 2]


def display_game(game_list: list[int | str]):
    print("Here is the current list: ")
    print(game_list)


def position_choice():
    acceptable_values: list[str] = ["0", "1", "2"]
    choice = "wrong"
    while choice not in acceptable_values:
        choice = input("Pick a position (0,1,2): ")
        if choice not in acceptable_values:
            print("Sorry, invalid choice!")
    return int(choice)


def gameon_choice() -> bool:
    acceptable_values: list[str] = ["y", "n"]
    choice = "wrong"
    while choice not in acceptable_values:
        choice = input("Keep playing? (y or n) ")
        if choice not in acceptable_values:
            print("Sorry, I don't understand, please choose y or n")
    if choice == "y":
        return True
    else:
        return False


def replacement_choice(game_list: list[int | str], position: int):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list


while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()
