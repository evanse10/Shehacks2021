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

background = pygame.image.load("naturebackground.jpg")
nature = pygame.transform.rotozoom(background,0,1.75)

recycling = pygame.image.load("recycling.jpg")
soda = pygame.image.load("crushedcan.jpg")
banana = pygame.image.load("bananapeel.png")
##compost =
##candy =
##garbage =
 
clock = pygame.time.Clock()
 
bin_block = 20
bin_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
enviro_facts = ["The average college student produces 640 pounds of solid waste each year :o", 
"By 2050, the ocean will contain more plastic by weight than fish",
"In 2018, Americans disposed of 146.2 million tons of trash - 24% was food waste",
"The Great Pacific Garbage Patch contains almost 3.5 million tons of trash",
"Roughly 80% of the items in lanfill could be recycled :o",
"The average person generates over 4 pounds of trash every day",
"1/3 of all the food produced globally goes to waste"]

 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def dis_score(score):
    value = font_style.render("Score: " + str(score), True, red)
    dis.blit(value, [0,0])

def recyclebin(x,y):
    binimage = pygame.transform.rotozoom(recycling,0,0.075)
    dis.blit(binimage,(x,y))
 
def sodacan(x,y):
    crushsoda = pygame.transform.rotozoom(soda,0,0.050)
    dis.blit(crushsoda,(x,y))

def bananapeel(x,y):
    bananaskin = pygame.transform.rotozoom(banana,0,0.037)
    dis.blit(bananaskin,(x,y))
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height - 100
 
    x1_change = 0
    trash_change = 0
 
    trash_x = round(random.randrange(0, dis_width - bin_block) / 10.0) * 10.0
    trashy = 0

    bintype = 0 ##0 for recycling, 1 for compost, 2 for garbage
    trashtype = 0
   
    score = 1
 
    while not game_over:
 
        if game_close == True:
            index = random.randint(0,6)
        
        while game_close == True:
            dis.fill(white)
            dis.blit(nature,(0,0))

            end = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            fact = font_style.render(enviro_facts[index], True, blue)
            end_score = font_style.render("Final score: " +str(score-1), True, red)
            dis.blit(end, [270,420])
            dis.blit(end_score, [270,450])
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
                if event.key == pygame.K_r:
                    ##change bin
                    bintype = 0
                elif event.key == pygame.K_e:
                    ##change bin
                    bintype = 1
                elif event.key == pygame.K_w:
                    ##change bin
                    bintype = 2
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
        ##pygame.draw.rect(dis, blue, [trash_x, trashy, bin_block, bin_block])
        ##pygame.draw.rect(dis, black, [x1, y1, bin_block, bin_block])
        if bintype == 0:
            recyclebin(x1,y1)
        elif bintype == 1:
            pygame.draw.rect(dis,black, [x1, y1, bin_block,bin_block])
        elif bintype == 2:
            pygame.draw.rect(dis,blue, [x1, y1, bin_block,bin_block])
        if trashtype == 0:
            sodacan(trash_x,trashy)
        elif trashtype == 1:
            bananapeel(trash_x,trashy)
        elif trashtype == 2:
            pygame.draw.rect(dis,red, [trash_x, trashy, bin_block,bin_block])
        
        
        dis_score(score-1)
        pygame.display.update()
        
        if abs(x1 - trash_x)<=15 and abs(y1-trashy)<= 15 and trashtype == bintype:
            trash_x = round(random.randrange(100, dis_width - bin_block - 100) / 10.0) * 10.0
            trashy = 0
            trashtype = random.randrange(0,3)
            score +=1
        clock.tick(bin_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
