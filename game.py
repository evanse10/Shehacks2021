## game functions:
##display
##facts about the environment
##garbage: falling, speed
##bins: moving left/right
##did the garbage make it in the bin?
##number of lives - maybe we should take this out so we can display our garbage facts more often?
##score/how much garbage was collected

## FACTS
## The average college student produces 640 pounds of solid waste each year, including rougly 500 disposable cups and 320 pounds of paper
## By 2050, the ocean will contain more plastic by weight than fish
## In 2018, americans disposed of 146.2 million tons of trash - 24 percent was food waste (35.28 million tons)
## The Geat Pacific Garbage Patch contains almost 3.5 million tons of trash

import pygame
import time
import random
 
pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


def display():
    while True:
        dis = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Shehacks 2021")

class bin():
    def __init__(self):
        self.image = pygame.image.load("bin.jpg")
        self.surface = pygame.Surface((100,100))
        self.rectangle = self.surface.get_rect()
    
    def move(self):
        pressed_key = pygame.ket.get_pressed()
        

        




display()


##hello from liz