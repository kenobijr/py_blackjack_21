import random
from src.scoring import calc_score

# Constants
BLACKJACK = 21

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

class French_deck:
    """class for set of 52 french cards, returns n random cards from set and reduces them drawn cards from set"""
	# init deck with 52 french cards
    def __init__(self):
        self.cards = sorted([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4)
	# draw n random cards, remove them from set and return them
    def draw_card(self, n):
        drawn_cards = [random.choice(self.cards) for _ in range(n)]
        self.remove_drawn_cards(drawn_cards)
        return drawn_cards
	# remove n cards from a list from the set; only called from inside draw_card method
    def remove_drawn_cards(self, drawn_cards):
        for card in drawn_cards:
            self.cards.remove(card)

def replace_ace_by_one(cards):
	"""receives n cards as list [11, 11]; replaces the first 11 with 1 and returns updated card list"""
	#get index of first ace in deck
	pos_first_ace = cards.index(11)
	#replace the ace at that position by 1
	cards[pos_first_ace] = 1
	return cards

def handle_aces_if_needed(cards, score):
    """replaces ace (11) with 1 if the score exceeds 21 and there's a 11 in cards with updated deck and score, otherwise return cards as is"""
    if score > BLACKJACK and 11 in cards:
        cards = replace_ace_by_one(cards)
        score = calc_score(cards)
    return cards, score

def execute_turn(cards, deck):
    """receives cards, adds further card and updates score; if over 21, replace A, update cards and score; return cards and score"""
    cards += deck.draw_card(1)
    score = calc_score(cards)
    # check if score > 21 with the added card and A in cards; if yes, replace A by 1
    cards, score = handle_aces_if_needed(cards, score)
    return cards, score
