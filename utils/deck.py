print(">>> deck.py loaded")


import random
from typing import List
from utils.card import Card


class Deck:
    SYMBOLS = [
        ("red", "♥"),
        ("red", "♦"),
        ("black", "♠"),
        ("black", "♣")
    ]

    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards: list[Card] = []

    def fill_deck(self) -> None:
        for color, icon in Deck.SYMBOLS:
            for value in Deck.VALUES:
                self.cards.append(Card(value=value, color=color, icon=icon))


    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)

    def distribute(self, players: List['Player']) -> None:
        """
        Distribute cards evenly to players.

        :param players: List of Player objects.
        """
        player_count = len(players)
        for i, card in enumerate(self.cards):
            players[i % player_count].cards.append(card)
            players[i % player_count].number_of_cards += 1
        self.cards.clear()
        # Update the number of cards for each player
        for player in players:
            player.number_of_cards = len(player.cards)

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards"