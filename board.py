# board.py
class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]

    def display(self):
        # Display the board with borders and separators
        print("  " + "----" * self.columns + "-")
        for row in self.grid:
            print(" | " + " | ".join(row) + " | ")
            print("  " + "----" * self.columns + "-")

    def drop_piece(self, column, symbol):
        # Drop the player's symbol into the selected column
        for row in reversed(self.grid):
            if row[column] == " ":
                row[column] = symbol
                return True
        return False  # Column is full

    def is_full(self):
        # Check if the board is full (no empty spaces left)
        return all(cell != " " for row in self.grid for cell in row)


