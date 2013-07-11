import pygame, math, random, Level, Gui

class Sprite(object):
    def __init__(self, surf):
        self.surf = pygame.image.load(surf).convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.width = 64
        self.rect.height = 64

class Minion(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self, surf)
        self.speed = 0
        self.frame = 0
        self.framerate = 0
        self.framebuffer = 0
        self.isAlive = True
        self.health = 10
        self.isActive = False
        self.isMoving = [False, True, False, False] # up down left right
    #fix this
    def dealDamage(self,health):
        if self.rect.x > 960:
            health -=2
            return health
    def update(self):
        #check for hit
        #if bullet.rect.colliderect(self.rect):
            #self.health =- turret.power
        #check if dead
        if self.health <= 0:
            self.isAlive = False
        #movement
        if self.isMoving[0] == True:
            if self.rect.move(0, -2).collidelist(Level.borderList) == -1:
                self.rect.move_ip(0, -2)
            else:
                if self.rect.move(-2, 0).collidelist(Level.borderList) == -1:
                    self.isMoving[0] = False
                    self.isMoving[2] = True
                elif self.rect.move(2, 0).collidelist(Level.borderList) == -1:
                    self.isMoving[0] = False
                    self.isMoving[3] = True
        elif self.isMoving[1] == True:
            if self.rect.move(0, 2).collidelist(Level.borderList) == -1:
                self.rect.move_ip(0, 2)
            else: 
                if self.rect.move(-2, 0).collidelist(Level.borderList) == -1:
                    self.isMoving[1] = False
                    self.isMoving[2] = True
                elif self.rect.move(2, 0).collidelist(Level.borderList) == -1:
                    self.isMoving[1] = False
                    self.isMoving[3] = True
        elif self.isMoving[2] == True:
            if self.rect.move(-2, 0).collidelist(Level.borderList) == -1:
                self.rect.move_ip(-2, 0)
            else:
                if self.rect.move(0, -2).collidelist(Level.borderList) == -1:
                    self.isMoving[2] = False
                    self.isMoving[0] = True
                elif self.rect.move(0, 2).collidelist(Level.borderList) == -1:
                    self.isMoving[2] = False
                    self.isMoving[1] = True
        elif self.isMoving[3] == True:
            if self.rect.move(2, 0).collidelist(Level.borderList) == -1:
                self.rect.move_ip(2, 0)
            else:
                if self.rect.move(0, -2).collidelist(Level.borderList) == -1:
                    self.isMoving[3] = False
                    self.isMoving[0] = True
                elif self.rect.move(0, 2).collidelist(Level.borderList) == -1:
                    self.isMoving[3] = False
                    self.isMoving[1] = True
    def selfDestruct(self, i):
        self.health = 0
        self.isAlive = False
        del minions[i]
    def draw(self, screen):
        screen.blit(self.surf, self.rect, pygame.Rect(0, 0, 64, 64))
                
                
playerTowers = []
class Tower(Sprite):
    def __init__(self,surf):
        Sprite.__init__(self, surf)
        self.frame = 0
        self.framerate = 0
        self.framebuffer = 0
        self.firerate = 0
        self.power = 0
        self.tier = 0
        self.range = 100 #radius
    def update(self, enemyX, enemyY):
        #checks for enemies
        if abs(math.sqrt((self.rect.centery - enemyY)**2 + (self.rect.centerx - enemyX)**2)) < self.range:
            print "shooting"
            #shoot
    def draw(self,screen):
        screen.blit(self.surf, self.rect, pygame.Rect(0,0, 64, 64))
class spawnTowers():
    def __init__(self):
        self.z = 0
        self.center = (0,0)
    def spawn(self,screen, buying_index):
        for i in Level.borderList:
            if i.collidepoint(pygame.mouse.get_pos()):
                self.center = i.center
                if buying_index == 1:
                    playerTowers.append(Tower("Sprite Sheets/Towers/aminoacid.png"))
                    playerTowers[len(playerTowers)-1].rect.center = self.center
                elif buying_index == 2:
                    playerTowers.append(Tower("Sprite Sheets/Towers/antibody64x64.png"))
                    playerTowers[len(playerTowers)-1].rect.center = self.center
                elif buying_index == 3:
                    playerTowers.append(Tower("Sprite Sheets/Towers/Lymphocyte.png"))
                    playerTowers[len(playerTowers)-1].rect.center = self.center
class Projectile(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self, surf)
    def draw(self):
        screen.blit(self.surf, self.rect, pygame.Rect(64, 64, 64, 64))
        
minions = []
class Waves():
    def __init__(self):
        self.index = 0
        self.wave_num = 0
        self.num_enemies = 10
    def calcNumEnemies(self):
        self.num_enemies = 10
    def startWave(self):
        self.wave_num += 1
        for i in range(self.num_enemies):
            self.index = random.randint(1, 3)
            if self.index == 1:
                minions.append(Minion("Sprite Sheets/Enemies/bacteria.png"))
            elif self.index == 2:
                minions.append(Minion("Sprite Sheets/Enemies/commoncold.png"))
            elif self.index == 3:
                minions.append(Minion("Sprite Sheets/Enemies/germ.png"))

class Spawner():
    def __init__(self, list, coords):
        self.spawnrate = 1000
        self.time_since_last_spawn = 0.0
        self.current_time = pygame.time.get_ticks()
        self.tempTicks = 0
        self.elapsed = 0.0
        for i in range(len(list)):
            list[i].rect.topleft = coords[0], coords[1]
    def spawn(self, list, screen, paused):
        if paused:
            pass
        elif paused == False:
            self.elapsed = pygame.time.get_ticks() - self.current_time
        self.current_time = pygame.time.get_ticks()
        self.time_since_last_spawn += self.elapsed
        if self.time_since_last_spawn >= self.spawnrate:
            #for i in range(len(list)):
                #list[i].draw(screen)
            self.time_since_last_spawn = 0
            print self.elapsed, "Elapsed Time"
            for i in range(len(list)):
                if list[i].isActive == False:
                    list[i].isActive = True
                    print "spawn!"
                    break