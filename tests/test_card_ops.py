import pytest
from src.card_ops import FrenchDeck, replace_ace_by_one, handle_aces_if_needed, execute_turn


def test_french_deck_init():
    """test creation of card deck object"""
    deck = FrenchDeck()
    assert len(deck.cards) == 52
    assert 11 in deck.cards
    assert 2 in deck.cards
    assert 1 not in deck.cards


def test_french_deck_draw():
    """test if drawing reduces deck"""
    deck = FrenchDeck()
    deck.draw_card(10)
    assert len(deck.cards) == 42


def test_french_deck_remove():
    """test reducing deck directly"""
    deck = FrenchDeck()
    deck.remove_drawn_cards([2, 2, 2, 2])
    assert len(deck.cards) == 48
    assert 2 not in deck.cards


def test_replace_ace_by_one_valid():
    """valid request with 1 or more 11 in the sequence, will replace the 1st occurrence of 11 in the sequence by 1"""
    assert replace_ace_by_one([11, 11]) == [1, 11]
    assert replace_ace_by_one([7, 11]) == [7, 1]
    assert replace_ace_by_one([5, 6, 8, 11, 2]) == [5, 6, 8, 1, 2]
    # with more than one 11's in the cards only the first 11 will be replaced
    assert replace_ace_by_one([5, 6, 11, 11, 2]) == [5, 6, 1, 11, 2]


def test_replace_ace_by_one_invalid():
    """invalid request with no 11 in the sequence"""
    assert replace_ace_by_one([6, 10]) == [6, 10]


def test_handle_aces_if_needed():
    """replaces A (11) by 1 if the score exceeds 21 and an 11 is in the cards with updated deck and score,
    otherwise return cards as is"""
    assert handle_aces_if_needed([11, 10], 21) == ([11, 10], 21)
    assert handle_aces_if_needed([10, 10, 10], 30) == ([10, 10, 10], 30)
    assert handle_aces_if_needed([11, 10, 5], 26) == ([1, 10, 5], 16)
    assert handle_aces_if_needed([11, 10, 5, 11], 37) == ([1, 10, 5, 11], 27)
    assert handle_aces_if_needed([11, 11], 22) == ([1, 11], 12)


def test_execute_turn_invalid():
    """test execute_turn raises TypeError when called with missing arguments"""
    with pytest.raises(TypeError):
        execute_turn([5, 6])
