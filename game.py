import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('collect the trash')

image = pygame.image.load("recycling.jpg")
background = pygame.image.load("naturebackground.jpg")
nature = pygame.transform.rotozoom(background,0,1.75)
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def dis_score(score):
    value = font_style.render("Score: " + str(score), True, red)
    dis.blit(value, [0,0])

def recyclebin(x,y):
    binimage = pygame.transform.rotozoom(image,0,0.033)
    dis.blit(binimage,(x,y))
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height - 100
 
    x1_change = 0
    food_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = 0

    score = 0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    food_change = 10
                    
     
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    food_change = 10
                    
            if event.type == pygame.KEYUP:
                x1_change = 0
                food_change = 10
 
        if x1 >= dis_width:
            x1_change = -snake_block
        
        if x1 < 0:
            x1_change = snake_block

        if foody >= dis_height:
            game_close = True
            
 
        x1 += x1_change
        foody += food_change
        dis.fill(white)
        dis.blit(nature,(0,0))
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        recyclebin(x1,y1)
        dis_score(score)
        pygame.display.update()
 
        if abs(x1 - foodx)<=10 and y1 == foody:
            foodx = round(random.randrange(100, dis_width - snake_block - 100) / 10.0) * 10.0
            foody = 0
            score +=1
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
