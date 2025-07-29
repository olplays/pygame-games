import pygame
pygame.init()
screen=pygame.display.set_mode((1200,1200))    
on=pygame.image.load("pgzero/fan_on.png")
off=pygame.image.load("pgzero/fan_off.png")
pygame.transform.scale(on,(300,300))
pygame.transform.scale(off,(300,300))
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
        if event.type== pygame.QUIT:
            pygame.quit()
            