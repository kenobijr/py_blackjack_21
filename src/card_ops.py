import random
from src.scoring import calc_score
from typing import List, Tuple

# Constants
BLACKJACK: int = 21

"""
A standard Blackjack deck is based on a 52-card deck used in regular card games. Here’s how the cards are structured:
1.	Four Suits:
•	Hearts (♥), Diamonds (♦), Clubs (♣), Spades (♠).
•	The suits are irrelevant in Blackjack; only card values matter.
2.	Card Values:
•	Number cards (2–10): Retain their face value.
•	Face cards (Jack, Queen, King): All count as 10.
•	Ace: Counts as 1 or 11, depending on the player’s hand.
3.	Number of Cards:
•	There are 4 of each rank (one for each suit).
"""


class FrenchDeck:
    """class for set of 52 french cards, returns n random cards from set and reduces them drawn cards from set"""
    def __init__(self):
        """initializes the deck with 52 cards (4 sets of values: 2–11)"""
        self.cards = sorted([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4)

    def draw_card(self, n: int) -> List[int]:
        """draw n random cards (reduced by random sample), remove them from set and return them"""
        if n > len(self.cards):
            raise ValueError("Not enough cards left to draw")
        drawn_cards = random.sample(self.cards, n)
        self.remove_drawn_cards(drawn_cards)
        return drawn_cards

    def remove_drawn_cards(self, drawn_cards: List[int]) -> None:
        """remove n cards from a list from the set; only called from inside draw_card method"""
        for card in drawn_cards:
            self.cards.remove(card)


def replace_ace_by_one(cards: List[int]) -> List[int]:
    """
    replaces the first occurrence of 11 with 1 in the given card list; only called if at least one 11 in cards;
    safeguard: if no 11 is found, returns the cards unchanged
    """
    if 11 in cards:
        cards[cards.index(11)] = 1
    return cards


def handle_aces_if_needed(cards: List[int], score: int) -> Tuple[List[int], int]:
    """replaces ace (11) with 1 if the score exceeds 21 and there's an 11 in cards with updated deck and score,
    otherwise return cards as is"""
    if score > BLACKJACK and 11 in cards:
        cards = replace_ace_by_one(cards)
        score = calc_score(cards)
    return cards, score


def execute_turn(cards: List[int], deck: FrenchDeck) -> Tuple[List[int], int]:
    """receives cards, adds further card and updates score; if over 21, replace A, update cards and score;
    return cards and score"""
    cards += deck.draw_card(1)
    score = calc_score(cards)
    # check if score > 21 with the added card and A in cards; if yes, replace A by 1
    cards, score = handle_aces_if_needed(cards, score)
    return cards, score
