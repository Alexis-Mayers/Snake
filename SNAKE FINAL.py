#########################################
# Programmer: Alexis Mayers
# Date: Nov. 28, 2016
# File Name: snake_template.py
# Description: This program is a template for Snake Game.
#               It demonstrates how to move and lengthen the snake.
#########################################

import pygame
pygame.init()
from math import sqrt
from random import randint
import time as t

HEIGHT = 600
WIDTH  = 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))

startTime=t.time()
counter = 20

eaten=0

WHITE = (255,255,255)
BLACK = (0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
GREEN=(0,255,0)
outline=0
delay=80
gameOver=False

introON=True
main=False

appleVisibility=True
#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 10
HSPEED = 10
VSPEED = 10

speedX = 0
speedY = -VSPEED
segx = [400]*3
segy = [400, 400+VSPEED, 400+2*VSPEED]
text = [("GAME OVER"),("Final Score: ")]

textX=300
textY=100
textX2=300
textY2=200

timertxt= [("Time: ")]
starttxt= [("PRESS ENTER TO START")]

appleX=randint(1,39)*20
appleY=randint(1,29)*20

greenAppleX=randint(1,39)*20
greenAppleY=randint(1,29)*20

introPic = pygame.image.load("SNAKE_INTRO.jpg")
introPic = pygame.transform.scale(introPic, (WIDTH,HEIGHT))
introPic = introPic.convert_alpha()

SnakeBackground = pygame.image.load("Snake_Background.jpg")
SnakeBackground = SnakeBackground.convert_alpha()

GameOverPic = pygame.image.load("Game_Over_Screen_copy.jpg")
GameOverPic = pygame.transform.scale(GameOverPic, (WIDTH,HEIGHT))
GameOverPic = GameOverPic.convert_alpha()

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
rad=pygame.mixer.music.load("Radioactive[Instrumental].wav")
bite=pygame.mixer.Sound("AppleBite.wav")

keys = pygame.key.get_pressed()

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)  # Pythagorean theorem

def intro_screen():
    pygame.mixer.music.play(-1, 0.0)
    introPic=pygame.image.load("SNAKE_INTRO.jpg")
    introPic=pygame.transform.scale(introPic, (WIDTH,HEIGHT))
    introPic = introPic.convert_alpha()
    screen.blit(introPic, (0,0))
    font = pygame.font.SysFont("Arial Black",50)
    textWelcome=font.render(("WELCOME TO"), 1, WHITE)
    screen.blit(textWelcome, (250,100))
    font = pygame.font.SysFont("Arial Black",50)
    textStart=font.render(("PRESS SPACE TO START"), 1, WHITE)
    screen.blit(textStart, (200,480))
    pygame.display.update()

def redraw_screen():   
    SnakeBackground = pygame.image.load("Snake_Background.jpg")
    SnakeBackground = SnakeBackground.convert_alpha()
    screen.blit(SnakeBackground, (0,0))
    font = pygame.font.SysFont("Arial Black",50)
    text=font.render(("Score: "+str(eaten)), 1, WHITE)
    screen.blit(text, (450,10))
    timertxt=font.render("Time: "+str(round(counter-(t.time()-startTime),1)),1,WHITE)
    screen.blit(timertxt, (10,10))

    if appleVisibility==True:
        apple= pygame.draw.circle(screen, RED, (appleX, appleY), 10)
        greenApple = pygame.draw.circle(screen, GREEN, (greenAppleX, greenAppleY), 10)
    if gameOver:
        for i in range(len(text)):
            textPrint=font.render(text[i],1, WHITE)
            screen.blit(textPrint,(textX[i],textY[i]))
    for i in range(len(segx)):
        if i==0:
            segmentCLR = (GREEN)
        elif i==len(segx)-1:
            segmentCLR = (BLUE)
        else:
            segmentCLR = (255,0,255)
        pygame.draw.circle(screen, segmentCLR, (segx[i], segy[i]), BODY_SIZE, outline)
    pygame.display.update()


def game_over_screen():
    GameOverPic=pygame.image.load("Game_Over_Screen_copy.jpg")
    GameOverPic=pygame.transform.scale(GameOverPic, (WIDTH,HEIGHT))
    GameOverPic = GameOverPic.convert_alpha()
    screen.blit(GameOverPic,(0,0))
    font = pygame.font.SysFont("Arial Black",70)
    text=font.render(("GAME OVER"), 1, BLACK)
    text2=font.render(("FINAL SCORE: "+str(eaten)), 1, BLACK)
    screen.blit(text,(textX,textY))
    screen.blit(text2,(textX2,textY2+100))
    pygame.display.update()             # display must be updated, in order
                                            # to show the drawings
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
inPlay = True


introON=True
while introON:
    intro_screen()
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            inPlay = False                # Flag that we are done so we exit this loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("GAME HAS STARTED")
            introON=False
            
            segx = [400]*3
            segy = [400, 400+VSPEED, 400+2*VSPEED]

while inPlay:
    # check for events
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                inPlay = False                # Flag that we are done so we exit this loop
        keys = pygame.key.get_pressed()

    # act upon key events
        if keys[pygame.K_LEFT] and speedX != HSPEED:
            speedX = -HSPEED
            speedY = 0
        if keys[pygame.K_RIGHT] and speedX != -HSPEED:
            speedX = HSPEED
            speedY = 0
        if keys[pygame.K_UP] and speedY != VSPEED:
            speedX = 0
            speedY = -VSPEED
        if keys[pygame.K_DOWN] and speedY != -VSPEED:
            speedX = 0
            speedY = VSPEED
        if keys[pygame.K_ESCAPE]:
            inPlay=False
            keys = pygame.key.get_pressed()


    # Detects if the snake goes off the screen
        if segx[0]>=WIDTH :
            print(text[0])
            inPlay = False
        if segy[0]<=0:
            print(text[0])
            inPlay = False
        if segx[0]<=0:
            print(text[0])
            inPlay = False
        if segy[0]>=HEIGHT:
            print(text[0])
            inPlay = False

    #Detects if time runs out
            if counter==0:
                inPlay = False
    # move all segments
        for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
            segx[i]=segx[i-1]               # every segment takes the coordinates
            segy[i]=segy[i-1]               # of the previous one
    # move the head
        segx[0] = segx[0] + speedX*2
        segy[0] = segy[0] + speedY*2

    # Detects if the snake eats the red apple
        num=distance(appleX, appleY, segx[0], segy[0])
        num2=distance(greenAppleX, greenAppleY, segx[0], segy[0])
        if num < 10:
            bite.play()
            appleX=randint(1,39)*20
            appleY=randint(1,29)*20
            segx.append(segx[-1])           # assign the same x and y coordinates
            segy.append(segy[-1])           # as those of the last segment.
            delay-=5
            counter+=10
            eaten+=1
            print("Your score is:", eaten)

    #Detects if snake eats poisonous apple
        if num2 < 10:
            bite.play()
            greenAppleX=randint(1,39)*20
            greenAppleY=randint(1,29)*20
            segx.pop()          # assign the same x and y coordinates
            segy.pop()          # as those of the last segment.
            delay+=5
            counter-=10
            eaten-=1
            print("Your score is:", eaten)

    #Changes the color of the added segment of the snake
        if eaten % 3 == 0:
            segmentCLR=(RED)

    # Snake runs into itself
        for i in range(1,len(segx),1):
            if segx[0]==segx[i] and segy[0]==segy[i]:
                inPlay = False

    # update the screen
        redraw_screen()
        pygame.time.delay(20)
    

pygame.mixer.music.stop()
game_over_screen()
pygame.time.delay(500)
pygame.quit()                           # always quit pygame when done!
