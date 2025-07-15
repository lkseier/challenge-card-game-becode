from utils.player import Player
from utils.game import Board
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main() -> None:
    """
    Starts the card game between multiple players.
    """
    print("🎴 Welcome to the Card Game!\n")
    
    # Ask how many players
    while True:
        try:
            num_players = int(input("How many players (2–4 recommended)? "))
            if num_players < 2:
                print("You need at least 2 players to play.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Collect player names
    players: list[Player] = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        players.append(Player(name))

    # Start the game
    board = Board(players)
    board.start_game()


if __name__ == "__main__":
    main()

