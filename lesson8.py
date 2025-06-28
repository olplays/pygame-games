import pygame
from pygame.locals import *
from time import *
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#initial position of player
playerx=200
playery=200
keys=[False,False,False,False]
player=pygame.image.load("pgzero/rocket.png")
background=pygame.image.load("pgzero/space.png")

while playery<600:
    screen.blit(background,(0,0))
    screen.blit(player,(playerx,playery))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit(0)
        #check whetther any other key is pressed
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            if event.key==K_LEFT:
                keys[1]=True
            if event.key==K_DOWN:
                keys[2]=True
            if event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            if event.key==K_LEFT:
                keys[1]=False
            if event.key==K_DOWN:
                keys[2]=False
            if event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if playery>0:
            playery-=2
    elif keys[2]:
        if playery<500:
            playery+=2
    elif keys[1]:
        if playerx>0:
            playerx-=2
    elif keys[3]:
        if playerx<500:
            playerx+=2
    pygame.display.update()
    playery+=1
    sleep(0.01)
font=pygame.font.SysFont("Roboto",100)
text=font.render("GAME OVER",True,(0,0))
screen.blit(text)
pygame.display.update()
sleep(5)
pygame.quit()