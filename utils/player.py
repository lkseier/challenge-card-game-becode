import random
from typing import List
from utils.card import Card
class Player:
    """
    Class representing a player in the card game.

    :param name: The name of the player.
    """
    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 0
        self.cards: List[Card] = []  # Initialize an empty list for cards
        self.turn_count: int = 0
        self.number_of_cards: int = 0  # Initialize the number of cards
        self.history: List[Card] = []
        

    def play(self) -> Card:
        """
        Allows the player to choose a card to play (interactive).
        """
        if not self.cards:
            raise ValueError(f"{self.name} has no cards left to play!")

        print(f"\n{self.name}'s hand:")
        for index, card in enumerate(self.cards):
            print(f"{index + 1}: {card}")

        while True:
            try:
                choice = int(input(f"{self.name}, choose a card to play (1-{len(self.cards)}): "))
                if 1 <= choice <= len(self.cards):
                    selected_card = self.cards.pop(choice - 1)
                    self.history.append(selected_card)
                    self.turn_count += 1
                    print(f"{self.name} played: {selected_card.value} {selected_card.icon}")
                    return selected_card
                else:
                    print("Invalid number. Try again.")
            except ValueError:
                print("Please enter a valid number.")


    def __str__(self) -> str:
        return f"Player {self.name} with {len(self.cards)} cards"

            
    
    
        


 
        
