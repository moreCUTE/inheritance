import pygame
import math
import random
pygame.init()

Monsterlist = []
    
def CircularCollision(x1, y1, x2, y2, imgSize = 100):
    x1+=imgSize/2
    y1+=imgSize/2
    if math.sqrt((x1-x2)*(x1-x2)+ (y1-y2)*(y1-y2)) < imgSize/2:
        return True
    else:
        return False

class Monster():    
          
        def __init__(self, x, y):
            self.xpos = x
            self.ypos = y
            self.health = 100
            self.alive = True
            self.image = None
            self.imageSize = None
            
            
        def getClicked(self, MouseX, MouseY):
            if CircularCollision(self.xpos, self.ypos, MouseX, MouseY)==True and self.alive==True:
                self.speak()
                self.teleport()
                self.health-=10
                
        def ded(self):
            if self.health <= 0 and self.alive == True:
                print("I'm ded.")
                self.alive = False
                
        def draw(self):
            if self.alive == True:
                screen.blit(self.image, (self.xpos, self.ypos))
        
        def speak(self):
            print("OW")
            
        def teleport(self):
            r = random.randint(1,100)
            mx = random.randint(-100,100)
            my = random.randint(-100,100)
            if r < 20:
                self.xpos += mx
                self.ypos += my
            
        

class Creeper( Monster ):           
        def __init__(self, xpos, ypos):
            Monster.__init__(self, xpos, ypos)
            self.image = pygame.image.load('creeper.jpg')
        def speak(self):
            print("TSSS")
            
class Spider( Monster ):           
        def __init__(self, xpos, ypos):
            Monster.__init__(self, xpos, ypos)
            self.image = pygame.image.load('spider.jpg')
            self.imageSize = 10
        def getClicked(self, MouseX, MouseY):
            if CircularCollision(self.xpos, self.ypos, MouseX, MouseY, self.imageSize)==True and self.alive==True:
                self.speak()
                self.teleport()
                self.health-=10
        def speak(self):
            print("KSISDHISHD")
        def teleport(self):
            r = random.randint(1,100)
            mx = random.randint(-100,100) * 2
            my = random.randint(-100,100) * 2
            if r < 60:
                self.xpos += mx
                self.ypos += my
            
class Zombie( Monster ):           
        def __init__(self, xpos, ypos):
            Monster.__init__(self, xpos, ypos)
            self.image = pygame.image.load('zombie.jpg')

class Skeleton( Monster ):           
        def __init__(self, xpos, ypos):
            Monster.__init__(self, xpos, ypos)
            self.image = pygame.image.load('skeleton.jpg')
        def speak(self):
            print("CLINK")
            
def MonsterGen():
    num = random.randrange(0,100)
    if num < 20:
        Monsterlist.append(Creeper(random.randrange(0, 750), random.randrange(0, 750)))
    elif num < 50:
       Monsterlist.append(Spider(random.randrange(0, 500), random.randrange(0, 500)))
    elif num < 80:
       Monsterlist.append(Zombie(random.randrange(0, 500), random.randrange(0, 500)))
    else:
       Monsterlist.append(Skeleton(random.randrange(0, 500), random.randrange(0, 500)))
    
for i in range (20):
    MonsterGen()
    
hot = pygame.image.load('hot.jpg')
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("monster gen with inheritance")
doExit = False
clock = pygame.time.Clock()
pos = pygame.mouse.get_pos()
click = False
while not doExit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        for mon in Monsterlist:
            mon.getClicked(pos[0], pos[1])
            mon.ded()
            
    screen.fill((0,0,0))
    for mon in Monsterlist:
        mon.draw()
        
    alive = False
    for m in Monsterlist:
        if m.alive == True:
            alive = True
            break
    if not alive:
        screen.blit(hot, (0,0)) 
        
  
    pygame.display.flip()
pygame.quit()
