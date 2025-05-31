import pgzrun
from random import randint

    
TITLE="flappy ball"
WIDTH=800
HEIGHT=600
R=randint(0,255)
G=randint(0,255)
B=randint(0,255)
jump_height=-40
clr=R,G,B
GRAVITY=200
gameover=False
class Ball:
    def __init__(self,x_pos_initial,y_pos_initial,):
        self.x=x_pos_initial
        self.y=y_pos_initial
        self.vx=200
        self.vy=10
        self.radius=40
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,clr)

ball=Ball(50,20)
def draw():
    screen.clear()
    ball.draw()
if gameover==False:
    def update(dt):
        #acceleration formula
        uy=ball.vy
        ball.vy=ball.vy + GRAVITY * dt
        ball.y=ball.y+(uy+ball.vy)*0.5+dt
        #bounce back of wall
        if ball.y>HEIGHT-ball.radius :
            ball.y=HEIGHT-ball.radius
            ball.vy=-ball.vy*0.9 #collision
            gameover=True
        elif ball.y<ball.radius:
            ball.vy=-ball.vy*0.4 #collision
            ball.y=ball.radius
        ball.x=ball.x+ball.vx*dt
        if ball.x>WIDTH-ball.radius or ball.x<ball.radius:
            ball.vx=-ball.vx
        
def on_key_down(key):
        if key==keys.SPACE:
            if gameover== False:
                ball.vy= jump_height

        if key== keys.R:
            ball.y=20

    
def GAMEOVER():
    GRAVITY=0
    ball.vy=0
    ball.vx=0
    jump_height=0
    gameover=True


pgzrun.go()