from pygame import *
import random 
init()
width = 880
height = 880
window = display.set_mode((width, height))
timer = time.Clock()
size = 80

count_player = 0
count_opponent = 0
font.init()
screen = display.set_mode((1000,1000)) 
font_1=font.SysFont('Arial',40)

mixer.music.load('pingpong/ball_sound.mp3')
mixer.music.set_volume(1)

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
        global count_opponent,count_player
        if self.rect.colliderect(player.rect):
            self.speedX=self.speed
            mixer.music.play()

        if self.rect.colliderect(opponent.rect):
            self.speedX=-self.speed
            mixer.music.play()

        if self.rect.y <10 or self.rect.colliderect(player.rect):
            self.speedY=self.speed
            mixer.music.play()
             
        if self.rect.y > height or self.rect.bottom >=height and self.rect.colliderect(opponent.rect):
            self.speedY=-self.speed
            mixer.music.play()
    
        if self.rect.x <10 or self.rect.x > width:
            self.rect.x = width//2
            self.rect.y = height // 2
            self.speedX=-1*self.speedX
            
        
        self.rect.x +=self.speedX
        self.rect.y +=self.speedY

        if  self.rect.x <10:
            count_opponent += 1
        if  self.rect.x > width:
            count_player +=1
        
        
        
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
        if self.rect.bottom < height:
            self.rect.y += self.speed*self.direction
        elif self.rect.y >0:
            self.rect.y += self.speed*self.direction
    
        if  ball.rect.centery > self.rect.centery:
            self.direction=1 
        else:
            self.direction=-1



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

    text_click = font_1.render(str(count_player) + " : " + str(count_opponent),True, (255,0,0))
    window.blit(text_click,(width // 2, 10))

        
            

    timer.tick(100)
    display.flip()