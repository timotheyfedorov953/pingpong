from pygame import *
import random 
init()
width = 880
height = 880
window = display.set_mode((width, height))
timer = time.Clock()
size = 80


class Ball():
    def __init__(self,x, y,speed, color):
        self.speedX = speed
        self.speedY = speed
        self.speed = speed
        self.image = Surface((5,5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.size = size
    
    def move(self):
        if self.rect.x <=10:
            self.speedX=self.speed

        if self.rect.right >=width:
            self.speedX=-self.speed

        if self.rect.y <=10:
             self.speedY=self.speed
             
        if self.rect.bottom >=height:
            self.speedY=-self.speed
        
        self.rect.x +=self.speedX
        self.rect.y +=self.speedY

class Player():
    def __init__(self,x, y,speed, color):
        self.speed = speed
        self.start_speed = speed 
        self.image = Surface((10, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.size = size
        self.direction = 1 

    def control(self):
        keys = key.get_pressed ()
        if keys[K_w] == 1:
            self.direction =-1
        
        if keys[K_s] == 1:
            self.direction =1
    
    def move(self):
        self.rect.y += self.speed*self.direction
        if self.rect.y <=10 or self.rect.bottom >=height:
            self.direction*=-1

    def autopilot(self):
        self.rect.y += self.speed*self.direction
        if self.rect.y <=10 or self.rect.bottom >=height:
            self.direction*=-1

opponent = Player(width - 20, height//2, 2,(0,255,255))
player = Player(20, height//2, 2, (255,255,255))
ball = Ball(width//3,height//2,2, (255,0,0))
game = True
while game:
    window.fill('black')
    game_events = event.get()   
    player.control()

    for ev in game_events:
        if ev.type == QUIT:
            game = False
    player.move()
    opponent.autopilot()
    ball.move()
    window.blit(player.image,(player.rect.x, player.rect.y))   
    window.blit(opponent.image,(opponent.rect.x, opponent.rect.y))  
    window.blit(ball.image,(ball.rect.x, ball.rect.y))    
            

    timer.tick(100)
    display.flip()