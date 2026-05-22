import pygame
import keyboard
import random

pygame.init()

frame_number=0
frames_since=0
dev=False
scW,scH=800,600
touching=False

#for platform
x_pos=0
x_size=0
y_size=0
speed=1
min_size_x=200
min_size_y=200
often=160
max_size=300

#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
ice_blue=(214, 255, 250)

screen = pygame.display.set_mode((scW, scH))
clock = pygame.time.Clock()
running = True
pygame.font.init()
myfont=pygame.font.SysFont('Arial',20)
done=False

class Player:
    def __init__(self):
        self.img=pygame.image.load('LIAM_POLARBEAR.png').convert_alpha()
        
        self.pos=(400,300)
        self.speed=4
        self.jumping=False
        self.scale = 0.3
        self.up=False
        Iw, Ih = self.img.get_size()
        self.image = pygame.transform.scale(self.img, (int(Iw * self.scale), int(Ih * self.scale)))
        self.rect = self.image.get_rect(center=(self.pos))
        self.falling=False
        
    def draw(self):
        screen.blit(self.image, self.rect)
    
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and not self.falling:
            self.rect.x-=self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and not self.falling:
            self.rect.x+=self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP] and not self.falling:
            self.rect.y-=self.speed+speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and not self.falling:
            self.rect.y+=self.speed-speed
            
        if keys[pygame.K_SPACE] and not self.jumping and not self.falling:
            self.jump()
        
        if keys[pygame.K_p] and dev:
            global done
            done=True
        if keys[pygame.K_x] and dev:
            self.die()
        
        
        if self.jumping and self.up:  #if moving up and jumping
            self.scale+=0.01            
        if self.jumping and self.scale>=0.5:   #if hit peak of jump
            self.up=False
        if self.jumping and not self.up and not self.scale <= 0.3:    #falling while jumping
            self.scale-=0.01
        if self.jumping and not self.up and self.scale <=0.3: #landing
            self.jumping=False
            self.speed=4
        
        if self.falling and self.scale > 0.1:      #when death
            self.scale-=0.01
        if self.falling and self.scale <= 0.1:
            done=True
            self.falling=False
                
        center=self.rect.center
        Iw, Ih = self.img.get_size()
        self.image = pygame.transform.scale(self.img, (int(Iw * self.scale), int(Ih * self.scale)))
        self.rect = self.image.get_rect(center=center)
        
    def collide(self):
        on_platform=False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                on_platform=True
        if not on_platform and not dev and not self.jumping:
            self.die()
            
        
    def jump(self):
        self.jumping=True
        self.up=True
        self.speed=7
    
    def die(self):
        self.jumping=False
        self.up=False
        self.falling=True

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,x_size,y_size,y=0):
        super().__init__()
        self.image=pygame.Surface([x_size,y_size])
        
        self.image.fill(ice_blue)
        
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    
    def movement(self):
        self.rect.y+=speed
        if self.rect.colliderect(player.rect):
            global touching
            touching=True
        if self.rect.top >= scH:
            self.kill()
        
platforms=pygame.sprite.Group()
platforms.add(Platform(0,800,600,50))
player=Player()

def platform_create():
    randomN=random.randrange(0,often,1)
    if randomN==0:
        x_pos=random.randrange(0,scW-50)
        x_size=random.randrange(min_size_x,min_size_x+max_size)
        y_size=random.randrange(min_size_y,min_size_y+max_size)
        platforms.add(Platform(x_pos,x_size,y_size,0-y_size))
        
    
while running:
    touching=False
    
    dt=clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     # if click X exit
            running = False
            
    if frames_since==3600:
        speed+=1
        frames_since=0
        #often+=50
            
    screen.fill(blue)
    
    platform_create()
    
    platforms.draw(screen)
    player.draw()
    player.move()
    player.collide()
    
    if frame_number>0:
        for p in platforms:
            p.movement()
                
    if touching:
        player.rect.y+=speed
    
    time_text=myfont.render(f"{int(frame_number/60)}",True,black)
    screen.blit(time_text,(10,10))
    
    if dev:
        pygame.draw.rect(screen, (0,0,0), player.rect,1)
        
    
    #NEEDS TO BE UNDER ALL DRAW
    pygame.display.flip()
        
    frame_number+=1
    frames_since+=1
        
    if done:
        #print('we work')
        screen.fill(black)
        win_txt=myfont.render(f"Game over. You survived {int(frame_number/60)} seconds. Press space to exit",True,white)
        credit_txt=myfont.render("Credits:   Liam Yoo: Polar Bear drawing    Sami Awdeh: Everything else ",True,white)
        screen.blit(win_txt,(scW//2-250,scH//2))
        screen.blit(credit_txt,(scW//2-300,350))
        pygame.display.flip()
        keyboard.wait('space') 
        break

pygame.quit()