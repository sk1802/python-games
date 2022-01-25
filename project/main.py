import math
import pygame
import random
pygame.init()



#game screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("My Game")
gameIcon=pygame.image.load("project/images/icon.png")
pygame.display.set_icon(gameIcon)

shot=pygame.image.load("project/images/shots.png")
shot=pygame.transform.scale(shot, (30,30))


enemies=["e1.png","e2.png","e3.png","e4.png"]

choice=[-1,1]

score=0
font =pygame.font.Font("freesansbold.ttf",32)
def show_score():
    screen.blit(font.render("SCORE : "+str(score),True,(255,255,255)),(0,0))

pygame.mixer.music.load("project/sounds/bg_sound.wav")
pygame.mixer.music.play(-1)

class bullets:
    def __init__(self,x,y,img):
        self.__fired__ = False
        self.__mover__=-5
        self.__x__=x
        self.__y__=y
        self.__img__=pygame.image.load("project/images/"+img)
        self.__img__=pygame.transform.scale(self.__img__, (40,40))
    def move(self,x):
        if(self.__fired__):
            self.__y__+=self.__mover__
            screen.blit(self.__img__, (self.__x__,self.__y__))
            if self.__y__<0:
                self.__fired__=False
                self.__x__=x
                self.__y__+=550
                
        if self.__y__<=0:
                self.__fired__=False
        if self.__fired__==False:
            self.__x__=x
    def get_x(self):
        return self.__x__
    def get_y(self):
        return self.__y__
    def activate(self):
        if self.__fired__:
            return
        pygame.mixer.Sound("project/sounds/shooting.wav").play()
        self.__fired__=True
    def deactivate(self):
        self.__y__=550
        self.__fired__=False
        
class player():
    def __init__(self,x,y,img):
        self.__x__=x
        self.__y__=y
        self.__img__=pygame.image.load("project/images/"+img)
        self.__img__=pygame.transform.scale(self.__img__, (40,40))
        screen.blit(self.__img__, (x,y))
    def move(self):
        screen.blit(self.__img__, (self.__x__,self.__y__))
        
    def set_x(self,x):
        self.__x__+=x
    def get_x(self):
        return self.__x__
    def get_y(self):
        return self.__y__
    
    


#enemy class
class enemy:
    
    def __init__(self,x,y,img):
        self.__mover__=3*random.choice(choice)
        self.__x__=x
        self.__y__=y
        self.__img__=pygame.image.load("project/images/"+img)
        self.__img__=pygame.transform.scale(self.__img__, (40,40))
        screen.blit(self.__img__, (x,y))
    def move(self):
    
        if self.__x__<=0 or self.__x__>=760:
            self.__mover__=-self.__mover__
            self.setY(20)
        self.setX(self.__mover__)
        
        screen.blit(self.__img__, (self.__x__,self.__y__))    
        
    def setX(self,x):
        self.__x__+=x
    def setY(self,y):
        self.__y__+=y
    
        screen.blit(self.__img__, (self.__x__,self.__y__))
    def get_x(self):
        return self.__x__
    def get_y(self):
        return self.__y__
    def destroy(self):
        
        self.__img__=None


def collision(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if(distance<=40):
        return True

def gameover():
    global score
    font =pygame.font.Font("freesansbold.ttf",32)
    screen.blit(font.render(" GAME OVER \n SCORE = "+str(score),True,(255,255,255)),(200,300))


def main():
    global score
    key=0
    counter =0
    p1=player(380,550,"player.png")
    
    
    
    ecount=3
    en=[]                
    e1=enemy(random.randint(0,760),0,random.choice(enemies))
    e2=enemy(random.randint(0,760),40,random.choice(enemies))
    e3=enemy(random.randint(0,760),80,random.choice(enemies))
    
    en.append(e1)
    en.append(e2)
    en.append(e3)
    
    
    
    bullet=bullets(380,550,"shots.png")

    running = True
    while running:
        
        screen.fill((150, 150, 200))
        bgimage=pygame.image.load("project/images/bg.jpg")
        bgimage=pygame.transform.scale(bgimage, (800,600))
        screen.blit(bgimage, (0,0))
        
        counter+=1
        if(counter>=2000 or len(en)<ecount):
            counter=0
            en.append(enemy(random.randint(0,760),0,random.choice(enemies)))
            ecount=len(en)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
        
        #check if right key is pressed or left key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if(p1.get_x()<=760):
                    p1.set_x(5)
                    key=pygame.K_RIGHT
            if event.key == pygame.K_LEFT:
                if(p1.get_x()>0):
                    p1.set_x(-5)
                    key=pygame.K_LEFT
            if event.key == pygame.K_UP and key!=pygame.K_UP:  
                    bullet.activate()   
                                
            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.set_x(0)
        
        
        for i in range(len(en)):
            if(collision(en[i].get_x(),en[i].get_y(),p1.get_x(),p1.get_y())):
                running=False
                break
            if(collision(en[i].get_x(),en[i].get_y(),bullet.get_x(),bullet.get_y())):
                pygame.mixer.Sound("project/sounds/died.wav").play()
                score+=10
                bullet.deactivate()
                d=en.pop(i)
                d.destroy()
                break
            
        for i in range(len(en)):
            en[i].move()
        bullet.move(p1.get_x())
        p1.move()
        show_score()
        pygame.display.update()
    gameover()
    start = pygame.time.get_ticks()
    while(True):
        if pygame.time.get_ticks()-start>=2000:
                break
        pygame.display.update()

main()