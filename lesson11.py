import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
#add caption
pygame.display.set_caption("Rocket in space")
#load image
rocket=pygame.image.load("rocket.png")
background=pygame.image.load("star.png")

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=rocket
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        #keep player on the screen
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>screen.get_width():
            self.rect.right=screen.get_width()
        elif self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=screen.get_height():
            self.rect.bottom=screen.get_height()

#create group containing the sprites
sprites=pygame.sprite.Group()

def start_game():
    player=Player(200,400)
    sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        # get and set the pressed keys
        pressed_keys=pygame.key.get_pressed()
        player.update(pressed_keys)
        #add background
        screen.blit(background,(0,0))
        #draw all sprites
        sprites.draw(screen)
        pygame.display.flip()   

start_game()