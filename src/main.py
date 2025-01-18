from src.helpers import print_game_stats, print_game_results, exit_game, init_ui
from src.card_ops import handle_aces_if_needed, execute_turn, FrenchDeck
from src.scoring import calc_score, compare_scores_1st_round, compare_scores_n_rounds, check_blackjack
from typing import List, Optional, Tuple

# constants
PLAY_YES: str = "y"
PLAY_NO: str = "n"
BLACKJACK: int = 21
COMPUTER_MIN_SCORE: int = 17


def main() -> None:
    """Ask player to start game; ask to play further games after completing the first one continuously"""
    # clear terminal and print game logo
    init_ui()
    # ask to start game; shut down on no / invalid answers
    start_or_not = input("Do you want to play a game of Blackjack? Type \"y\" or \"n\": ")
    if start_or_not != PLAY_YES:
        exit_game()
    # play the first game
    run_game()
    # loop for further games after first one ended
    while True:
        continue_or_not = input("Do you want to play further? Type \"y\" or \"n\": ")
        if continue_or_not != PLAY_YES:
            exit_game()
        # start next game with reset UI and new deck
        init_ui()
        run_game()


def run_game(
    deck: FrenchDeck = FrenchDeck(),
    player_cards: Optional[list[int]] = None,
    computer_cards: Optional[List[int]] = None
) -> None:
    """
    manages the core gameflow: initial round, player and computer turns, determines the winner
    args:
        deck: creates new card deck object from class.
        player_cards: predefined player cards by testcases or none as default so that random ones are drawn
        computer_cards: predefined computer cards by testcases or none as default so that random ones are drawn
    """
    player_cards = player_cards or deck.draw_card(2)
    computer_cards = computer_cards or deck.draw_card(2)
    player_score, computer_score = calc_score(player_cards), calc_score(computer_cards)
    # check if aces will be replaced by 1 in 1st round (for AA=22); if yes replace one ace by 1 and update score(s)
    player_cards, player_score = handle_aces_if_needed(player_cards, player_score)
    computer_cards, computer_score = handle_aces_if_needed(computer_cards, computer_score)
    # print game stats of 1st round to terminal: player's cards open with score; for computer only first card & no score
    print_game_stats(player_cards, player_score, computer_cards)
    # check if blackjack in first round for at least one player; game ends then
    if check_blackjack(player_score, computer_score):
        # calc winner for blackjack in 1st round
        winner = compare_scores_1st_round(computer_score)
        print_game_results(player_cards, player_score, computer_cards, computer_score, winner)
        return
    # PLAYER'S TURN (no blackjack in 1st round)
    player_cards, player_score, player_bust = player_turn(player_cards, player_score, computer_cards, deck)
    # COMPUTER'S TURN (player did stand or went bust)
    computer_cards, computer_score = computer_turn(computer_cards, computer_score, player_bust, deck)
    # check who won and print end results after player's and computer's turns over
    winner = compare_scores_n_rounds(player_score, computer_score)
    print_game_results(player_cards, player_score, computer_cards, computer_score, winner)


def player_turn(
    player_cards: List[int],
    player_score: int,
    computer_cards: List[int],
    deck: FrenchDeck
) -> Tuple[List[int], int, bool]:
    """
    handles the player's turn; player hits as he sees fit until he stands or busts
    args:
        player_cards (List[int]): The player's current hand as a list of card values
        player_score (int): The player's current score
        computer_cards (List[int]): The computer's cards, used to display game stats
        deck (FrenchDeck): The current deck of cards
    returns:
        Tuple[List[int], int, bool]:
            - updated player_cards after the turn
            - updated player_score after the turn
            - a boolean flag indicating whether the player went bust (true if bust, false otherwise)

    """
    player_bust: bool = False
    while True:
        draw_card = input("Type \"y\" to draw another card or \"n\" to pass: ")
        # break loop and return values if player doesn't hit
        if draw_card != PLAY_YES:
            break
        # draw a card, update score, check if score > 21 & ace in cards; if yes, replace ace by 1, update cards & score
        player_cards, player_score = execute_turn(player_cards, deck)
        print_game_stats(player_cards, player_score, computer_cards)
        # if player went over (=bust), set bust flag for computer turn, break loop and return values
        if player_score > BLACKJACK:
            player_bust = True
            break
    return player_cards, player_score, player_bust


def computer_turn(
    computer_cards: List[int],
    computer_score: int,
    player_bust: bool,
    deck: FrenchDeck
) -> Tuple[List[int], int]:
    """
    handles the computer's turn; computer draws cards only if the player didn't bust,
    and it's under the minimum score of 17; continues drawing until going over the min score of 17  or busting
    args:
        computer_cards (List[int]): the computer's current hand as a list of card values
        computer_score (int): the computer's current score
        player_bust (bool): a flag indicating if the player has busted; if true, the computer does not draw cards
        deck (FrenchDeck): the current deck of cards used to draw additional cards
    returns:
        Tuple[List[int], int]:
            - updated computer_cards after the turn
            - updated computer_score after the turn
    """
    while computer_score < COMPUTER_MIN_SCORE and not player_bust:
        # draw a card, update score, check if score > 21 & ace in cards; if yes, replace ace by 1, update cards & score
        computer_cards, computer_score = execute_turn(computer_cards, deck)
    return computer_cards, computer_score


if __name__ == "__main__":
    main()
