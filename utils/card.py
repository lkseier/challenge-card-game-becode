from typing import List 

#Creating a card class with color, icon, and value attributes
class Symbol:
         """
    Class representing the symbol of a card, with a color and icon.

    :param color: A string representing the color of the symbol (e.g., "red", "black").
    :param icon: A single character representing the symbol icon (one of [♥, ♦, ♣, ♠]).
    """
         def __init__(self, color: str, icon: str):
            self.color = color
            self.icon = icon
         def __str__(self) -> str:  # Returns a string representation of the symbol.
              return f"{self.color} {self.icon}"

class Card(Symbol):
    """
    Class representing a playing card that inherits from Symbol and adds a value.

    :param color: The color of the symbol.
    :param icon: The symbol icon.
    :param value: The value of the card (one of ['A', '2', ..., '10', 'J', 'Q', 'K']).
    """
    def __init__(self, color: str, icon: str, value: str) -> None:
        super().__init__(color, icon)
        self.value = value
    def __str__(self) -> str:
        """Returns a string representation of the card."""
        return f"{self.icon} {self.value}"

CARD_RANKS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
def compare_cards(card1: Card, card2: Card) -> int:
    """
    Compare two cards based on their values.

    :param card1: The first card to compare.
    :param card2: The second card to compare.
    :return: 1 if card1 is greater, -1 if card2 is greater, 0 if they are equal.
    """
    rank1 = CARD_RANKS[card1.value]
    rank2 = CARD_RANKS[card2.value]
    
    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        return 0
    