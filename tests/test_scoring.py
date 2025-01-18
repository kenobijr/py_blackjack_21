from src.scoring import calc_score, check_blackjack, compare_scores_1st_round, compare_scores_n_rounds

def test_calc_score():
    """returns scores as int for list cardsets"""
    assert calc_score([5, 10]) == 15
    assert calc_score([5, 10, 7]) == 22
    assert calc_score([11, 2, 6, 8, 10]) == 37

def test_check_blackjack():
    """checks if player or computer or both have blackjack in 1st round and returns bool"""
    assert check_blackjack(21, 12) == True
    assert check_blackjack(8, 21) == True
    assert check_blackjack(21, 21) == True
    assert check_blackjack(14, 12) == False

def test_compare_scores_1st_round():
    """returns computer wins str for 21 as computer's score and player wins str for all other scores"""
    assert compare_scores_1st_round(21) == "Computer has Blackjack, you lose. 😱"
    assert compare_scores_1st_round(10) == "You have Blackjack, you won! 😎"

def test_compare_scores_n_rounds():
    """compares scores for an end state in all but the 1st rounds  and returns winner message as str for all cases"""
    assert compare_scores_n_rounds(25, 27) == "You went over, you lose. 😭"
    assert compare_scores_n_rounds(22, 17) == "You went over, you lose. 😭"
    assert compare_scores_n_rounds(21, 22) == "Computer went over, you win. 😁"
    assert compare_scores_n_rounds(15, 15) == "It's a draw. 🙃"
    assert compare_scores_n_rounds(19, 6) == "You win. 😁"
    assert compare_scores_n_rounds(5, 10) == "You lose. 😭"
