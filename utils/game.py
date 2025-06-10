from utils.player import Player
from utils.player import Deck

class Board:
    def __init__(self, players, turn_count=0, active_cards=None, history_cards=None):
        """Initializes the game board with players and game state."""
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards
        board = Board([player("player 1"), player("player 2"), player("player 3"), player("player 4")])
        self.players = [Player(player) for player in players]
    def start_game(self):
        """Starts the game by initializing the board and players."""
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        for player in self.players:
            player.cards = []
            player.turn_count = 0
            player.number_of_cards = 0
            player.history = []
    def next_turn(self):
        """Advances to the next player's turn."""
        self.turn_count += 1
        current_player = self.players[self.turn_count % len(self.players)]
        current_player.turn_count += 1
        return current_player
    def play_card(self, player, card):
        """Allows a player to play a card."""
        if card in player.cards:
            player.play(card)
            self.active_cards.append(card)
            self.history_cards.append(card)
        else:
            raise ValueError("Card not in player's hand.")

