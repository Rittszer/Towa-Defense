import pygame, sys

class Sprite(object):
    def __init__(self, surf):
        self.surf = pygame.image.load(surf).convert_alpha()
        self.rect = self.surf.get_rect()
        #self.rect.width = 64
        #self.rect.height = 64
class Menu(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self, surf)
        self.startScreenStartButton = Sprite("images/Start Screen/Start Screen Start Button.png")
        self.startScreenQuitButton = Sprite("images/Start Screen/Start Screen Quit Button.png")
        self.healthBar = Sprite("images/healthBar.png")
        self.healthBar.rect.topleft = (1020,909)
        self.resumeButton = Sprite("images/Resume button.png")
        self.quitButton = Sprite("images/Quit button.png")
        self.soundButton = Sprite("Sprite Sheets/Sound Sheet.png")
        self.soundButton.rect.width = 320
        self.soundButton.rect.height = 64
        self.musicButton = Sprite("Sprite Sheets/Music Sheet.png")
        self.musicButton.rect.width = 320
        self.musicButton.rect.height = 64
        self.helpButton = Sprite("images/Help Button.png")
        self.interface = Sprite("images/Game Interface.png")
        self.menuButton = Sprite("images/Menu Button.png")
        self.aminoAcidTile = Sprite("images/In-Game Purchase/Amino Acid Purchase Icon.png")
        self.antibodyTile = Sprite("images/In-Game Purchase/Antibody Purchase Icon.png")
        self.lymphocyteTile = Sprite("images/In-Game Purchase/Lymphocyte Purchase Icon.png")
        self.soundOnOff = 1
        self.musicOnOff = 1
    def drawStartMenu(self,screen):
        screen.blit(self.surf,self.rect)
        self.startScreenStartButton.rect.center = (1000,620)
        self.startScreenQuitButton.rect.center = (1000,760)
        screen.blit(self.startScreenStartButton.surf,self.startScreenStartButton.rect)
        screen.blit(self.startScreenQuitButton.surf,self.startScreenQuitButton.rect)
    def drawPauseMenu(self,screen):
        screen.blit(self.surf,self.rect)
        self.resumeButton.rect.topleft = (480,192)
        self.quitButton.rect.topleft = (480,704)
        self.soundButton.rect.topleft = (480,320)
        self.musicButton.rect.topleft = (480,446)
        self.helpButton.rect.topleft = (480,576)
        screen.blit(self.helpButton.surf,self.helpButton.rect)
        screen.blit(self.resumeButton.surf,self.resumeButton.rect)
        screen.blit(self.quitButton.surf,self.quitButton.rect)
        if self.soundOnOff == 1:
            screen.blit(self.soundButton.surf,self.soundButton.rect,pygame.Rect(0,0,320,64))
        elif self.soundOnOff == -1:
            screen.blit(self.soundButton.surf,self.soundButton.rect,pygame.Rect(320,0,320,64))
        if self.musicOnOff == 1:
            screen.blit(self.musicButton.surf,self.musicButton.rect,pygame.Rect(0,0,320,64))
        elif self.musicOnOff == -1:
            screen.blit(self.musicButton.surf,self.musicButton.rect,pygame.Rect(320,0,320,64))
    def drawInterface(self,screen,health):
        screen.blit(self.interface.surf,self.interface.rect)
        screen.blit(self.healthBar.surf,self.healthBar.rect,pygame.Rect(0,0,health*2,20))
        self.menuButton.rect.center = 1120,66
        screen.blit(self.menuButton.surf,self.menuButton.rect)
        self.shopTowers(screen)

    def shopTowers(self,screen):
        self.aminoAcidTile.rect.topleft = 1045, 250
        self.antibodyTile.rect.topleft = 1045, 450
        self.lymphocyteTile.rect.topleft = 1045, 650
        screen.blit(self.aminoAcidTile.surf,self.aminoAcidTile.rect)
        screen.blit(self.antibodyTile.surf,self.antibodyTile.rect)
        screen.blit(self.lymphocyteTile.surf,self.lymphocyteTile.rect)