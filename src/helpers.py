import os
import sys

logo = r"""
    ____  __    ___   ________ __    _____   ________ __
   / __ )/ /   /   | / ____/ //_/   / /   | / ____/ //_/
  / __  / /   / /| |/ /   / ,< __  / / /| |/ /   / ,<
 / /_/ / /___/ ___ / /___/ /| / /_/ / ___ / /___/ /| |
/_____/_____/_/__|_\____/_/ |_\____/_/ _|_\____/_/ |_|
          / __ \ \/ /            |__ \<  /
         / /_/ /\  / ______________/ // /
        / ____/ / / /_____/_____/ __// /
       /_/     /_/             /____/_/
"""


def init_ui():
    """clears the terminal and prints game logo"""
    clear_screen()
    print(logo)


def clear_screen():
    """clears the screen; cls for windows, clear for macOS and linux"""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


def exit_game():
    """clears the screen and exits the application"""
    clear_screen()
    sys.exit("Bye bye")


def print_game_stats(player_cards, player_score, computer_cards):
    """takes cards as list [5, 10] and score as int for player, 1st card of computer, and prints it to terminal"""
    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Computer's first card: {computer_cards[0]}")


def print_game_results(player_cards, player_score, computer_cards, computer_score, winner):
    """takes cards as list [5, 10], scores as ints, winner message and prints it to terminal"""
    print(f"  Your final hand: {player_cards}, final score: {player_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(winner)
