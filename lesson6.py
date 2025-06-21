import pygame
import time
pygame.init()
HEIGHT=600
WIDTH=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happy Birthday! :)")
#load and scale first background
balloon=pygame.image.load("pgzero/balloon.jpg")
cake=pygame.image.load("pgzero/caek.jpg")
confetti=pygame.image.load("pgzero/confetti.jpg")
pygame.transform.scale(cake,(WIDTH,HEIGHT))
pygame.transform.scale(balloon,(WIDTH,HEIGHT))
while 1:
    font=pygame.font.SysFont("Calibri",70)
    text1=font.render("Happy",True,(0,0,0))
    text2=font.render("Birthday",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(balloon,(0,0))
    screen.blit(text1,(200,150))
    screen.blit(text2,(200,200))
    pygame.display.update()
    time.sleep(2)

    screen.fill((255,255,255))
    screen.blit(cake,(0,0))
    pygame.display.update()
    time.sleep(2)

    screen.fill((255,255,255))
    screen.blit(confetti,(0,0))
    pygame.display.update()
    time.sleep(2)