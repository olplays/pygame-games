import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
Color=(0,134,255)
pygame.display.update()
class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_radius=radius
        self.circle_width=width #code to fill color in circle
        self.circle_surcface=screen
    def draw(self):
        self.Draw_circle=pygame.draw.circle(self.circle_surcface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)
    def grow(self,r):
        self.circle_radius=self.circle_radius+r
        self.Draw_circle=pygame.draw.circle(self.circle_surcface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)

circle=Circle(Color,(300,300),25,0)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle.grow(20)
            pygame.display.update()



