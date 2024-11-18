import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from copy import deepcopy

# Define the 10x10 board
BOARD_SIZE = 10

# Define each piece as a list of lists, covering 100 cells in total across all pieces
# These pieces have specific shapes, and they add up to fully cover a 10x10 grid.
pieces = [
    [[1, 1], [1, 1]],  # Piece 1 (2x2 square)
    [[1, 1, 1], [1, 0, 0]],  # Piece 2 (L shape)
    [[1, 1, 1, 1]],  # Piece 3 (4x1 line)
    [[1], [1], [1], [1]],  # Piece 4 (1x4 line)
    [[1, 1, 0], [0, 1, 1]],  # Piece 5 (Z shape)
    [[1, 1, 1], [0, 1, 0]],  # Piece 6 (T shape)
    [[1, 1], [0, 1]],  # Piece 7 (corner shape)
    [[1, 1, 1], [1, 0, 0]]  # Piece 8 (another L shape)
]

# Initialize the board with zeros (0 means unoccupied)
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# Function to check if a piece fits in the board at a given position
def can_place(board, piece, row, col):
    piece_height = len(piece)
    piece_width = len(piece[0])

    if row + piece_height > BOARD_SIZE or col + piece_width > BOARD_SIZE:
        return False

    for r in range(piece_height):
        for c in range(piece_width):
            if piece[r][c] == 1 and board[row + r][col + c] != 0:
                return False
    return True


# Function to place a piece on the board
def place_piece(board, piece, row, col, piece_id):
    piece_height = len(piece)
    piece_width = len(piece[0])
    for r in range(piece_height):
        for c in range(piece_width):
            if piece[r][c] == 1:
                board[row + r][col + c] = piece_id


# Function to remove a piece from the board
def remove_piece(board, piece, row, col):
    piece_height = len(piece)
    piece_width = len(piece[0])
    for r in range(piece_height):
        for c in range(piece_width):
            if piece[r][c] == 1:
                board[row + r][col + c] = 0


# Recursive function to try placing all pieces on the board
def solve(board, pieces, piece_index):
    if piece_index == len(pieces):
        return True

    piece = pieces[piece_index]

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if can_place(board, piece, row, col):
                place_piece(board, piece, row, col, piece_index + 1)

                if solve(board, pieces, piece_index + 1):
                    return True

                remove_piece(board, piece, row, col)

    return False


# Solve the puzzle
if solve(board, pieces, 0):
    print("Solution found! Displaying the board...")
else:
    print("No solution exists.")


# Visualization using matplotlib
def draw_board(board):
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('tab20')  # Using a colormap with many colors
    norm = mcolors.BoundaryNorm(range(len(pieces) + 1), cmap.N)

    ax.imshow(board, cmap=cmap, norm=norm)

    # Add grid and labels
    ax.set_xticks([x - 0.5 for x in range(1, BOARD_SIZE)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, BOARD_SIZE)], minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", size=0)
    ax.tick_params(which="both", left=False, bottom=False, labelleft=False, labelbottom=False)

    # Show the plot
    plt.show()


# Call the draw function to display the board
draw_board(board)
