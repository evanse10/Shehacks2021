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
soda = pygame.image.load("crushedcan.jpg")
 
clock = pygame.time.Clock()
 
bin_block = 20
bin_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
enviro_facts = ["The average college student produces 640 pounds of solid waste each year", 
"By 2050, the ocean will contain more plastic by weight than fish",
"In 2018, Americans disposed of 146.2 million tons of trash - 24% was food waste",
"The Great Pacific Garbage Patch contains almost 3.5 million tons of trash",
"Roughly 80% of the items in lanfill could be recycled :o"]

 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def dis_score(score):
    value = font_style.render("Score: " + str(score), True, red)
    dis.blit(value, [0,0])

def recyclebin(x,y):
    binimage = pygame.transform.rotozoom(image,0,0.033)
    dis.blit(binimage,(x,y))
 
def sodacan(x,y):
    crushsoda = pygame.transform.rotozoom(soda,0,0.035)
    dis.blit(crushsoda,(x,y))
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height - 100
 
    x1_change = 0
    trash_change = 0
 
    trash_x = round(random.randrange(0, dis_width - bin_block) / 10.0) * 10.0
    trashy = 0

    score = 1
 
    while not game_over:
 
        if game_close == True:
            index = random.randint(0,4)
        
        while game_close == True:
            dis.fill(white)
            dis.blit(nature,(0,0))

            end = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            fact = font_style.render(enviro_facts[index], True, blue)
            end_score = font_style.render("Final score: " +str(score-1), True, red)
            dis.blit(end, [30,60])
            dis.blit(end_score, [30,80])
            dis.blit(fact, [0,30])
            
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
                    x1_change = -bin_block
                    trash_change = 10*score**0.2
                    
     
                elif event.key == pygame.K_RIGHT:
                    x1_change = bin_block
                    trash_change = 10*score**0.2
                    
            if event.type == pygame.KEYUP:
                x1_change = 0
                trash_change = 10*score**0.2
 
        if x1 >= dis_width :
            x1_change = -bin_block
        
        if x1<0:
            x1_change = bin_block

        if trashy >= dis_height:
            game_close = True
            
        x1 += x1_change
        trashy += trash_change
        dis.fill(white)
        dis.blit(nature,(0,0))
        pygame.draw.rect(dis, blue, [trash_x, trashy, bin_block, bin_block])
        pygame.draw.rect(dis, black, [x1, y1, bin_block, bin_block])
        recyclebin(x1,y1)
        sodacan(trash_x,trashy)
        dis_score(score-1)
        pygame.display.update()
 
        if abs(x1 - trash_x)<=10 and abs(y1-trashy)<= 15:
            trash_x = round(random.randrange(100, dis_width - bin_block - 100) / 10.0) * 10.0
            trashy = 0
            score +=1
        clock.tick(bin_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()

