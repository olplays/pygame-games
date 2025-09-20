import pygame
pygame.init()
WIDTH=1600
HEIGHT=1400
screen=pygame.display.set_mode((WIDTH,HEIGHT))

class Polygon:
    def __init__(self,width,color,points):
        self.width=width
        #self.height=height
        #self.dimensions=(width,height)
        self.color=color
        self.points=points
    def draw(self,screen):
        pygame.draw.polygon(screen,self.color,self.points,self.width)    
        pygame.display.update()


triangle=Polygon((255,100,0),[(300,100),(200,300),(400,300)],0)

while 1:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit(0)
    triangle.draw(screen)
    pygame.display.update()

