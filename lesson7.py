import pygame
pygame.init()
import time
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
balloon=pygame.image.load("pgzero/balloon.jpg")
pygame.transform.scale(balloon,(WIDTH,HEIGHT))
confetti=pygame.image.load("pgzero/confetti.jpg")
pygame.transform.scale(confetti,(WIDTH,HEIGHT))
while 1:
    font=pygame.font.SysFont("roboto",65)
    text1=font.render("Happy father's day :)",True,(210,0,255))
    screen.blit(confetti,(0,0))
    screen.blit(text1,(50,100))
    pygame.display.update()
    time.sleep(3)

    font=pygame.font.SysFont("calibri",100)
    screen.fill((255,255,255))
    text2=font.render("<:-)",True,(203,8,47))
    screen.blit(balloon,(0,0))
    screen.blit(text2,(200,300))
    pygame.display.update()
    time.sleep(3)