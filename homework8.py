import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))    
pygame.display.update()
on=pygame.image.load("pgzero/on.png")
off=pygame.image.load("pgzero/off.png")
pygame.transform.scale(on,(600,600))
pygame.transform.scale(off,(600,600))
while 1:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            screen.blit(on,(0,0))
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            screen.blit(off,(0,0))
            pygame.display.update()