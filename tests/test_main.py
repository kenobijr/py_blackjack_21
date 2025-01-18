import pytest
from project import run_game, player_turn, computer_turn

def test_run_game_blackjack_computer(capsys):
    """
    test run_game() using pytest capsys module which tracks the printed output at terminal
    test for "edgecase" blackjack for computer only in 1st round
    otherwise dependency injection needed do to random elements
    """
    run_game(player_cards=[5,10], computer_cards=[11,10])
    captured = capsys.readouterr()
    expected_output = (
        "    Your cards: [5, 10], current score: 15\n"
        "    Computer's first card: 11\n"
        "  Your final hand: [5, 10], final score: 15\n"
        "  Computer's final hand: [11, 10], final score: 21\n"
        "Computer has Blackjack, you lose. 😱\n"
    )
    assert captured.out == expected_output

def test_run_game_blackjack_player(capsys):
    """test for "edgecase" blackjack for player only in 1st round"""
    run_game(player_cards=[10,11], computer_cards=[5,7])
    captured = capsys.readouterr()
    expected_output = (
        "    Your cards: [10, 11], current score: 21\n"
        "    Computer's first card: 5\n"
        "  Your final hand: [10, 11], final score: 21\n"
        "  Computer's final hand: [5, 7], final score: 12\n"
        "You have Blackjack, you won! 😎\n"
    )
    assert captured.out == expected_output

def test_run_game_blackjack_both(capsys):
    """test for "edgecase" blackjack for player and computer in 1st round"""
    run_game(player_cards=[10,11], computer_cards=[11,10])
    captured = capsys.readouterr()
    expected_output = (
        "    Your cards: [10, 11], current score: 21\n"
        "    Computer's first card: 11\n"
        "  Your final hand: [10, 11], final score: 21\n"
        "  Computer's final hand: [11, 10], final score: 21\n"
        "Computer has Blackjack, you lose. 😱\n"
    )
    assert captured.out == expected_output

def test_player_turn_arguments():
    with pytest.raises(TypeError):
        # expects 4 positional arguments
        player_turn([5,7], 12)
        player_turn("a", "b", "c")

def test_computer_turn_player_bust():
    """if the player busted (flag True) already computer turn must return the values for cards and score as received"""
    assert computer_turn([10,5], 15, True, [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]) == ([10,5], 15)
    assert computer_turn([2,11], 13, True, [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11]) == ([2,11], 13)

def test_computer_turn_over_min_score():
    """if computer score over min_score of 17, computer turn must return the values for cards and score as received (no matter if player bust)"""
    assert computer_turn([10,10], 20, False, [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]) == ([10,10], 20)
    assert computer_turn([9,8], 17, True, [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]) == ([9,8], 17)


