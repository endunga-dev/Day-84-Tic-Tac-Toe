import time
import random # FOR AI LATER!
from art import logo # Get the logo from art.py
board = ["" for i in range(9)]

turns = 1

# Make board / Generate board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Add letter to board
def add_letter(location, ltr):
    # The positions and board are in same order,
    # so just get the pos of that position in list and find it on board
    pos_index = positions.index(location)
    if board[pos_index] == "":
        board[pos_index] += ltr
        return True
    else:
        print("You cannot place a letter there, the spot isn't empty!")
        return False

# Decide who X and O is based on the number of turns (X is ALWAYS first, turns starts off as 1)
def letter_checker():
    if turns % 2 == 0:
        print("O's turn.")
        return 'O'
    else:
        print("X's turn.")
        return 'X'

# Check if someone won, or if it was a draw
def win_draw_lose(ltr, turn_cnt, rows):
    target_cnt = 3
    for row in rows: # loop through the winning rows
        if row.count(ltr) == target_cnt: # If there are 3 letters in any of those rows...
            return True # We have a winner!
    if turn_cnt >= 10: # If there's ten turns and the above isn't true, we have a draw
        return None
    else: # If none of the above are true, the game is still going
        return False

# Make the AI move 😳
def ai_move():
    available_pos = [] # For every index and position in positions,
    # if the board at that index (position) is blank, add it to available positions list
    for index, pos in enumerate(positions):
        if board[index] == '':
            available_pos.append(pos)
    if available_pos: # If there is an available position, make a random choice, and add a letter there
        choice = random.choice(available_pos)
        add_letter(choice, ai_letter)
        return True
    return False

valid_letters = ['X', 'O']
# Start game and logic
print(logo)
print("Welcome! This program is the classic tic-tac-toe game, meant for 2 players (AI too!)\n")
print("NOTE: To play this game, you must specify the position you want your letter placed. Type EXACTLY as shown there.\n\n"
      "Read the following to know the positions to place your letter:\n\n"
      "top-left\ntop-center\ntop-right\ncenter-left\ncenter\ncenter-right\nbottom-left\nbottom-center\nbottom-right\n")

# Do you want to play against AI :O
vs_AI = input("Would you like to play against an AI player? Type 'yes' or 'no'.").lower()
if vs_AI == "yes":
    ai_player = True
    ai_letter = input("Please choose a letter for the AI. ('X' or 'O')").upper()
    while ai_letter not in valid_letters: # If they were BSing the input...
        ai_letter = input("Enter X or O buddy. 😐").upper()
    if ai_letter == 'O':
        human_letter = 'X'
    else:
        human_letter = 'O'
else:
    ai_player = False
    ai_letter = None
    human_letter = None

start_game = None
while True:
    ready = input("Are you ready to play, and do you understand how to? Type 'yes' or 'no'."
                  " (or 'stop' to exit.)\n").lower()

    if ready == "yes":
        print_board()
        start_game = True
        break
    elif ready == "no":
        start_game = False
        print("Take your time.")
        time.sleep(5)
    elif ready == "stop":
        break
    else:
        print("Invalid input.")
        continue

positions = ["top-left", "top-center",
                 "top-right", "center-left",
                 "center", "center-right",
                 "bottom-left", "bottom-center",
                 "bottom-right"]

while start_game:
    current_letter = letter_checker()

    if ai_player and current_letter == ai_letter: # If the current letter according to the turns
        # is the Ai's letter, the AI should move
        ai_move()
        turns += 1
        print_board()
        print(f"Turn count: {turns}")
    else:
        where_to = input("Where would you like to place your letter?\n").lower()

        # Make sure where_to is a valid position
        if where_to in positions:
            can_add = add_letter(where_to, current_letter)
            if can_add:
                turns += 1
                print_board()
                print(f"Turn count: {turns}")
            else:
                continue
        else:
            print("Invalid input. Check to ensure that position is a valid one.")
            continue

    # Check for a winner

    # Define the winning rows, and update it dynamically by placing it in while loop
    winning_rows = [
        (board[0], board[1], board[2]),
        (board[3], board[4], board[5]),
        (board[6], board[7], board[8]),
        (board[0], board[3], board[6]),
        (board[1], board[4], board[7]),
        (board[2], board[5], board[8]),
        (board[0], board[4], board[8]),
        (board[2], board[4], board[6]),
    ]
    winner = win_draw_lose(current_letter, turns, winning_rows)
    if winner:
        print(f"The winner is {current_letter}!")
        break
    elif winner is None:
        print("It was a draw!")
        break