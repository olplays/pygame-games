import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
Color=(0,134,255)
pygame.display.update()
class Rectangle():
    def __init__(self,color,pos,x,y,width,height):
        self.rectangle_color=color
        #self.rectangle_pos=pos
        self.rectangle_x=x
        self.rectangle_y=y
        self.rectangle_width=width #code to fill color in rectangle
        self.rectangle_surcface=screen
        self.height=height
    def draw(self):
        self.Draw_rect=pygame.draw.rect(self.rectangle_surcface,self.rectangle_color,(self.rectangle_x,self.rectangle_y,self.rectangle_width,self.height))
    def grow(self,m):
        self.rectangle_width=self.rectangle_width+m
        self.height=self.height+m
        self.Draw_rect=pygame.draw.rect(self.rectangle_surcface,self.rectangle_color,(self.rectangle_x,self.rectangle_y,self.rectangle_width,self.height))
rect=Rectangle(Color,(80,200),50,100,50,100)
while 1:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            rect.grow(40)
            pygame.display.update()