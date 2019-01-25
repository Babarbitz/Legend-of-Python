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

#Sprite for the menu_sprite objects
menu_sprite = pygame.sprite.Sprite()
#Make list of all sprites to be printed at the menu.
menulist = pygame.sprite.Group()
#Make list of all printed sprites in game
spritelist = pygame.sprite.Group()
#Make list of all player-collidable objects
collidlist = pygame.sprite.Group()
#Make list of all updating sprites
updatelist = pygame.sprite.Group()
#Permanent list for drawing
hudlist = pygame.sprite.Group()
#Global clock for refresh rate for each window.
clock = pygame.time.Clock()

winState = False

#Add to list
def ATL(elem, a, b, c):
    if(a):
        spritelist.add(elem)
    if(b):
        collidlist.add(elem)
    if(c):
        updatelist.add(elem)

def empty_sprites():
    menulist.empty()
    spritelist.empty()
    collidlist.empty()
    updatelist.empty()
    hudlist.empty()

def game_state():
    #Initial Draw Function
    pygame.init()
    window = pygame.display.set_mode([Wwidth, Wheight])

    LVMNG = LevelManager(spritelist, collidlist, updatelist)
    LVMNG.make(2, 5)
    text = Render_Font(5, 5, "L-2",16,WHITE)
    hudlist.add(text)

    # Main run loop
    run = True

    while run:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return True

           # Key pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_1:
                    empty_sprites()
                    LVMNG.make(1,5)
                    text = Render_Font(5, 5, "L-1",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_2:
                    empty_sprites()
                    LVMNG.make(2,5)
                    text = Render_Font(5, 5, "L-2",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_3:
                    empty_sprites()
                    LVMNG.make(3,5)
                    text = Render_Font(5, 5, "L-3",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_4:
                    empty_sprites()
                    LVMNG.make(2,4)
                    text = Render_Font(5, 5, "L-4",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_5:
                    empty_sprites()
                    LVMNG.make(1,3)
                    text = Render_Font(5, 5, "L-5",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_6:
                    empty_sprites()
                    LVMNG.make(2,3)
                    text = Render_Font(5, 5, "L-6",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_7:
                    empty_sprites()
                    LVMNG.make(3,3)
                    text = Render_Font(5, 5, "L-7",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_8:
                    empty_sprites()
                    LVMNG.make(0,2)
                    text = Render_Font(5, 5, "L-8",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_9:
                    empty_sprites()
                    LVMNG.make(1,2)
                    text = Render_Font(5, 5, "L-9",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_0:
                    empty_sprites()
                    LVMNG.make(2,2)
                    text = Render_Font(5, 5, "L-10",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_q:
                    empty_sprites()
                    LVMNG.make(3,2)
                    text = Render_Font(5, 5, "L-11",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_w:
                    empty_sprites()
                    LVMNG.make(4,2)
                    text = Render_Font(5, 5, "L-12",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_e:
                    empty_sprites()
                    LVMNG.make(2,1)
                    text = Render_Font(5, 5, "L-13",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_r:
                    empty_sprites()
                    LVMNG.make(4,1)
                    text = Render_Font(5, 5, "L-14",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_t:
                    empty_sprites()
                    LVMNG.make(5,1)
                    text = Render_Font(5, 5, "L-15",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_y:
                    empty_sprites()
                    LVMNG.make(1,0)
                    text = Render_Font(5, 5, "L-16",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_u:
                    empty_sprites()
                    LVMNG.make(2,0)
                    text = Render_Font(5, 5, "L-17",16,WHITE)
                    hudlist.add(text)
                elif event.key == pygame.K_i:
                    empty_sprites()
                    LVMNG.make(3,0)
                    text = Render_Font(5, 5, "L-0",16,WHITE)
                    hudlist.add(text)

        updatelist.update()
        window.fill(BLACK)
        spritelist.draw(window)
        hudlist.draw(window)

        # Translate screen to window
        pygame.display.flip()
        
        # Framerate
        clock.tick(60)

    return False

# Main Loop handling game_states
def main():
    while(True):
        if (game_state()):
            break
    
    print("Manual Test exit success")

if __name__=="__main__":
    main()
