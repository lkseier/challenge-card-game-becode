#Creating a card class with color, icon, and value attributes
class Symbol:
        def __init__(self, color, icon):
            self.color = color
            self.icon = icon
class Card(Symbol): # Card class inherits from Symbol
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.color = color
        self.icon = icon
        """Initializes a card with color, icon, and value."""
        self.value = value
