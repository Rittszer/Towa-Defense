import pygame

class Sprite(object):
    def __init__(self, surf):
        self.surf = pygame.image.load(surf).convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.width = 64
        self.rect.height = 64

class Waves():
    def startWave():
        self.amount_of_enemies = 10

#screen = pygame.display.set_mode((64*20, 64 * 14))

level1_file = open("level1.txt")
level1 = level1_file.readlines()
level1 = [line.strip() for line in level1]

level2_file = open("level2.txt")
level2 = level2_file.readlines()
level2 = [line.strip() for line in level2]

current_level = 0
spawn_dict = {1:(64, -64), 2:(0, 704)}

borderList = []
for row in range(len(level1)):
    for column in range(len(level1[0])):
        if level1[row][column] == "t":
                borderList.append(pygame.Rect(column * 64, row * 64, 64, 64))
def drawLevelOne(screen):
    current_level = 1
    land = Sprite("images/land.png")
    water = Sprite("images/water.png")
    IntestinesCorner1 = Sprite("images/Intestines Corner 1.png") #V
    IntestinesCorner2 = Sprite("images/Intestines Corner 2.png") #Z
    IntestinesCorner3 = Sprite("images/Intestines Corner 3.png") #C
    IntestinesCorner4 = Sprite("images/Intestines Corner 4.png") #X
    IntestinesLR = Sprite("images/Intestines Straight 2.png")
    IntestinesUD = Sprite("images/Intestines Straight 1.png")
    for row in range(len(level1)):
        for column in range(len(level1[0])):
            if level1[row][column] == "t":
                pass
            elif level1[row][column] == "v":
                screen.blit(IntestinesCorner1.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level1[row][column] == "z":
                screen.blit(IntestinesCorner2.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level1[row][column] == "c":
                screen.blit(IntestinesCorner3.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level1[row][column] == "x":
                screen.blit(IntestinesCorner4.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level1[row][column] == "u":
                screen.blit(IntestinesUD.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level1[row][column] == "s":
                screen.blit(IntestinesLR.surf, pygame.Rect(column * 64, row * 64, 64, 64))
def drawLevelTwo():
    current_level = 2
    for row in range(len(level2)):
        for column in range(len(level2[0])):
            if level2[row][column] == "p":
                screen.blit(land.surf, pygame.Rect(column * 64, row * 64, 64, 64))
            elif level2[row][column] == "t":
                screen.blit(water.surf, pygame.Rect(column * 64, row * 64, 64, 64))
                borderList.append(pygame.Rect(column * 64, row * 64, 64, 64))