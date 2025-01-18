
# Blackjack PY -- 21

#### Video Demo: <https://youtu.be/SeO_JJm4-rs>

#### Description:
This app offers an easy-to-use Blackjack game to be played via the terminal against the computer. Below, the game rules and code architecture are explained in detail.

---

# GAME RULES:

### Goal
Reach a hand value as close to 21 as possible without exceeding it (“busting”).

### Card Deck
- French deck with cards: `[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`.
- Cards are removed from the deck when drawn. A new shuffled deck is created each round.

### Scores
- **Number cards (2–10):** Face value.
- **Face cards (Jack, Queen, King):** 10 points each.
- **Ace:** 1 or 11, whichever benefits the hand most. (1 if hand exceeds 21).

### Blackjack
An Ace + a 10-point card (total 21) in the first round is Blackjack. It beats all hands except another Blackjack.

### Gameplay
1. Both the player and computer are dealt two cards.
2. The player’s cards are face up; one of the computer's cards is hidden.
3. If AA is dealt in the first round, one Ace is counted as 1, making the score 12.
4. If **only one** player has Blackjack in the first round, that player wins. If **both** have Blackjack, the computer wins.
5. If no Blackjack occurs, the player decides whether to “hit” (draw another card) or “stand” (keep their current hand).

---

### Flow of the Player’s Turn:
- Draw a card, replacing Ace with 1 if bust.
  - **If score > 21**: Player busts, game over.
  - **If score ≤ 21**: Player can choose to hit or stand.
  - **Note:** A score of 21 after the first round is not Blackjack.
  - The player can keep drawing even with a score of 21 (though it may be illogical).
  - If the player busts, the computer does not draw further since the player already lost.

### Flow of the Computer’s Turn:
- Computer draws another card if its current score is < 17 and the player hasn’t busted.
  - Replace Ace with 1 if bust.
  - **If bust** or **17 ≤ score ≤ 21**, game ends, and results are evaluated.

---

### End State:
- **Both bust:** Computer wins.
- **One busts:** The other wins.
- **Same score:** Draw.
- **Higher score:** Higher score wins.

---

# CODE ARCHITECTURE:

## Overview
This project is a console-based implementation of **Blackjack**. The goal is to beat the computer by having a hand value closest to 21 without exceeding it. It follows standard rules, handling Aces dynamically and allowing multiple rounds.

### Features:
- Dynamic card drawing and score calculation.
- Clear user interface with game prompts and results.
- Automatic win/loss detection for busts or Blackjack.

---

## File Descriptions

### `project.py`
Main entry point for the game, handling core game flow:
- **`main()`**: Initializes the game UI and manages the game loop.
- **`run_game()`**: Executes the primary game logic, including player and computer turns.
- **`player_turn()`**: Allows the player to draw cards or pass until they stand or bust.
- **`computer_turn()`**: Ensures the computer plays optimally, drawing cards until its score is at least 17.

---

### `card_ops.py`
Manages the card deck and player actions:
- **`French_deck`**: Class that simulates a 52-card deck with draw functionality.
- **`replace_ace_by_one()`**: Adjusts Aces from 11 to 1 if needed.
- **`handle_aces_if_needed()`**: Checks and updates the value of Aces when score exceeds 21.
- **`execute_turn()`**: Adds a card to the hand and updates the score, handling Ace values accordingly.

---

### `scoring.py`
Handles scoring and win condition logic:
- **`calc_score()`**: Calculates the total value of the current hand.
- **`check_blackjack()`**: Determines if either player has Blackjack in the first round.
- **`compare_scores_1st_round()`**: Declares the winner if Blackjack is dealt in the first round.
- **`compare_scores_n_rounds()`**: Compares scores after multiple rounds to declare a winner.

---

### `helpers.py`
Provides utility functions for UI and system interactions:
- **`init_ui()`**: Clears the screen and displays the game logo.
- **`clear_screen()`**: Clears the console screen (supports Windows, macOS, Linux).
- **`exit_game()`**: Exits the game with a goodbye message.
- **`print_game_stats()`**: Displays the player’s and computer’s cards during gameplay.
- **`print_game_results()`**: Displays the final hand, scores, and winner.

---

## Design Choices:

1. **Class-Based Deck Implementation**
   The `French_deck` class ensures no card is drawn twice by managing a dynamic deck that reduces after each draw.

2. **Ace Handling Logic**
   Aces dynamically adjust from 11 to 1 to prevent busts, aligning with real Blackjack rules.

3. **Separation of Concerns**
   The modular structure improves readability and maintainability by dividing the game logic across multiple files.

4. **Continuous Gameplay Loop**
   Allows for continuous rounds until the player opts to quit, enhancing the immersive experience.

---

## Conclusion
This project is a fully functional, text-based Blackjack game that adheres to modular design principles. It offers an engaging and realistic gameplay experience by simulating core Blackjack mechanics, making it both entertaining and educational for players.


>>>>>>> f539667 (initial commit: add blackjack project files)
