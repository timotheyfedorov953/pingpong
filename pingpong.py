from pygame import *
import random 
init()
width = 880
height = 880
window = display.set_mode((width, height))
timer = time.Clock()
size = 80
class Box():
    def __init__(self,x, y):
        self.startx = x
        self.starty = y


class Player(Box):
    def __init__(self,x, y,speed):
        Box.__init__(self, x, y)
        self.speed = speed
        self.start_speed = speed 
        self.image = Surface((10, size))
        self.image.fill((0,0,255))
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


player = Player(20, height//2, 2)
game = True
while game:
    window.fill('black')
    game_events = event.get()   
    player.control()

    for ev in game_events:
        if ev.type == QUIT:
            game = False
    player.move()

    window.blit(player.image,(player.rect.x, player.rect.y))   
            

    timer.tick(100)
    display.flip()