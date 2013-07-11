import sys, pygame, Level, Gui, Entity

def redrawSoundButton():
    if menu.soundOnOff == 1:
            screen.blit(menu.soundButton.surf,menu.soundButton.rect,pygame.Rect(0,0,320,64))
    elif menu.soundOnOff == -1:
        screen.blit(menu.soundButton.surf,menu.soundButton.rect,pygame.Rect(320,0,320,64))
    pygame.display.flip()
#Start Graphics
pygame.init()

#Screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960))
screen_rect = screen.get_rect()
#Booleans
startButtonClicked = False
pauseMenuButton = False
justPaused = True
spawning = True
#Ints
playerHealthCount = 100

#Entities
waves = Entity.Waves()
#Menu Stuff
menu = Gui.Menu("images/Pause Menu.png")
while startButtonClicked == False:
    #main menu code
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            startButtonClicked = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.flip()
while startButtonClicked == True and playerHealthCount > 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and pauseMenuButton == False:
            if event.button == 1:
                print "Playing Game"
            if event.button == 2:
                print "Info on Tower"
            if event.button == 3:
                print "Upgrade Tower"
        elif event.type == pygame.MOUSEBUTTONDOWN and pauseMenuButton == True:
            if menu.resumeButton.rect.collidepoint(pygame.mouse.get_pos()):
                pauseMenuButton = False
                justPaused = True
                print "Resume"
            elif menu.quitButton.rect.collidepoint(pygame.mouse.get_pos()):
                sys.exit()
            elif menu.soundButton.rect.collidepoint(pygame.mouse.get_pos()):
                redrawSoundButton()
                menu.soundOnOff = -menu.soundOnOff
        if event.type == pygame.KEYDOWN:
            print pauseMenuButton
            if event.key == pygame.K_ESCAPE and pauseMenuButton == False:
                pauseMenuButton = True
                print "Pause"
            elif event.key == pygame.K_ESCAPE and pauseMenuButton == True:
                pauseMenuButton = False
                justPaused = True
                print "Resume"
        if startButtonClicked == True and pauseMenuButton == True:
            #Pause Menu Code
            pass
    if pauseMenuButton == False:
        Level.drawLevelOne()
        if spawning:
            waves.startWave()
            for i in range(len(Entity.minions)):
                enemy_spawner = Entity.Spawner(Entity.minions, Level.spawn_dict[1])
                print "calling spawn"
            spawning = False
        if spawning == False:
            if len([enemy for enemy in Entity.minions if enemy.isAlive == True]) == 0:
                spawning = True
        enemy_spawner.spawn(Entity.minions, screen)
        for i in range(len(Entity.minions)):
            if Entity.minions[i].isActive:
                Entity.minions[i].update()
                Entity.minions[i].draw(screen)
            
    elif pauseMenuButton == True:
        if justPaused == True:
            Level.drawLevelOne()
            menu.drawPauseMenu(screen)
            justPaused = False
        
    pygame.display.flip()