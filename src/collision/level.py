## @file level.py
# @title Dungeon Background
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
from actor.spritesheet import *
from config.window import *

## @brief Dungeon level background class
# @detail Creates the background of a dungeon, can be modified in the future to change colour based on sprite sheet and new arg
class Level(pygame.sprite.Sprite):

    ## @brief Background initializer
    # @detail Initialize a background to constantly be printed as game background
    def __init__(self):
        super().__init__()
         # Make wall with given width and height, and sprite if one given
        dungeon_path = 'src/actor/sprites/dungeonsprite.png'
        sheet = pygame.image.load(dungeon_path).convert_alpha()
        dungeon_sheet = SpriteSheet(dungeon_path)

        ## Level background sprite image
        self.image = pygame.transform.scale(sheet, (480, 320))
        self.image.set_colorkey(BLACK)
        image = dungeon_sheet.get_image(0, 24, 480, 320)
        self.image = image
        # Top left corner holds the x and y
        ## Background x and y coordinates (adjusted for the HUD display)
        self.rect = self.image.get_rect()
        self.rect.y = Y_OFFSET
        self.rect.x = 0
      

#480x 320y
