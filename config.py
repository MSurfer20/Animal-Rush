import pygame
import math
import random
import sys

pygame.init()
ARCADE_FONT = pygame.font.Font('ARCADE_N.TTF', 25)
FONT = pygame.font.Font('ARCADE_N.TTF', 25)
ICON = pygame.image.load('gameicon.png')
OVER_FONT = pygame.font.Font('freesansbold.ttf', 56)
GREEN = (50, 104, 0)
BLACK = (0, 0, 0)
ENTER = "PRESS ENTER TO CONTINUE"
NEWGAME = "HIT ENTER TO START A NEW GAME!"
TIE = "THE GAME IS A TIE"
GAMENAME = "Animal Rush"
PLAYER2 = pygame.image.load('player1.png')
PLAYER1 = pygame.image.load('player.png')
READY = "GET READY PLAYER "
ROUND_TIE = "ROUND TIED BETWEEN PLAYER 1 AND 2"
BLUE = (68, 187, 255)
WIN = " WON THE GAME"
FINSCOR = "FINAL SCORE FOR PLAYER "
CONGO = "CONGRATULATIONS ON CROSSING THE RIVER"
COLLI = "YOU GOT COLLIDED WITH THE OBSTACLE!!"
RED = (255, 0, 0)
screen_size = (1400, 900)
