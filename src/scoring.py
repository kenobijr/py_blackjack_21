from typing import List
# Constants
BLACKJACK: int = 21


def calc_score(cards: List[int]) -> int:
    """receives a list of n cards from card_deck in format [5, 10, 3] and returns the score"""
    return sum(cards)


def check_blackjack(player_score: int, computer_score: int) -> bool:
    """
    checks if player or computer or both have blackjack and returns bool;
    applied only in 1st round, in which it's possible to get blackjack;
    in further round 21 counts as "normal" value
    """
    return player_score == BLACKJACK or computer_score == BLACKJACK


def compare_scores_1st_round(computer_score: int) -> str:
    """
    compares the scores for an end state and returns winner message as str
    is only applied at 1st round if at least player or computer (or both) have Blackjack (=21)
    """
    # if computer has blackjack, it wins; also if player has blackjack too
    if computer_score == 21:
        return "Computer has Blackjack, you lose. 😱"
    # if computer had no blackjack, player must have blackjack logically and wins
    else:
        return "You have Blackjack, you won! 😎"


def compare_scores_n_rounds(player_score: int, computer_score: int) -> str:
    """
    compares the scores for an end state for 1 + n rounds and returns winner message as str
    winning rules top to bottom:
    - both went over, computer wins
    - only player went over, computer wins
    - only computer went over, player wins
    - same score: draw
    - player score higher than computer score, player wins
    - computer score higher than player score, computer wins
    """
    if player_score > 21 and computer_score > 21:
        return "You went over, you lose. 😭"
    elif player_score > 21:
        return "You went over, you lose. 😭"
    elif computer_score > 21:
        return "Computer went over, you win. 😁"
    elif player_score == computer_score:
        return "It's a draw. 🙃"
    elif player_score > computer_score:
        return "You win. 😁"
    else:
        return "You lose. 😭"
