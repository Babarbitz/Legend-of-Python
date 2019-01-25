## @file aquamentus.py
# @title Aquamentus Boss
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 8 2018

import random

from .boss import *
from .constants import *
from .fireball import *
from .spritesheet import *
from .item import *
from config.window import *

# Sets spritemap to the proper sprite file for the boss
SPRITE_MAP = 'src/actor/sprites/aquamentus.png'

## @brief This class represents the Aquamentus Boss
class Aquamentus(Boss):
    
    ## @brief Constructor for Aquamentus
    #  @details Constructor takes two parameters, the x and y coordinates
    #  @param x X coordinate of the starting postion of the Aquamentus
    #  @param y Y coordinate of the starting postion of the Aquamentus
    def __init__(self, x, y):

        # Call superclass constructor
        Boss.__init__(self, x, y)

        ## Represents wether or not the boss is attacking
        self.isAttacking = False
        ## Represents the frame that the boss starts an attack
        self.attackStartFrame = 0
        f1 = Fireball(-1000, -1000, 0, 0)
        f2 = Fireball(-1000, -1000, 0, 0)
        f3 = Fireball(-1000, -1000, 0, 0)
        ## Represents the boss' fireballs
        self.fireballs = [f1, f2, f3]

        ## Aquamentus' set x speed
        self.xSpeed = AQUAMENTUS_SPEED

        ## Aquamentus' max health
        self.maxHP = AQUAMENTUS_MAX_HP
        ## Aquamentus' current health
        self.HP = AQUAMENTUS_MAX_HP
         ## Aquamentus' damage
        self.dmg = AQUAMENTUS_DMG
        
        try:
            # Load the sprite sheet
            sheet = pygame.image.load(SPRITE_MAP).convert_alpha()
            ## Sprite image 
            self.image = pygame.transform.scale(sheet, (64, 64))
            self.image.set_colorkey(BLACK)
            ## Array of sprites
            self.sprites = populateSprites()
        except pygame.error as message:
            print("image did not load")
        ## Collision list
        self.obj = None

        ## Index for the array of sprites
        self.spriteIndex = 0
        ## Integer value representing the buffer for the number of hits for Aquamentus  after being hit by player character.
        self.hitCount = 0
        ## Represents the current state if Aquamentus has collided with player character attack.
        self.isHit = False
        ## This represents the previous x-location of Aquamentus in movement/stationary  state.
        self.oldx = self.rect.x
        ## This represents the previous y-location of Aquamentus in movement/stationary  state.
        self.oldy = self.rect.y

    ## @brief Evaluates the state of the Aquamentus
    #  @details Evalautes if Aquamentus can stop, if it is
    #  in iframes, if it collides with something, and if it has died
    def checkState(self):

        # Check for collision
        collision = pygame.sprite.spritecollide(self, self.obj, False)
        for i in collision:
            # Wall collision
            if (i.id == "W" or i.id == "D"):
                # Put user at the edge of the wall the hit
                i.collision(self)
                self.swapDirection()

        if (self.rect.x < Wwidth - 160):
            self.rect.x = Wwidth - 159
            self.swapDirection()

        if (self.frameCounter % 120 == 30):
            self.attack()
        # Count down hit i-frames
        if (self.isHit):
            self.hitCount -= 1
            if(self.hitCount == 0):
                self.isHit = False

        # Check for death
        if (self.HP <= 0):
            self.kill()

    ## @brief Swaps Aquamentus' direction
    #  @details Multiplies the speed in the x direction by -1
    def swapDirection(self):
        self.xSpeed = -1 * self.xSpeed

    ## @brief Allows for Aquamentus to attack
    #  @details Spawns fireballs at Aquamenuts' mouth and sets their move speed
    def attack(self):
        self.isAttacking = True
        self.attackStartFrame = self.frameCounter
        self.fireballs[0].start(self.rect.x, self.rect.y, -3, 0)
        self.fireballs[1].start(self.rect.x, self.rect.y, -3, -1)
        self.fireballs[2].start(self.rect.x, self.rect.y, -3, 1)

    ## @brief Controls Aquamentus logic
    #  @details Uses the states to control the Aquamentus
    def bossLogic(self):

        self.oldx = self.rect.x
        self.oldy = self.rect.y
        if self.isAttacking:
            if (self.frameCounter - self.attackStartFrame > 60):
                self.isAttacking = False

        # set sprite
        if (self.frameCounter % 25 == 0):
            if (self.spriteIndex % 2 == 0):
                self.spriteIndex = 1
            else:
                self.spriteIndex = 0

            if self.isAttacking:
                self.spriteIndex += 2
        self.image = self.sprites[self.spriteIndex]

        if(self.isHit):
            if(self.hitCount % 2 == 0):
                self.image = pygame.Surface([0, 0])

## @brief Creates the sprite list for Aquamentus
#  @details Iterates through a sprite sheet to pull images for the sprite array
#  @return sprites Array if the sprites that represent the Aquamentus 
def populateSprites():
    try:
        # Create empty sprite list
        sprites = []

        # Load sprite sheet
        sheet = SpriteSheet(SPRITE_MAP)

        # Populate spritelist
        sprite = sheet.get_image(0, 0, 64, 64)
        sprites.append(sprite)

        sprite = sheet.get_image(64, 0, 64, 64)
        sprites.append(sprite)

        sprite = sheet.get_image(128, 0, 64, 64)
        sprites.append(sprite)

        sprite = sheet.get_image(196, 0, 64, 64)
        sprites.append(sprite)

        return sprites
    except pygame.error as message:
            print("image did not load")
