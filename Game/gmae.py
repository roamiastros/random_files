import pygame
import time

pygame.init()

scW, scH = 800, 600
GROUND_Y = 550
FPS = 60

current_rock=""

dev=False

#colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

c_level=1

screen = pygame.display.set_mode((scW, scH))
clock = pygame.time.Clock()
running = True

pygame.font.init()

myfont=pygame.font.SysFont('Arial',20)

won=False

###################### PLAYER ##########################
class Player:
    def __init__(self, path):
        try:
            image = pygame.image.load(path).convert_alpha()
        except pygame.error as message:
            print(f"{message} fail")
            pygame.quit()
            exit()
        
        self.spawn=(50,450)
        
        scale = 0.2
        Iw, Ih = image.get_size()
        self.image = pygame.transform.scale(image, (int(Iw * scale), int(Ih * scale)))
        self.rect = self.image.get_rect(center=(self.spawn))
        
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -12
        self.gravity_force = 0.5
        self.on_ground = True
        
        self.deaths=0
        
    def gravity(self,platforms):
        self.vel_y += self.gravity_force
        self.rect.y += self.vel_y
        
        for p in platforms:
            if type(p) == pygame.rect.Rect:  
                if self.rect.colliderect(p) and self.vel_y > 0:  
                    self.rect.bottom = p.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.rect.colliderect(p) and self.vel_y<0:
                    self.rect.top=p.bottom
                    self.vel_y=0

        if self.rect.y >= GROUND_Y +200:
            self.death()
            
    def move_collide(self,d,platforms):
        self.rect.x+=d
        
        global c_level
        
        if self.rect.colliderect(level.Irect):
            if c_level+1>len(level.levels):
                global won
                won=True
            else:
                c_level+=1
                level.setup(c_level)
        
        for p in platforms:            
            if type(p) == pygame.rect.Rect:                
                if self.rect.colliderect(p):
                    if dx > 0:  # Moving right
                        self.rect.right = p.left
                    if dx < 0:  # Moving left
                        self.rect.left = p.right
                        
        for p in platforms:
            if type(p) == pygame.rect.Rect:  
                if self.rect.colliderect(p) and self.vel_y > 0:
                    self.rect.bottom = p.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.rect.colliderect(p) and self.vel_y<0:
                    self.rect.top=p.bottom
                    self.vel_y=0
        for sprite in brambles:
            if sprite.rect.colliderect(self.rect):
                self.death()
                
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def death(self):
        self.temp=0
        
        if type(self.deaths)==str:
            self.deaths=self.temp+68
        else:
            self.deaths+=1
            
        self.rect.center=self.spawn
        self.on_ground=False
        
        if str(66+1) in str(self.deaths):
            self.temp=self.deaths-(66+1)
            self.deaths="no"
        #print(f"u died. deaths: {self.deaths}")
        
    def p_spawn(self):
        self.rect.center=(self.spawn)
        
#################################PLAYER END####################################

########### Bramble ############
class bramble(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("bush.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect(center=(x,y))
        
        self.render=False
    def draw(self):
        screen.blit(self.image,self.rect)
########### bramble end ##########

brambles=pygame.sprite.Group()

################ LEVEL ################
class Level:
    def __init__(self):
        
        try:
            Gimage = pygame.image.load("goal.png").convert_alpha()
        except pygame.error as message:
            print(f"{message} fail")
            
            
        scale = 0.2
        Iw, Ih = Gimage.get_size()
        self.Gimage = pygame.transform.scale(Gimage, (int(Iw * scale), int(Ih * scale)))
        self.Irect = self.Gimage.get_rect(center=(10000000,1000000))
            
                
        #levels
        self.level_1=[(50,450),(255,255,205),(750,50),"Kaibab Limestone",
            pygame.Rect(0,GROUND_Y,scW-500,50),
            pygame.Rect(scW-400,GROUND_Y-100,100,40),
            pygame.Rect(100,400,50,20),
            pygame.Rect(0,300,100,40),
            pygame.Rect(250,175,50,20),
            pygame.Rect(500,200,50,20),
                (255,201,154),
            pygame.Rect(0,575,scW-500,25)
        ]
        
        
        self.lvl_2_b=[(750,300),(400,300)]
        
        self.level_2=[(50,100),(254, 204, 151),(750,450),self.lvl_2_b,"Toroweap Formation",
                pygame.Rect(0,GROUND_Y-200,scW-500,400),
                pygame.Rect(550, GROUND_Y,50,50),
                      (205,51,1),
                pygame.Rect(0,GROUND_Y,scW-500,400)
        ]
        
        self.lvl_3_b=[(225,300)]
        
        self.level_3=[(50,0),(205,51,1),(50,550),self.lvl_3_b,"Supai Group",
                      #wall so you cant walk back to get around
                      pygame.Rect(-50,0,49,600),
                      
                      pygame.Rect(0,100,200,100),
                      pygame.Rect(175,100,25,350),
                      pygame.Rect(325,200,75,200),
                      pygame.Rect(325,600,75,200)
        ]
        
        self.lvl_4_b=[(400,400)]
        
        self.level_4=[(50,500),(153,153,153),(750,50),self.lvl_4_b,"Redwall Limestone",
                      pygame.Rect(0,599,200,1),
                      pygame.Rect(250,500,50,25),
                      pygame.Rect(600,300,200,600),
                      (250,250,254),
                      pygame.Rect(375,373,50,2),
                      (100, 139, 136),
                      pygame.Rect(600,550,200,50),
                      pygame.Rect(-1,-100,1,700)
        ]
        
        self.lvl_5_b=[(97.5,524),(247.5,524),(397.5,524),(547.5,524)]
        
        self.level_5=[(20,400),(100, 139, 136),(750,450),self.lvl_5_b,"Bright Angel Shale",
                      pygame.Rect(0,500,45,300),
                      pygame.Rect(150,500,45,300),
                      pygame.Rect(300,500,45,300),
                      pygame.Rect(450,500,45,300),
                      pygame.Rect(600,500,45,300),
                      pygame.Rect(1+66,499,1,1)
                      ]
        
        self.level_6_b=[(75,100),(170,275)]
        
        self.level_6=[(500,0),(255,153,54),(750,550),"Tapeats Sandstone",
                      #outside borders
                      
                      pygame.Rect(801,0,50,GROUND_Y),
                      
                      pygame.Rect(0,50,650,50),
                      pygame.Rect(200,250,800,50),
                      pygame.Rect(0,600,800,1),
                      
                      self.level_6_b
        ]
        
        self.level_7_b=[(466,574)]
        self.level_7=[(50,500),(255,153,54),(450,644),self.level_7_b,"Tapeats Sandstone",
                      pygame.Rect(0,599,800,1)       
        ]       
    
        self.level_8=[(500,500),(255,153,54),(50,550),"Tapeats Sandstone",
                      pygame.Rect(-2,0,1,800),
                      pygame.Rect(0,450,200,20),
                      pygame.Rect(450,550,350,30),
                      pygame.Rect(0,750,800,10),
                      pygame.Rect(200,450,20,150)
                      ]
        
        self.level_9_b=[(450,574),(494,574),(700,623)]
        
        self.level_9=[(50,500),(51,51,51),(750,550),"Vishnu Schist",
                    pygame.Rect(0,599,800,1),
                      self.level_9_b
        ]
        
        self.level_10_b=[(200,300),(300,350)]
        
        self.level_10=[(50,10),(51,51,51),(0,550),self.level_10_b,"Vishnu Schist",
             pygame.Rect(0,100,200,50),
             pygame.Rect(0,590,100,10),
                        (252,252,252),
             pygame.Rect(400,100,100,50),
             pygame.Rect(500,400,30,10),
             pygame.Rect(-1,-100,1,700),
             pygame.Rect(600,599,40,1),
             pygame.Rect(200,599,40,1)
            ]
        
        self.levels=[self.level_1,self.level_2,self.level_3,self.level_4,self.level_5,self.level_6,self.level_7,self.level_8,self.level_9,self.level_10]
             
        self.platforms = []
            
        self.setup(1)
        
    def setup(self,lvlN):
        brambles.empty()
        
        self.current_level=self.levels[lvlN-1]                
        self.color=self.current_level[1]
        
        temp_spawn=(self.current_level)[0]
        player.spawn=temp_spawn
        player.p_spawn()
        
        self.goal=self.current_level[2]
        self.Irect.center=self.goal
        
        self.platforms=self.current_level[3:]
        
        self.drawL(screen)
                
        self.brambleRender=False
            
    def drawL(self, surface):
        surface.blit(self.Gimage, self.Irect)

        self.color=self.current_level[1]
        
        for p in self.platforms:
            if type(p) == tuple:
                self.color=p
            elif type(p)==list:
                for x,y in p:
                    if self.brambleRender==False:
                        brambles.add(bramble(x,y))  
                brambles.draw(screen)
                self.brambleRender=True
            elif type(p)==str:
                global current_rock
                current_rock=p
            else:
                pygame.draw.rect(surface, self.color, p)
 
##############LEVEL END#######################

player = Player("player.png")
level = Level()

#main loop
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     # if click X exit
            running = False
   
    death_txt=myfont.render(f"deaths: {player.deaths}",True,(0,0,0))
    lvl_txt=myfont.render(f"level: {c_level}",True,RED)
    rock_txt=myfont.render(f"current rock: {current_rock}",True,(0,0,0))
    
    keys = pygame.key.get_pressed()
    dx=0
    
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx=-player.speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx=player.speed
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if player.on_ground:
            player.vel_y = player.jump_power
            player.on_ground = False
    if keys[pygame.K_p]:
        print(player.rect.center)
    if keys[pygame.K_r] and dev:
        player.rect.center=level.goal
        time.sleep(0.1)
                
    player.move_collide(dx,level.platforms)
    player.gravity(level.platforms)

    screen.fill(WHITE)
    
    screen.blit(lvl_txt,(20,20))
    screen.blit(death_txt,(120,20))
    screen.blit(rock_txt,(240,20))
     
    if dev:
        pygame.draw.rect(screen, (0,0,0), player.rect,1)
    
    level.drawL(screen)
    player.draw(screen)
    pygame.display.flip()
    
    if won:
        screen.fill(BLACK)
        win_txt=myfont.render(f"You Win!     Levels: {c_level}      Deaths: {player.deaths}",True,WHITE)
        screen.blit(win_txt,(scW//2-200,scH//2))
        pygame.display.flip()
        time.sleep(10)
        break
    
pygame.quit()


