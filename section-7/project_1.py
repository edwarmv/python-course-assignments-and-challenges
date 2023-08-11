positions: list[int | str] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = "x"
player2 = "o"


def draw_board():
    return f"""
       |   |   
     {positions[0]} | {positions[1]} | {positions[2]} 
       |   |   
    -----------
       |   |   
     {positions[3]} | {positions[4]} | {positions[5]} 
       |   |   
    -----------
       |   |   
     {positions[6]} | {positions[7]} | {positions[8]} 
       |   |   
    """


def ask_player_to_choose(number_player):
    player_choice = None
    while player_choice == None:
        choice = int(input(f"player {number_player} - choose a position: "))
        if choice in positions:
            player_choice = choice
        else:
            print("choose a valid position")
    return player_choice - 1


def check_board(player_number):
    player = "x" if player_number == 1 else "o"
    # rows
    if positions[0] == player and positions[1] == player and positions[2] == player:
        return True
    if positions[3] == player and positions[4] == player and positions[5] == player:
        return True
    if positions[6] == player and positions[7] == player and positions[8] == player:
        return True
    # columns
    if positions[0] == player and positions[3] == player and positions[6] == player:
        return True
    if positions[1] == player and positions[4] == player and positions[7] == player:
        return True
    if positions[2] == player and positions[5] == player and positions[8] == player:
        return True

    if positions[0] == player and positions[4] == player and positions[8] == player:
        return True
    if positions[2] == player and positions[4] == player and positions[6] == player:
        return True
    return False


def check_tie():
    full_filled = True
    for position in positions:
        if isinstance(position, int):
            full_filled = False
    return full_filled


print(draw_board())
while True:
    player1_choice = ask_player_to_choose(1)
    positions[player1_choice] = "x"
    print(draw_board())
    if check_board(1):
        print("Player 1 wins")
        break
    if check_tie():
        print("Tie")
        break
    player2_choice = ask_player_to_choose(2)
    positions[player2_choice] = "o"
    print(draw_board())
    if check_board(2):
        print("Player 2 wins")
        break
    if check_tie():
        print("Tie")
        break
