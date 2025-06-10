from utils.card import Card
class Player:
    def __init__(self, cards, turn_count=0, number_of_cards=0, history=None):
        self.cards = []  # Initialize an empty list for cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history
    def receive_card(self, card):
            """Receives a card and adds it to the player's hand."""
            self.hand.extend([card])
            self.number_of_cards += 1 # Update the number of cards
            # Add the card to the history
    def play(self, card):
        """Plays a card from the player's hand."""
        if card in self.cards:
            self.cards.remove(card)
            self.number_of_cards -= 1 # Update the number of cards
            # Add the card to the history
            self.history.append(card)
        else:
            raise ValueError("Card not in hand.") # Raise an error if the card is not in hand
    def __str__(self):
        """String representation of the player."""
        return f"Player with {self.number_of_cards} cards: {', '.join(str(card) for card in self.cards)}"
    

class Deck:
        def __init__(self):
                self.cards = [] # Initialize an empty list for cards
                self.fill_deck() # Initialize the deck with cards
        def __str__(self): # String representation of the card
            if self.icon == "J":
                return f"{self.color} {self.icon} {self.value} (Jack)"
            elif self.icon == "Q":
                return f"{self.color} {self.icon} {self.value} (Queen)"
            elif self.icon == "K":
                return f"{self.color} {self.icon} {self.value} (King)"
            elif self.icon == "A":
                return f"{self.color} {self.icon} {self.value} (Ace)"
            else:return f"{self.color} {self.icon} {self.value}"
        def card(self):
            """Initializes the deck with cards."""
            self.cards = []
            self.fill_deck()
        def fill_deck(self):
            """Fills the deck with cards of different colors and values."""
            icons = ["♥", "♦", "♣", "♠"]
            values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            for icon in icons:
                 for value in values:
                     self.cards.append(Card(icon, value))
        def shuffle(self):
                """Shuffles the deck of cards."""
                import random
                random.shuffle(self.cards)
        def distribute_cards(self, players, number_of_cards):
            """Distributes cards to players."""
            for _ in range(number_of_cards):
                 for player in players:
                      if self.cards:
                        player.receive_card(self.draw_card())
            else:
                raise ValueError("Not enough cards to distribute.")
            
    
    
        


 
        
