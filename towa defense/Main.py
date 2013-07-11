import sys, pygame, Level, Gui, Entity
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (160,120)
#Start Graphics
pygame.init()

#Screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960))
screen_rect = screen.get_rect()
#Booleans
startButtonClicked = False
pauseMenuButton = False
spawning = True
buying = [False, False, False]
#Ints
playerHealthCount = 100
#Entities
towers = Entity.spawnTowers()
waves = Entity.Waves()
#Menu Stuff
menu = Gui.Menu("images/Pause Menu.png")
startMenu = Gui.Menu("images/Start Screen/Start Screen.png")
IntestinesBackground = Level.Sprite("images/Level1 Background.png")
while True:
    while startButtonClicked == False:
        #main menu code
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if startMenu.startScreenStartButton.rect.collidepoint(pygame.mouse.get_pos()):
                    startButtonClicked = True
                elif startMenu.startScreenQuitButton.rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
        startMenu.drawStartMenu(screen)
        pygame.display.flip()
    while startButtonClicked == True and playerHealthCount > 0:
        clock.tick(60)
        paused = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pauseMenuButton == False:
                if event.button == 1:
                    if menu.menuButton.rect.collidepoint(pygame.mouse.get_pos()):
                        pauseMenuButton = True
                    if buying[0] == True:
                        towers.spawn(screen, 1)
                        buying[0] = False
                    if menu.aminoAcidTile.rect.collidepoint(pygame.mouse.get_pos()):
                        buying[0] = True
                    if buying[1] == True:
                        towers.spawn(screen, 2)
                        buying[1] = False
                    if menu.antibodyTile.rect.collidepoint(pygame.mouse.get_pos()):
                        buying[1] = True
                    if buying[2] == True:
                        towers.spawn(screen, 3)
                        buying[2] = False
                    if menu.lymphocyteTile.rect.collidepoint(pygame.mouse.get_pos()):
                        buying[2] = True
                if event.button == 2:
                    print "Info on Tower"
                if event.button == 3:
                    print "Upgrade Tower"
            elif event.type == pygame.MOUSEBUTTONDOWN and pauseMenuButton == True:
                if menu.resumeButton.rect.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    pauseMenuButton = False
                    print "Resume"
                elif menu.quitButton.rect.collidepoint(pygame.mouse.get_pos()):
                    startButtonClicked = False
                    pauseMenuButton = False
                    paused = False
                    playerHealthCount = 100
                    for i in range(len(Entity.minions)):
                        Entity.minions[i].isAlive = False
                    Entity.minions = []
                elif menu.soundButton.rect.collidepoint(pygame.mouse.get_pos()):
                    menu.soundOnOff = -menu.soundOnOff
                elif menu.musicButton.rect.collidepoint(pygame.mouse.get_pos()):
                    menu.musicOnOff = -menu.musicOnOff
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and pauseMenuButton == False:
                    pauseMenuButton = True
                    paused = True
                    enemy_spawner.spawn(Entity.minions, screen, paused)
                elif event.key == pygame.K_ESCAPE and pauseMenuButton == True:
                    pauseMenuButton = False
                    paused = False
            if startButtonClicked == True and pauseMenuButton == True:
                #Pause Menu Code
                pass
        if pauseMenuButton == False:
            screen.blit(IntestinesBackground.surf,IntestinesBackground.rect)
            Level.drawLevelOne(screen)
            if spawning:
                waves.startWave()
                for i in range(len(Entity.minions)):
                    enemy_spawner = Entity.Spawner(Entity.minions, Level.spawn_dict[1])
                spawning = False
            if spawning == False:
                if len([enemy for enemy in Entity.minions if enemy.isAlive == True]) == 0:
                    spawning = True
            enemy_spawner.spawn(Entity.minions, screen, paused)
            for i in range(len(Entity.minions)):
                if Entity.minions[i].isActive:
                    if Entity.minions[i].rect.x >= 960:
                        if playerHealthCount > 1:
                            playerHealthCount -= 1
                        else:
                            startButtonClicked = False
                            pauseMenuButton = False
                            playerHealthCount = 100
                        Entity.minions[i].selfDestruct(i)
                        break
                    Entity.minions[i].update()
                    Entity.minions[i].draw(screen)
            for i in range(len(Entity.playerTowers)):
                Entity.playerTowers[i].draw(screen)
            menu.drawInterface(screen,playerHealthCount)  
        elif pauseMenuButton == True:
            #if justPaused == True:
            screen.blit(IntestinesBackground.surf,IntestinesBackground.rect)
            Level.drawLevelOne(screen)
            menu.drawInterface(screen,playerHealthCount)
            menu.drawPauseMenu(screen)
            
        pygame.display.flip()
