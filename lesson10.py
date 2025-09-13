import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()

# load image
subway=pygame.image.load("subway.png")
ludo=pygame.image.load("ludo.png")
temple=pygame.image.load("temple.png")
candy=pygame.image.load("candy.jpg")

#place images
screen.blit(subway,(150,100))
screen.blit(ludo,(150,200))
screen.blit(temple,(150,300))
screen.blit(candy,(150,400))
#font and text
font=pygame.font.SysFont("roboto",30)
text=font.render("Ludo",True,(0,0,0))
text2=font.render("Candy Crush",True,(0,0,0))
text3=font.render("Temple run",True,(0,0,0))
text4=font.render("Subway surfer",True,(0,0,0))

#place text

screen.blit(text,(350,200))
screen.blit(text3,(350,300))
screen.blit(text2,(350,400))
screen.blit(text4,(350,100))
pygame.display.update()
#event loop
run=True
first_click=None
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if first_click is None:
                first_click=pos
            else:
                pygame.draw.line(screen,(0,0,0),first_click,pos,3)
                first_click=None
                pygame.display.update()
pygame.quit()
