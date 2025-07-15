from typing import List, Dict
from utils.player import Player
from utils.deck import Deck
from utils.card import Card

# Card ranking for comparison
CARD_RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


class Board:
    """
    Class representing the game board.

    Attributes:
        players: List of Player objects.
        turn_count: The current turn number.
        active_cards: Dictionary mapping player names to the last card played.
        history_cards: List of all cards played except active ones.
    """

    def __init__(self, players: List[Player]) -> None:
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: List[tuple[Player, Card]] = []
        self.history_cards: List[Card] = []

    def start_game(self) -> None:
        """
        Start the card game: fill deck, distribute cards, and play turns until no cards left.
        """
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        print("\n🎲 Game Start!\n")

        # Initialize score for each player
        for player in self.players:
            player.score = 0

        # ✅ Game loop - correctly indented inside method
        while all(player.cards for player in self.players):
            self.turn_count += 1
            print(f"\n--- Turn {self.turn_count} ---")

            self.active_cards = []

            for player in self.players:
                card_played = player.play()
                self.active_cards.append((player, card_played))

            # Determine winner of the round
            round_winner = max(self.active_cards, key=lambda pc: CARD_RANKS[pc[1].value])
            winner_player, winning_card = round_winner
            winner_player.score += 1

            # Round summary
            print("\n🃏 Round Summary:")
            for player, card in self.active_cards:
                print(f"{player.name} played: {card}")

            print(f"\n🏆 {winner_player.name} wins Turn {self.turn_count} with {winning_card}")

            # Save to history
            self.history_cards.extend(card for _, card in self.active_cards)

        # Game over
        print("\n🎉 Game Over!")
        print("\n📊 Final Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score} point(s)")

        top_score = max(p.score for p in self.players)
        winners = [p.name for p in self.players if p.score == top_score]

        if len(winners) == 1:
            print(f"\n🏅 Winner: {winners[0]}!")
        else:
            print(f"\n🤝 It's a tie between: {', '.join(winners)}")
