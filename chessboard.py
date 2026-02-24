#chess 8*8 matrix the white spaces are 0 and the black spaces are 1
w = '0'
b = '1'
chess_board = [ [w, b, w, b, w, b, w, b],
                [b, w, b, w, b, w, b, w],
                [w, b, w, b, w, b, w, b],
                [b, w, b, w, b, w, b, w],
                [w, b, w, b, w, b, w, b],
                [b, w, b, w, b, w, b, w],
                [w, b, w, b, w, b, w, b],
                [b, w, b, w, b, w, b, w],
                 ]
#function to print the chess board
def print_chess_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
#call the function to print the chess board
print_chess_board(chess_board)
