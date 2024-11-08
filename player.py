# player.py
class Player:
    def __init__(self, name, symbol):
        self.name = name      # Player's name
        self.symbol = symbol  # Player's symbol (e.g., "X" or "O")
        self.moves = []

    def get_symbol(self):
        return self.symbol
    
    def add_move(self, row, column):
        self.moves.append((row,column))
    
