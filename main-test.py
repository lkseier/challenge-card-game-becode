from utils.player import Player
from utils.deck import Deck
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
    """
    Main entry point for the card game.
    """
    # Create players
    players = [Player("Alice"), Player("Bob")]

    # Create board with players and start the game
    board = Board(players=players)
    board.start_game()

if __name__ == "__main__":
    main()

from utils.card import Card

# Testing a card manually. #card.py
test_card = Card("A", "red", "♥")
print("Single test card:", test_card)

# Testing deck creation and printing
from utils.deck import Deck

# Test deck
deck = Deck()
deck.fill_deck()
print(deck)  # Should print: Deck with 52 cards

# Optional: print first few cards
print("First 5 cards in deck:")
for card in deck.cards[:5]:
    print(card)

# Testing player creation and card playing
from utils.player import Player

# Create players
p1 = Player("Alice")
p2 = Player("Bob")
players = [p1, p2]

# Distribute cards from deck
deck.distribute(players)

print(p1)  # Should show Player(name=Alice, cards=26)
print(p2)  # Should show Player(name=Bob, cards=26)

# Test playing one card
played_card = p1.play()
print(f"{p1.name} played: {played_card}")

