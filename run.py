"""
- runner script to start the blackjack app;
- imports the main function from the blackjack.main module and executes it
- by using this script, the game can be started from the project root directory, ensuring a
consistent execution environment
- usage:
    run the script directly from the command line:
    python3 run.py
"""

# import the main function from the blackjack application
from src.main import main

# if this script is run directly, execute the main function
if __name__ == "__main__":
    main()
