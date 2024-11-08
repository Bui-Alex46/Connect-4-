from board import Board
from player import Player

def main():
    # Create the board and players
    board = Board()
   
    current_player = board.player1
    while not board.is_full():
        # Get current player's move
        try:
            column = int(input(f"{current_player.name} ({current_player.symbol}), choose a column (0 - {board.columns - 1}): "))
        except ValueError:
            print("Please enter a valid integer for the column.")
            continue

        # Drop the piece for the current player
        if board.drop_piece(column, current_player):
            board.display()
            
             # Check if the current player has won
            if board.check_win(current_player.symbol):
                print(f"{current_player.name} wins!")
                break
            # Print current moves for the player
            print(f"Moves for {current_player.name}: {current_player.moves}")
            
            # Alternate turns
            current_player = board.player2 if current_player == board.player1 else board.player1
        else:
            print("Column is full. Try again.")

    print("Game Over! The board is full.")

if __name__ == "__main__":
    main()
