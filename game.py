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
        dis.fill(blue)
        pygame.display.update()
        pygame.display.set_caption("Shehacks 2021")
        ## need to add command to quit the screen - this might need to be the main function of the game

class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.jpg")
        self.surface = pygame.Surface((100,100))
        self.rectangle = self.surface.get_rect()
        ## need to create coordinates to keep track of the position and make starting coordinates
    
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key==K_LEFT & self.rect.left>0:
            self.rect.move_ip(-5,0)
            ## need to update the coordinates
        if pressed_key==K_RIGHT & self.rect.left>0:
            self.rect.move_ip(5,0)
            ## need to update the coordinates
            ## also might need to safeguard against running off the screen on the right side
    

        

        




display()


##hello from liz
