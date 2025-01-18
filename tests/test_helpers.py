import pytest
from src.helpers import print_game_stats, print_game_results, exit_game


def test_print_game_stats(capsys):
    """takes cards as list and score as int for player, 1st card of computer, and prints it to terminal"""
    print_game_stats([6, 11], 17, [7, 7])
    captured = capsys.readouterr()
    expected_output = (
        "    Your cards: [6, 11], current score: 17\n"
        "    Computer's first card: 7\n"
    )
    assert captured.out == expected_output


def test_print_game_results(capsys):
    """takes cards as list, scores as ints, winner message and prints it to terminal"""
    print_game_results([6, 11, 10], 27, [7, 7, 6], 20, "You went over, you lose. 😭")
    captured = capsys.readouterr()
    expected_output = (
        "  Your final hand: [6, 11, 10], final score: 27\n"
        "  Computer's final hand: [7, 7, 6], final score: 20\n"
        "You went over, you lose. 😭\n"
    )
    assert captured.out == expected_output


def test_exit_game():
    with pytest.raises(SystemExit) as exinfo:
        exit_game()
    assert exinfo.value.code == "Bye bye"
