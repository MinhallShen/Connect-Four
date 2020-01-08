import pygame
import math
import sys
import numpy 

# initialize pygame
pygame.init()

# display size
screen = pygame.display.set_mode((800, 600))

# title
pygame.display.set_caption("Connect Four")

# colours 
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

# board
boardImg = pygame.image.load("Connect4Board.png")
boardX = 80
boardY = 100

'''
row1 = [0, 0, 0, 0, 0, 0, 0]
row2 = [0, 0, 0, 0, 0, 0, 0]
row3 = [0, 0, 0, 0, 0, 0, 0]
row4 = [0, 0, 0, 0, 0, 0, 0]
row5 = [0, 0, 0, 0, 0, 0, 0]
row6 = [0, 0, 0, 0, 0, 0, 0]
row7 = [0, 0, 0, 0, 0, 0, 0]
board = [row1, row2, row3, row4, row5, row6, row7]
^^doesn't work because continue_game function will
always return false, have to use numpy. (source: Keith
Galli)
'''

# constants
turn = 0
radius = 36
bottom_left_x = 130
bottom_left_y = 541
x_dist = 90
y_dist = 80

# functions

# must create board using numpy by making a function
def create_board():
  bo = numpy.zeros((6, 7))
  return bo

# where the board goes
def boardPos():
  screen.blit(boardImg, (boardX, boardY))

# put either yellow or red down
def place_piece(board, r, c, colour):
  board[r][c] = colour;

# is the column already full?
def valid_move(board, c):
  if board[5][c] == 0:
    return True

# find where the piece will drop
def next_row(board, c):
  for r in range(6):
    if board[r][c] == 0:
      return r

# check for four in a row
def continue_game(board, colour):
  #check horizontal
  for c in range(4):
    for r in range(6):
      if board[r][c] == colour and board[r][c+1] == colour and board[r][c+2] == colour and board[r][c+3] == colour:
        return False
  #check vertical
  for c in range(7):
    for r in range(3):
      if board[r][c] == colour and board[r+1][c] == colour and board[r+2][c] == colour and board[r+3][c] == colour:
        return False
  #check /
  for c in range(4):
    for r in range(3):
      if board[r][c] == colour and board[r+1][c+1] == colour and board[r+2][c+2] == colour and board[r+3][c+3] == colour:
        return False
  #check \
  for c in range(4):
    for r in range(3, 6):
      if board[r][c] == colour and board[r-1][c+1] == colour and board[r-2][c+2] == colour and board[r-3][c+3] == colour:
        return False

def make_board(board):
  for c in range(7):
    for r in range(6):
      if board[r][c] == 1:
        pygame.draw.circle(screen, red, (c*x_dist + bottom_left_x, 541 - r*y_dist), radius)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, yellow, (c*x_dist + bottom_left_x, 541 - r*y_dist), radius)
      else:
        pygame.draw.circle(screen, black, (c*x_dist + bottom_left_x, 541 - r*y_dist), radius)
  pygame.display.update()
        

# game loop
running = True
board = create_board()
print(board)
pygame.display.update()

while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
          
        if event.type == pygame.MOUSEMOTION:
          posx = event.pos[0]

          if turn % 2 == 0:
            if pygame.mouse.get_pos()[0] > 75 and pygame.mouse.get_pos()[0] < 725:
              pygame.draw.circle(screen, red, (posx, bottom_left_y - 6*y_dist), radius)

          else: 
            if pygame.mouse.get_pos()[0] > 75 and pygame.mouse.get_pos()[0] < 725:
              pygame.draw.circle(screen, yellow, (posx, bottom_left_y - 6*y_dist), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
          if pygame.mouse.get_pos()[0] < 75 or pygame.mouse.get_pos()[0] > 725:
            continue
          if turn % 2 == 0:
            posx = pygame.mouse.get_pos()[0]
            column = int(math.floor((posx - 80)/(640/7)))
            if column >= 0 and column <= 6:
              if valid_move(board, column):
                row = next_row(board, column)
                place_piece(board, row, column, 1)
                if continue_game(board, 1) == False:
                  running = False

          else:
            posx = pygame.mouse.get_pos()[0]
            column = int(math.floor((posx - 80)/(640/7)))
            if column >= 0 and column <= 6:
              if valid_move(board, column):
                row = next_row(board, column)
                place_piece(board, row, column, 2)
                if continue_game(board, 2) == False:
                  running = False

          print(board)
          turn += 1
          if running == False:
            pygame.time.wait(4000)
        make_board(board)

                  
    screen.fill(black)
    boardPos()   
    

