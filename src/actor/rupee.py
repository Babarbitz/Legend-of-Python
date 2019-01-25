## @file rupee.py
# @title Rupee_Bar Class
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018
import pygame
from .constants import *
from .spritesheet import SpriteSheet

## @brief This class represents the RupeeBar object.
# @detail The Rupee class uses the Pygame library and SpriteSheet module to create an image for the 
class Rupee_Bar(pygame.sprite.Sprite):
    ## @brief Constructor for the RupeeBar object.
    # @detail Constructor for class initializes the x and y location of the RupeeBar object.
    # @param x this represents the x-coordinate at which the RupeeBar object will be drawn.
    # @param y this represents the y-coordinate at which the RupeehBar object will be drawn.
    def __init__(self, x, y):
        super().__init__()

        item_path = 'src/actor/sprites/items2.png'
        sheet = pygame.image.load(item_path).convert_alpha()
    
        item_sheet = SpriteSheet(item_path)
        ## This represents the sprite image of the Rupee_Bar object.
        self.image = pygame.transform.scale(sheet, (20, 15))
        self.image.set_colorkey(BLACK)
        self.image = item_sheet.get_image(32, 0, 32, 32)
        

        # Top left corner holds the x and y
        ## This represents rectangle for collision and position for the sprite image of the Rupee_Bar object.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    

   
