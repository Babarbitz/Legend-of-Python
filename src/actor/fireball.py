## @file fireball.py
# @title Fireball object
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
from .constants import *
from .spritesheet import SpriteSheet

SPRITE_MAP = 'src/actor/sprites/fireball.png'

## @brief This class represents the Fireball object
class Fireball(pygame.sprite.Sprite):

    ## @brief Constructor for Fireball
    #  @details Constructor takes four parameters, the x and y coordinates and 
    #  the x and y speeds
    #  @param x X coordinate of the starting postion of the Fireball
    #  @param y Y coordinate of the starting postion of the Fireball
    #  @param xSpeed The speed in the x direction of the Fireball
    #  @param ySpeed The speed in the y direction of the Fireball
    def __init__(self, x, y, xSpeed, ySpeed):
        
        # Call superclass constructor
        super().__init__()

        ## Fireball surface
        self.image = pygame.Surface([16, 32])

        ## Rectangle that represents the fireball
        self.rect = self.image.get_rect()
        ## Fireball x postion
        self.rect.x = x
        ## Fireball y positon
        self.rect.y = y

        ## Fireball ID type
        self.id = "E"

        ## Wether the fireball is hit
        self.isHit = False

        # Set fireball stats
        ## Fireball damage
        self.dmg = FIREBALL_DMG

        ## Fireball hit frames
        self.hitCount = 0

        ## Fireball speed in the x direction
        self.xSpeed = xSpeed
        ## Fireball speed in the y direction
        self.ySpeed = ySpeed

        ## Total number of frames fireball is alive
        self.frameCounter = 0

        try:
            # Load the sprite sheet
            sheet = pygame.image.load(SPRITE_MAP).convert_alpha()
            ## Fireball current sprite
            self.image = pygame.transform.scale(sheet, (16,20))
            self.image.set_colorkey(BLACK)
            self.sprites = populateSprites()
        except pygame.error as message:
            print("image did not load")

        ## Fireball collision list
        self.obj = None

        ## Sprite list index
        self.spriteIndex = 0
    
    ## @brief Starts the Fireball's movement
    #  @details Sets the x and y postions and x and y speeds for Fireball
    #  @param x X coordinate of where the Fireball is placed
    #  @param y Y coordinate of where the Fireball is placed
    #  @param xs The speed in the x direction of the Fireball
    #  @param ys The speed in the y direction of the Fireball
    def start(self, x, y, xs, ys):
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = xs
        self.ySpeed = ys

    ## @brief Ends the Fireball's movement
    #  @details Sets the x and y speed to 0 and places the Fireball of screen
    def end(self):
        self.rect.x = -1000
        self.rect.y = -1000
        self.xSpeed = 0
        self.ySpeed = 0

    ## @brief Empty function for being hit by player
    #  @details Needs to exist for when player sword collides with Fireball
    def hit(self, dir):
        pass

    ## @brief Evaluates the state of the Fireball
    #  @details Checks for collision with walls, doors, and players
    def checkState(self):
        
        # Check for collision
        collision = pygame.sprite.spritecollide(self, self.obj, False)
        for i in collision:
            # Wall collision
            if (i.id == "W" or i.id == "D" or i.id == "P"):
                self.end()

    ## @brief Moves the Fireball
    #  @details Adds the x speed and y speed to the x and y postion of the 
    #  Fireball
    def move(self):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    ## @brief Updates the Fireball sprite
    #  @details Swaps between the 2 sprites every 15 frames
    def logic(self):
        if (self.frameCounter % 15 == 0):
            if self.spriteIndex == 0:
                self.spriteIndex = 1
            else:
                self.spriteIndex = 0
            self.image = self.sprites[self.spriteIndex]

    ## @breif Updates the Fireball every frame
    #  @details Checks the state, applies the logic, and then moves the Fireball
    def update(self):
        self.checkState()
        self.logic()
        self.move()
        self.frameCounter += 1

## @brief Creates the sprite list for Fireball
#  @details Iterates through a sprite sheet to pull images for the sprite array
#  @return sprites Array if the sprites that represent the Fireball 
def populateSprites():
    try:
        # Create empty sprite list
        sprites = []
        
        # Load sprite sheet
        sheet = SpriteSheet(SPRITE_MAP)

        # Populate spritelist
        sprite = sheet.get_image(0, 0, 16, 20)
        sprites.append(sprite)
        
        sprite = sheet.get_image(16, 0, 16, 20)
        sprites.append(sprite)

        return sprites
    except pygame.error as message:
            print("image did not load")