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
    
    def evaluate_board(self): # Function to evaluate the board
        if self.check_win("O"): # Check if AI wins
            return 100
        elif self.check_win("X"):  # Check if player wins
            return -100
        else:
            return 0

    def get_valid_columns(self): # Function to get valid columns
        valid_columns = []
        for col in range(self.columns):
            if self.grid[0][col] == " ":
                valid_columns.append(col)
        return valid_columns

    def minimax(self, depth, is_maximizing): # Function to implement minimax algorithm
        score = self.evaluate_board()

        if abs(score) == 100 or self.is_full() or depth == 0:
            return score

        if is_maximizing:
            best_score = float("-inf")
            for col in self.get_valid_columns():
                self.drop_piece(col, self.player2)
                best_score = max(best_score, self.minimax(depth - 1, False))
                self.undo_move(col)
            return best_score
        else:
            best_score = float("inf")
            for col in self.get_valid_columns():
                self.drop_piece(col, self.player1)
                best_score = min(best_score, self.minimax(depth - 1, True))
                self.undo_move(col)
            return best_score

    def undo_move(self, column):
        for row in range(self.rows):
            if self.grid[row][column] != " ":
                self.grid[row][column] = " "
                break
