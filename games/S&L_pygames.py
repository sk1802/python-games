import pygame
import random

pygame.init()

# Set the window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Set the size of each cell
CELL_SIZE = 40

# Set the number of rows and columns
ROWS = WINDOW_WIDTH // CELL_SIZE
COLUMNS = WINDOW_HEIGHT // CELL_SIZE

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.add_snakes()
        self.add_ladders()

    def add_snakes(self):
        # Add some snakes to the board
        self.board[2][2] = -5
        self.board[4][4] = -7
        self.board[5][1] = -9

    def add_ladders(self):
        # Add some ladders to the board
        self.board[1][1] = 4
        self.board[3][3] = 6
        self.board[4][2] = 8

class Player:
    def __init__(self, board):
        self.board = board
        self.x = 0
        self.y = 0
        self.current_position = 0

    def move(self, dice_roll):
        # Calculate the new position
        self.current_position += dice_roll
        self.current_position += self.board.board[self.x][self.y]

        # Update the player's position on the board
        self.x = self.current_position // COLUMNS
        self.y = self.current_position % COLUMNS


board = Board()
player = Player(board)

while True:
    # Roll the dice
    dice_roll = random.randint(1, 6)

    # Move the player
    player.move(dice_roll)

    # Draw the board and player
    window.fill((255, 255, 255))
    for i in range(ROWS):
        for j in range(COLUMNS):
            pygame.draw.rect(window, (0, 0, 0), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
    pygame.draw.rect(window, (255, 0, 0), (player.x * CELL_SIZE, player.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)) 
    pygame.display.update() 
    pygame.time.delay(1000) 
    pygame.display.set_caption("Snake and Ladders")
    pygame.display.flip()