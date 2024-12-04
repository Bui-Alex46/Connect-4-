import tkinter as tk
from tkinter import messagebox
from board import Board


class Connect4GUI:
    def __init__(self):
        self.board = Board()
        self.current_player = self.board.player1  # Start with Player 1
        self.window = tk.Tk()
        self.window.title("Connect 4")
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        # Create the game board as a grid of buttons
        self.buttons = [
            [
                tk.Button(
                    self.window,
                    text=" ",
                    font=("Helvetica", 20),
                    width=4,
                    height=2,
                    command=lambda row=row, col=col: self.make_move(col),
                )
                for col in range(self.board.columns)
            ]
            for row in range(self.board.rows)
        ]

        for row in range(self.board.rows):
            for col in range(self.board.columns):
                self.buttons[row][col].grid(row=row, column=col, padx=2, pady=2)

        # Create a label to display the game status
        self.status_label = tk.Label(self.window, text="", font=("Helvetica", 14))
        self.status_label.grid(row=self.board.rows, column=0, columnspan=self.board.columns)

    def make_move(self, column): # Function to handle player's move and AI's move
       if self.current_player == self.board.player2:  # Prevent player from making a move when it's AI's turn
            self.ai_move()
            return

       if column is None:
         return

       if not self.board.drop_piece(column, self.current_player): # Check if the move is valid
            messagebox.showinfo("Invalid Move", "This column is full. Try another!")
            return

       self.update_board()

     # Check for win or draw
       if self.board.check_win(self.current_player.symbol):
            self.update_status(win=True)
            messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
            self.reset_game()
            return

       if self.board.is_full():
            self.update_status(draw=True)
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return

        # Switch players
       self.current_player = (
       self.board.player2 if self.current_player == self.board.player1 else self.board.player1
       )
       self.update_status()

       if self.current_player == self.board.player2:  # Trigger AI's move
            self.ai_move()
    
    def ai_move(self): # Function to handle AI's move
    
        self.update_status() 
        self.window.update_idletasks()  

        best_score = float("-inf")
        best_column = None

        for column in self.board.get_valid_columns(): # Iterate through all valid columns
            self.board.drop_piece(column, self.board.player2)
            score = self.board.minimax(depth=4, is_maximizing=False)  # Minimax search and adjust depth as needed to test the AI
            self.board.undo_move(column)

            if score > best_score:
                best_score = score
                best_column = column

        if best_column is not None: # Make the best move
            self.board.drop_piece(best_column, self.board.player2)
            self.update_board()

            if self.board.check_win(self.board.player2.symbol):   # Checks for win or draw  
                self.update_status(win=True)
                messagebox.showinfo("Game Over", f"{self.board.player2.name} wins!")
                self.reset_game()
                return

            if self.board.is_full(): # Checks for draw
                self.update_status(draw=True)
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

        self.current_player = self.board.player1 # Switch players
        self.update_status()


    def update_board(self):
        # Refresh the GUI to match the board state
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                self.buttons[row][col].config(text=self.board.grid[row][col])

    def update_status(self, win=False, draw=False):
        if win:
            self.status_label.config(text=f"{self.current_player.name} wins!")
        elif draw:
            self.status_label.config(text="It's a draw!")
        else:
            self.status_label.config(text=f"{self.current_player.name}'s turn ({self.current_player.symbol})")

    def reset_game(self):
        # Reset the board and GUI for a new game
        self.board = Board()
        self.current_player = self.board.player1
        self.update_board()
        self.update_status()

    def run(self):
        # Start the GUI event loop
        self.window.mainloop()


if __name__ == "__main__":
    Connect4GUI().run()