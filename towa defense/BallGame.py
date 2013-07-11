import pygame, sys, math

class Sprite(object):
	def __init__(self, surf):
		self.surf = surf
		self.rect = self.surf.get_rect()
		self.rect.width = 50
		self.rect.height = 50
		
class Ball(Sprite):
	def __init__(self, surf):
		Sprite.__init__(self, surf)
		self.direction = 0 #0upleft || 1upright || 2botleft || 3botright
		self.speed = 100
		self.frame = 0
		self.framerate = 3
		self.framebuffer = 0
		self.isMoving = [False, False, False, True]
		self.velx = 1
		self.vely = 1
		self.rect.x = 200
		self.rect.y = 100
	def update(self):
		if self.rect.top <= screen_rect.top:
			self.vely = 1
			#~ print "[0]"
			#~ self.direction = 0
			#~ if math.sqrt((self.rect.centery - 250)**2 + (self.rect.centerx - 0)**2) >= self.rect.w / 2.0:
				#~ self.rect.move_ip(self.speed * delta / 1000.0, self.speed * delta / 1000.0)
		if self.rect.bottom >= screen_rect.bottom:
			self.vely = -1
			#~ print "[1]"
			#~ self.direction = 1
			#~ if math.sqrt((self.rect.centery - 250)**2 + (self.rect.centerx - 0)**2) >= self.rect.w / 2.0:
				#~ self.rect.move_ip(self.speed * delta / 1000.0, -self.speed * delta / 1000.0)
		if self.rect.left <= screen_rect.left:
			self.velx = 1
			#~ print "[2]"
			#~ self.direction = 2
			#~ if math.sqrt((self.rect.centery - 250)**2 + (self.rect.centerx - 0)**2) >= self.rect.w / 2.0:
				#~ self.rect.move_ip(-self.speed * delta / 1000.0, self.speed * delta / 1000.0)
		if self.rect.right >= screen_rect.right:
			self.velx = -1
			#print "[3]"
			#print self.rect.x
			#print self.rect.y
			#~ print (self.speed * delta / 1000.0), ",",(self.speed * delta / 1000.0)
			#~ self.direction = 3
			#~ if math.sqrt((self.rect.centery - 250)**2 + (self.rect.centerx - 0)**2) >= self.rect.w / 2.0:
				#~ self.rect.move_ip(self.speed * delta / 1000.0, self.speed * delta / 1000.0)
		if self.velx == -1 and self.vely == -1:
			self.rect.move_ip(-2, -2)
		elif self.velx == 1 and self.vely == -1:
			self.rect.move_ip(2, -2)
		elif self.velx == -1 and self.vely == 1:
			self.rect.move_ip(-2, 2)
		else:
			self.rect.move_ip(2, 2)
		self.rect.clamp_ip(screen_rect)
	def draw(self):
		screen.blit(self.surf, self.rect, pygame.Rect(self.frame * 50, self.direction * 50, 50, 50))

class Player(Sprite):
	def __init__(self, surf):
		Sprite.__init__(self, surf)
		self.rect.width = 50
		self.rect.height = 50
		self.direction = 1 #0up 1down 2left 3right
		self.speed = 100 #pixels per sec
		self.frame = 0 #index on sheet
		self.framerate = 4
		self.framebuffer = 0
		self.isMoving = [False, False, False, False]
	def update(self, water_collision):
		if self.isMoving == [False, False, False, False]:
			self.frame = 0
		else:
			self.framebuffer = 0
			self.frame += 1
			if self.frame > 3:
				self.frame = 0
		if self.isMoving[0] == True:
			self.direction = 0
			if self.rect.move(0, -self.speed * delta/ 1000.0).collidelist(water_collision) == -1:
				self.rect.move_ip(0, -self.speed * delta/ 1000.0)
				print self.rect.x , ",", self.rect.y
		if self.isMoving[1] == True:
			self.direction = 1
			if self.rect.move(0, self.speed * delta/ 1000.0).collidelist(water_collision) == -1:
				self.rect.move_ip(0, self.speed * delta/ 1000.0)
				print self.rect.x , ",", self.rect.y
		if self.isMoving[2] == True:
			self.direction = 2
			if self.rect.move(-self.speed * delta/ 1000.0, 0).collidelist(water_collision) == -1:
				self.rect.move_ip(-self.speed * delta/ 1000.0, 0)
				print self.rect.x , ",", self.rect.y
		if self.isMoving[3] == True:
			self.direction = 3
			if self.rect.move(self.speed * delta/ 1000.0, 0).collidelist(water_collision) == -1:
				self.rect.move_ip(self.speed * delta/ 1000.0, 0)
				print self.rect.x , ",", self.rect.y
		self.rect.clamp_ip(screen_rect)
	def draw(self):
		screen.blit(self.surf, self.rect, pygame.Rect(self.frame * 50, self.direction * 50, 50, 50))

pygame.init()
screen = pygame.display.set_mode((64*20, 64 * 14))
screen_rect = screen.get_rect()
timer = pygame.time.get_ticks()
delta = 0
land = Sprite(pygame.image.load("land.png").convert())
water = Sprite(pygame.image.load("water.png").convert())
player = Player(pygame.image.load("water.png").convert_alpha())
ball = Ball(pygame.image.load("ball2.png").convert_alpha())
level1_file = open("map_file.txt")
level1 = level1_file.readlines()
level1 = [line.strip() for line in level1]
waterTileList = []
master_clock = pygame.time.Clock()

while True:
	master_clock.tick(100)
	delta = pygame.time.get_ticks() - timer
	timer = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			if event.key == pygame.K_w:
				player.isMoving[0] = True
			if event.key == pygame.K_s:
				player.isMoving[1] = True
			if event.key == pygame.K_a:
				player.isMoving[2] = True
			if event.key == pygame.K_d:
				player.isMoving[3] = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player.isMoving[0] = False
			if event.key == pygame.K_s:
				player.isMoving[1] = False
			if event.key == pygame.K_a:
				player.isMoving[2] = False
			if event.key == pygame.K_d:
				player.isMoving[3] = False
			
	
	screen.fill((0, 0, 0))
	for row in range(len(level1)):
		for column in range(len(level1[0])):
			if level1[row][column] == "g":
				screen.blit(land.surf, pygame.Rect(column * 50, row * 50, 50, 50))
			elif level1[row][column] == "w":
				screen.blit(water.surf, pygame.Rect(column * 50, row * 50, 50, 50))
				
	for row in range(len(level1)):
		for column in range(len(level1[0])):
			if level1[row][column] == "w":
				waterTileList.append(pygame.Rect(column * 50, row * 50, 50, 50))

	player.update(waterTileList)
	ball.update()
	ball.draw()
	player.draw()
	
	
	pygame.display.flip()
