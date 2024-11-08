# board.py
from player import Player
class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]
        self.player1 = Player("P1", "X")
        self.player2 = Player("P2", "O")



    def display(self):
        # Display the board with borders and separators
        print("  " + "----" * self.columns + "-")
        for row in self.grid:
            print(" | " + " | ".join(row) + " | ")
            print("  " + "----" * self.columns + "-")

# ---------------------------------------------------------------------------
# FUNCTION PLACES THE SYMBOL INTO A DESIGNATED SPOT IN THE BOARD
    def drop_piece(self, column, player):
        # Check if the column is within valid range
        if column < 0 or column >= self.columns:
            print("Invalid column.")
            return False

        # Find the next available row in the chosen column
        for row_index in range(self.rows - 1, -1, -1):
            if self.grid[row_index][column] == " ":
                self.grid[row_index][column] = player.symbol

                # Store the move in the player's move list
                player.add_move(row_index, column)
                return True

        # If no empty cell is found, the column is full
        print("Column is full.")
        return False
    


# Check if board is full 
    def is_full(self):
        # Check if the board is full (no empty spaces left)
        return all(cell != " " for row in self.grid for cell in row)
    
    # Retrieve all moves for a specific symbol
    def get_moves(self,player):
        return player.moves


    def check_win(self, symbol):
        # Check horizontal, vertical, and diagonal win conditions
        for row in range(self.rows):
            for col in range(self.columns):
                if (self.check_direction(row, col, 0, 1, symbol) or  # Horizontal
                    self.check_direction(row, col, 1, 0, symbol) or  # Vertical
                    self.check_direction(row, col, 1, 1, symbol) or  # Diagonal down-right
                    self.check_direction(row, col, 1, -1, symbol)):  # Diagonal up-right
                    return True
        return False

    def check_direction(self, row, col, row_step, col_step, symbol):
        # Check 4 consecutive pieces in a specific direction
        for i in range(4):
            r = row + i * row_step
            c = col + i * col_step
            # Ensure we're within bounds and the symbol matches
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns or self.grid[r][c] != symbol:
                return False
        return True
