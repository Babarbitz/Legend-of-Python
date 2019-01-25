## @file __main__.py
# @title Main Game Running File
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date December 4 2018

import pygame

from actor.player import *
from actor.healthbar import *
from actor.rupee import *
from actor.keys import*
from actor.constants import *
from config.colour import *
from config.window import *
from collision.levelmanager import *
from actor.renderfont import *
from time import *
from collision.leveldata import *

## Sprite for the menu_sprite objects
menu_sprite = pygame.sprite.Sprite()
## Make list of all sprites to be printed at the menu.
menulist = pygame.sprite.Group()
## Make list of all printed sprites in game
spritelist = pygame.sprite.Group()
## Make list of all player-collidable objects
collidlist = pygame.sprite.Group()
## Make list of all updating sprites
updatelist = pygame.sprite.Group()
## Permanent list for drawing
hudlist = pygame.sprite.Group()
## Global clock for refresh rate for each window.
clock = pygame.time.Clock()

winState = False

## @brief Function to add an element to the sprite/collision/update list
# @param elem Element to be added to the lists
# @param a Boolean on whether to add elem to sprite list
# @param b Boolean on whether to add elem to collision list
# @param c Boolean on whether to add elem to update list
def ATL(elem, a, b, c):
    if(a):
        spritelist.add(elem)
    if(b):
        collidlist.add(elem)
    if(c):
        updatelist.add(elem)

## @brief Function to empty all object lists in main loop (sprite, collide, update, hud)
def empty_sprites():
    menulist.empty()
    spritelist.empty()
    collidlist.empty()
    updatelist.empty()
    hudlist.empty()


## @brief In-game state function
# @detail This function acts whenever the user is in game, controlling the player and navigating the dungeon. It plays the background audio,
# loads all the assests, and loops to update all objects and constantly print them on screen
def game_state():
    #Initial Draw Function
    audio_track1 = "src/sound/music/dungeon.mp3"
    audio_track2 = "src/sound/soundfx/link-die.wav"
    pygame.mixer.pre_init(44100, -16, 3, 512)
    pygame.mixer.init()
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])
    #MakeLevel([True, True, True, True], [], [[100,200+Y_OFFSET,'S'],[400, 200+Y_OFFSET, 'K'], [200, 200+Y_OFFSET, 'K'], [300,200+Y_OFFSET, 'K']],[], spritelist, collidlist, updatelist)
    rupeebar = Rupee_Bar(Wwidth/3,20)
    hudlist.add(rupeebar)
    #MakeLevel([True, True, True, True], [], [[100,200,'S'],[400, 200, 'K'], [200, 200, 'K'], [300,200, 'K']], [300, 200, 'A'],spritelist, collidlist, updatelist)

    LVMNG = LevelManager(spritelist, collidlist, updatelist)
    LVMNG.make(2, 5)

    Rupee_Count = Render_Font(Wwidth/3 + 30,30, "x 0",12,WHITE)
    hudlist.add(Rupee_Count)
    Keys_Count = Render_Font(Wwidth/2 + 130,30, "x 0",12,WHITE)
    hudlist.add(Keys_Count)



    healthbar = Health_Bar(10,20)
    hudlist.add(healthbar)

    keysbar = Keys_Bar(Wwidth-140, 20)
    hudlist.add(keysbar)

    Life_Font = Render_Font(15,6, "-LIFE-",14,(255, 0, 0))
    hudlist.add(Life_Font)

    Rupee_Font = Render_Font(Wwidth/3 + 25,8, "-RUPEES-",12,(124, 0, 255))
    hudlist.add(Rupee_Font)
  
    Keys_Font = Render_Font(Wwidth-120,5, "-KEYS-", 14,PURPLE)
    hudlist.add(Keys_Font)


    #Make player, and set obj list to collidlist
    player = Player(Wwidth/2-20,Wheight/2+10, [healthbar, Rupee_Count, Keys_Count])
    player.obj = collidlist
    ATL(player, True, False, True)


    # Main run loop
    run = True
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load(audio_track1)
    pygame.mixer.music.play(loops=-1)

    while run:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

           # Key pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move(0, True)
                elif event.key == pygame.K_d:
                    player.move(2, True)
                elif event.key == pygame.K_w:
                    player.move(1, True)
                elif event.key == pygame.K_s:
                    player.move(3, True)
                elif event.key == pygame.K_k:
                    player.attack()
                elif event.key == pygame.K_l:
                    player.useitem()
                elif event.key == pygame.K_m:
                    pygame.mixer.music.set_volume(0)
                elif event.key == pygame.K_n:
                    pygame.mixer.music.set_volume(0.1)
                elif event.key == pygame.K_9:
                    if(player.debug):
                        player.debug = False
                        player.speed = PLAYER_SPEED
                    else:
                        player.debug = True
                        player.speed = 6
                        player.rupes = 99
                        player.rbar.updateText("x " + str(player.rupes))

            # Key let go
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.move(0, False)
                elif event.key == pygame.K_d:
                    player.move(2, False)
                elif event.key == pygame.K_w:
                    player.move(1, False)
                elif event.key == pygame.K_s:
                    player.move(3, False)
        if (player.hp <= 0):
            LVMNG.clear()
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track2))
            sleep(1.5)
            return True
        ## This is where the win screen thing is set TODO
        if (player.hasWon == True):
            global winState 
            winState = True
            return True

        # if(self.rect.x > Wwidth - 50 or self.rect.x < 18 or self.rect.y > Wheight + Y_OFFSET - 108 or self.rect.y < Y_OFFSET + 18)
        if(player.leveltrans):
            player.leveltrans = False
            player.spawning = True
            if(player.rect.x > Wwidth - 50):
                LVMNG.transition(1, 0)
                player.rect.x = 32    
            elif(player.rect.x < 18):
                LVMNG.transition(-1, 0)
                player.rect.x = Wwidth - 64
            elif(player.rect.y > Wheight + Y_OFFSET - 108):
                LVMNG.transition(0, 1)
                player.rect.y = Y_OFFSET + 32
            elif(player.rect.y < Y_OFFSET + 18):
                LVMNG.transition(0, -1)
                player.rect.y = Wheight - 64

            ATL(player, True, False, True)
        # This checks if the player is dead for death screen.
       


        if((len(LVMNG.enarray) == 0) and (len(LVMNG.boss) == 0) and (LVMNG.killed == False)):
            LVMNG.endroom()
        

        updatelist.update()
        window.fill(BLACK)
        spritelist.draw(window)
        hudlist.draw(window)

        # Translate screen to window
        pygame.display.flip()
        
        # Framerate
        clock.tick(60)

    return False



## @brief Menu state function
# @detail Function with loop to run audio, loop menu screen, and wait for the user to press K to start the game
def menu_state():
    audio_track1 = "src/sound/music/overworld.mp3"
    pygame.mixer.pre_init(48000, -16, 1, 512)
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.2)
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])

    sprite_list = []
    menu_path1 = 'src/actor/sprites/menuscreen1.png'
    menu_path2 = 'src/actor/sprites/menuscreen2.png'
    menu_path3 = 'src/actor/sprites/menuscreen3.png'
    

    menu_sheet = SpriteSheet(menu_path1)
    image = menu_sheet.get_image(0,0,480,376)
    sprite_list.append(image)

    menu_sheet = SpriteSheet(menu_path2)
    image = menu_sheet.get_image(0,0,480,376)
    sprite_list.append(image)

    menu_sheet = SpriteSheet(menu_path3)
    image = menu_sheet.get_image(0,0,480,376)
    sprite_list.append(image)
    
    menu_sprite.rect = image.get_rect()
    menu_sprite.rect.x = 0
    menu_sprite.rect.y = 0

    menulist.add(menu_sprite)
  
    pygame.mixer.music.load(audio_track1)
    pygame.mixer.music.play(loops=-1)
    i = 0
    while (True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    menulist.empty()
                    pygame.mixer.music.fadeout(400*5)
                    return True

        if(i > 2):
            i = 0
        sleep(.25)
        menu_sprite.image = sprite_list[i]

        i += 1
    
        menulist.update()
        menulist.draw(window)

        pygame.display.flip()
        clock.tick(60)
                    
## @brief Loading screen state function
# @detail This function acts on the transition from menu to in-game, allowing the game to load all needed assets
def loading_state():
   
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])
    window.fill(BLACK)

    menu_font1 = Render_Font(Wwidth/2-150, Wheight/2, "NOW LOADING...",16,WHITE)
    menulist.add(menu_font1)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
   
    menulist.update()
    menulist.draw(window)
    pygame.display.flip()
    clock.tick(60)

## @brief Death state function
# @detail This function acts once the user has died, printing a message and waiting for input to either go back into game or to quit
def death_state():
    audio_track1 = "src/sound/music/death.mp3"
    pygame.mixer.pre_init(48000, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])
    window.fill(BLACK)
    pygame.mixer.music.load(audio_track1)
    pygame.mixer.music.play()
    menu_font1 = Render_Font(Wwidth/2-90, Wheight/2-20, "You Died",20,RED)
    menu_font2 = Render_Font(Wwidth/2-13, Wheight/2+20, "or Q: QUIT GAME",14,WHITE)
    menu_font3 = Render_Font(Wwidth/2-200, Wheight/2+20, "K: MAIN MENU",14,WHITE)
    menulist.add(menu_font1)
    menulist.add(menu_font2)
    menulist.add(menu_font3)
   

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    menulist.empty()
                    empty_sprites()
                    return False
                    break
                elif event.key == pygame.K_q:
                    menulist.empty()
                    return True
                    break

        menulist.update()
        menulist.draw(window)
        pygame.display.flip()
        clock.tick(60)
    return False

## @brief Win state function
# @detail This function acts when the player gets the objective object, signifying the end of the game, printing a win screen
def win_state():
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])
    window.fill(BLACK)

    menu_font1 = Render_Font(Wwidth/2-135, Wheight/2-20, "CONGRATULATIONS!",18,BLUE)
    menu_font2 = Render_Font(Wwidth/2-80,Wheight/2 +30, "YOU WIN!",20,BLUE)
    menulist.add(menu_font1)
    menulist.add(menu_font2)
    while(True):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        return
       
        menulist.update()
        menulist.draw(window)
        pygame.display.flip()
        clock.tick(60)

## @brief Main Game Loop
# @detail This function runs all states, and transitions from state to state when needed
def main():
    while(True):
        if (menu_state()):
            loading_state()
            menulist.empty()
            if (game_state()):
                if(winState):
                    win_state()
                    break
                elif (death_state()):
                    break
            else:
                break
        else:
            break
    

    print("Game Exit Succesful!")
    pygame.quit()





if __name__=="__main__":
    main()
