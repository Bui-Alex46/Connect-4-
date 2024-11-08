# Define board dimensions
ROW = 6
COLUMN = 7

# Create a 6x7 grid for the playable area
board = [[" " for _ in range(COLUMN)] for _ in range(ROW)]

# Function to print the board with borders and internal separators
def print_board(board):
    # Print the top border
    print("  " + "----" * COLUMN + "-")

    for row in board:
        # Print each row with separators
        print(" | " + " | ".join(row) + " | ")
        # Print the row separator after each row
        print("  " + "----" * COLUMN + "-")

# Print the initial board
print_board(board)
