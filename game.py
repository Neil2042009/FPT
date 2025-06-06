import pygame
import time
import random

black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

coin = 0 #Set the initial score
background = pygame.image.load()

pygame.init()
width, height = 720, 480
pygame.display.set_caption()
screen = pygame.display.set_mode((width, height))
