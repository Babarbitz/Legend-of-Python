## @file block.py
# @title Block Class
# @author Lucas Zacharewicz
# @date November 21 2018


import pygame
from config.window import *
from actor.constants import *
from actor.spritesheet import *

## @brief This class represents the Block class for collision for objects in the environment.
class Block(pygame.sprite.Sprite):
    ## @brief Constructor for the Block class.
    # @detail Constructor for Block class initializes a block object based on the x/y location of the wall, and the sprite the collision for the wall will be created upon.
    # @param x This represents the integer value for the x-location for the Block object to be created.
    # @param y This represents the integer value for the y-location for the Block object to be created.
    # @param sprite This represents the sprite that the collision for a Block will be present upon at all times.
    def __init__(self, x, y, sprite):
        # Parent constructor
        super().__init__()

        ## Forces block size to be 32 x 32
        self.image = pygame.Surface([32, 32])

        # Load the sprite sheet
        sheet = pygame.image.load(sprite).convert_alpha()
        ## block current sprite
        self.image = pygame.transform.scale(sheet, (32,32))
        self.image.set_colorkey(BLACK)

        self.image = populate(sprite)

        # Top left corner holds the x and y
        ## This represents rectangle for position for the sprite image of the Block object.
        self.rect = self.image.get_rect()
        self.rect.y = y + Y_OFFSET
        self.rect.x = x

        # Collision ID
        ## This represents the ID for the block object, used for collision in __main.py__.
        self.id = "W"

    ## @brief This method checks for collision with the Block object and other sprite object.
    #  @detail The collision will be checked with the Block and other sprite object as the object collides with the block.
    #  @param i This is the sprite object that is passed into the method, and checks if the object is colliding with the block object, reseting the sprite objects location accordingly.
    def collision(self, i):
        if(i.oldx + i.rect.width <= self.rect.x):
            i.rect.x = self.rect.x - i.rect.width
        elif(i.oldx >= self.rect.x + self.rect.width):
            i.rect.x = self.rect.x + self.rect.width
        elif(i.oldy + i.rect.height <= self.rect.y):
            i.rect.y = self.rect.y - i.rect.height
        elif(i.oldy >= self.rect.y + self.rect.height):
            i.rect.y = self.rect.y + self.rect.height

## @brief Opens the sprite for the object
#  @details Opens and loads the sprite for the block
#  @param map The spritemap to load from
#  @return Sprite for the block
def populate(map):
    
    # Load sprite sheet
    sheet = SpriteSheet(map)

    # Populate spritelist
    sprite = sheet.get_image(0, 0, 32, 32)

    return sprite
