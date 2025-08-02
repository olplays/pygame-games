import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH=900
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACE INVADER")
red = ((255,0,0))
yellow = ((255,255,0))
black = ((0,0,0))
white = ((255,255,255))
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
HEALTH_FONT=pygame.font.SysFont("roboto",40)
WINNER_FONT=pygame.font.SysFont("comicsans",40)
FPS=60
MAX_BULLETS=3
VEL=5
BULLETS_VEL=7
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=55,50
yellow_ship_image=pygame.image.load(
    os.path.join("pgzero/ship1.png"))
yellow_ship=pygame.transform.rotate(pygame.transform.scale(
    yellow_ship_image,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

red_ship_image=pygame.image.load(os.path.join("pgzero/ship2.png"))
red_ship=pygame.transform.rotate(pygame.transform.scale(
    red_ship_image,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
background=pygame.image.load("pgzero/star.png")
yellow_hit=pygame.USEREVENT+1
red_hit=pygame.USEREVENT+2
def draw_window(red,red_bullets,red_health,yellow,yellow_bullets,yellow_health):
    screen.blit(background,(0,0))
    pygame.Rect(screen,black,BORDER)
    red_health_text=HEALTH_FONT.render("HEALTH: "+str(red_health),1,white)
    yellow_health_text=HEALTH_FONT.render("HEALTH: "+str(yellow_health),1,white)
    screen.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text,(10,10))
    
    screen.blit(yellow_ship,(yellow.x,yellow.y))
    screen.blit(red_ship,(red.x,red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(screen,yellow,bullet)
    for bullet in red_bullets:
        pygame.draw.rect(screen,red,bullet)
    pygame.display.update()
def yellow_handle_movements(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x -VEL>0:
        yellow.x -=VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x +=VEL
    if key_pressed[pygame.K_w] and yellow.y -VEL>0:
        yellow.y -=VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT-15:
        yellow.x +=VEL

def red_handle_movements(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x + VEL + red.width > BORDER.width + BORDER.x:
        red.x -=VEL
    if key_pressed[pygame.K_RIGHT] and red.x <WIDTH:
        red.x +=VEL
    if key_pressed[pygame.K_UP] and red.y -VEL>0:
        red.y -=VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height <HEIGHT-15:
        red.x +=VEL

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,white)
    screen.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,
                HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow= pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets=[]
    yellow_bullets=[]
    red_health=10
    yellow_health=10
    #set thye timer
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #red bullet
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet=pygame.rect(
                        yellow.x +yellow.width,yellow.y+yellow.height//2-2,10,5
                    )
                    yellow_bullets.append(bullet)
                #yellow bullet
                if event.key ==pygame.K_RETURN and len(red_bullets)<MAX_BULLETS:
                    bullet=pygame.rect(
                        red.x +red.width,red.y+red.height//2-2,10,5
                    )
                    red_bullets.append(bullet)
            if event.type == red_hit:
                red_health -= 1
            if event.type == yellow_hit:
                yellow_health -=1
        winner_text=""
        if red_health<=0:
            winner_text="YELLOW WINS!!!"
        if yellow_health<=0:
            winner_text="RED WINS!!!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        key_pressed=pygame.key.get_pressed()
        yellow_handle_movements(key_pressed,yellow)
        red_handle_movements(key_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        pygame.display.update()
if __name__ =="main":
    main()



