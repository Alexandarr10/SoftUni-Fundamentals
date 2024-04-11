class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'

    def play(self):
        while not self.game_over():
            self.print_board()
            row, col = self.get_move()
            self.make_move(row, col)
            self.switch_player()

        if self.winner() == 'T':
            print("It's a tie!")
        else:
            print(f"{self.winner()} wins!")

    def game_over(self):
        return self.winner() != None or self.full_board()

    def winner(self):
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return None

    def full_board(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def make_move(self, row, col):
        self.board[row][col] = self.player

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter col (0, 1, 2): "))
                if self.valid_move(row, col):
                    return (row, col)
                else:
                    print("Invalid move, please try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
