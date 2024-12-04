from board import Board
from player import Player

def main():

    # Get user input
    choice = input("Im alone (1) or I have a friend (2)")

    # Validate input
    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Choose option 1 or 2: ")

    # Create the board and players
    board = Board()

    # Perform actions based on the choice
    if choice == "1":
        print("You chose to play alone ): (PvAI)")
        player = board.player1
        aiplayer = board.player2
        playerVai(board, player, aiplayer)
    else:
        print("You chose to play with your friend (PvP)")
        player1 = board.player1
        player2 = board.player2
        playerVplayer(board, player1, player2)


def playerVplayer(board, player1, player2):
    currentplayer = board.player1
    while not board.is_full():
        # Get current player's move
        try:
            column = int(input(f"{currentplayer.name} ({currentplayer.symbol}), choose a column (0 - {board.columns - 1}): "))
        except ValueError:
            print("Please enter a valid integer for the column.")
            continue

        # Drop the piece for the current player
        if board.drop_piece(column, currentplayer):
            board.display()

            #Check if the current player has won
            if board.check_win(currentplayer.symbol):
                print(f"{currentplayer.name} wins!")
                break
            # Print current moves for the player
            print(f"Moves for {currentplayer.name}: {currentplayer.moves}")

            #Alternate turns
            currentplayer = board.player2 if currentplayer == board.player1 else board.player1
        else:
            print("Column is full. Try again.")

    print("Game Over! The board is full.")

def playerVai(board, player, ai): # Function to handle ai move
    currentplayer = player
    while not board.is_full(): # Check if the board is full
        if currentplayer == player:
            try:
                column = int(input(f"{currentplayer.name} ({currentplayer.symbol}), choose a column (0 - {board.columns - 1}): "))
            except ValueError:
                print("Please enter a valid integer for the column.")
                continue

            if board.drop_piece(column, currentplayer):
                board.display()

                if board.check_win(currentplayer.symbol):
                    print(f"{currentplayer.name} wins!")
                    break

                currentplayer = ai
            else:
                print("Column is full. Try again.")
        else:
            print("AI is making its move...")
            best_score = float("-inf")
            best_move = None
            for col in board.get_valid_columns():
                board.drop_piece(col, ai)
                score = board.minimax(depth=4, is_maximizing=False)
                board.undo_move(col)
                if score > best_score:
                    best_score = score
                    best_move = col

            if best_move is not None:
                board.drop_piece(best_move, ai)
                board.display()

                if board.check_win(ai.symbol):
                    print(f"{ai.name} wins!")
                    break

                currentplayer = player



if __name__ == "__main__":
    main()
