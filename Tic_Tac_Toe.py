import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] != ' ' for i in range(len(board))):
        return True

    return False

def check_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return -1 if maximizing_player else 1

    if check_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if maximizing_player:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    empty_cells = get_empty_cells(board)
    best_move = None
    best_eval = float('-inf')

    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'O'
        eval = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = cell

    return best_move

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text='', font=('normal', 20), width=6, height=3,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if check_winner(self.board):
                self.show_winner()
            elif check_board_full(self.board):
                self.show_tie()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.ai_move()

    def ai_move(self):
        row, col = get_best_move(self.board)
        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O')

        if check_winner(self.board):
            self.show_winner()
        elif check_board_full(self.board):
            self.show_tie()
        else:
            self.current_player = 'X'

    def show_winner(self):
        winner = 'X' if self.current_player == 'O' else 'O'
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_board()

    def show_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
