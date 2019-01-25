## @file stalfos.py
# @title Stalfos Enemy
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018
import random

from .enemy import *
from .constants import *
from .spritesheet import *
from .item import *

SPRITE_MAP = 'src/actor/sprites/stalfos.png'

## @brief This class represents the Stalfos enemy
class Stalfos(Enemy):

    ## @brief Constructor for Stalfos
    #  @details Constructor takes two parameters, the x and y coordinates
    #  @param x X coordinate of the starting postion of the Keese
    #  @param y Y coordinate of the starting postion of the Keese
    def __init__(self, x, y):

        ## Call superclass constructor
        Enemy.__init__(self, x, y)

        ## Boolean values for keeping track of the Stalfos state.
        self.isMoving = False

        ## Movement integer value for previous direction of movement for Stalfos state.
        self.previousDirection = 0
        ## Movement integer value for current direction of movement for Stalfos state.
        self.direction = 0
        ## Integer representing the frames walked by Staflos in movement state.
        self.walkFrames = 0
        ## Integer value for movement frame for Stalfos during movement state.
        self.walkStartFrame = 0
        ## This represents the previous x-location of Stalfos in movement/stationary  state.
        self.oldx = self.rect.x
        ## This represents the previous y-location of Stalfos in movement/stationary  state.
        self.oldy = self.rect.y

        ## This represents the list of objects Stalfos can collide with, in movement/stationary state.
        self.obj = None

        ## The integer value setting the Stalfos health to maximum health.
        self.maxHP = STALFOS_MAX_HP
        ## The integer value representing Current Stalfos health.
        self.HP = STALFOS_MAX_HP

        ## The integer value representing the current damage value that the Stalfos object has received from player character.
        self.dmg = STALFOS_DMG

        try:
            ## Spritesheet for the acessing of the Stalfos sprite image.
            sheet = pygame.image.load(SPRITE_MAP).convert_alpha()
            ## Sprite image for the Stalfos object.
            self.image = pygame.transform.scale(sheet, (32,32))
            self.image.set_colorkey(BLACK)
            
            ## Creates a list of sprites list for Stalfos.
            self.sprites = populateSprites()
            ## Set Stalfos starting sprite
            self.image = self.sprites[0]
        except pygame.error as message:
            print("image did not load")

        ## Represents the integer value for the current index in the sprite list for Stalfos.
        self.spriteIndex = 0
        ## Represents the integer value (0,1,2,3) direction Stalfos is hit in by player character attack.
        self.hitdir = 0
        ## Integer value representing the buffer for the number of hits for the Enemy after being hit by player character.
        self.hitCount = 0
       

# If collides it stops moving

# If isMoving == False
# set xspeed and yspeed to 0

# Movement: pick a direction, pick a distance, move, stop, repeat


    ## @brief Evaluates the state of the Stalfos
    #  @details Evalautes if the Stalfos if moving, if it can stop, if it is in 
    #  iframes, if it collides with something, and if it has died
    def checkState(self):
        audio_track1 = "src/sound/soundfx/enemy-die.wav"
        pygame.mixer.pre_init(32000, -16, 2 , 512)
        pygame.mixer.init()
        ## Check for movement
        if (self.xSpeed != 0 or self.ySpeed != 0):
            self.isMoving = True
        else:
            self.isMoving = False
        
        # Check if stop conitions are met
        framesWalked = self.frameCounter - self.walkStartFrame

        if (framesWalked == self.walkFrames):
            isMoving = False
            self.stop()

        # Count down hit i-frames
        if (self.isHit):
            
            self.hitCount -= 1
            if(self.hitCount > 20):
                if(self.hitdir == 2):
                    self.rect.x += STALFOS_HIT_SPEED
                elif(self.hitdir == 3):
                    self.rect.y += STALFOS_HIT_SPEED
                elif(self.hitdir == 0):
                    self.rect.x -= STALFOS_HIT_SPEED
                elif(self.hitdir == 1):
                    self.rect.y -= STALFOS_HIT_SPEED
            if(self.hitCount == 0):
                ## Represents the current state if Stalfos has collided with player character attack.
                self.isHit = False

        collision = pygame.sprite.spritecollide(self, self.obj, False)
        for i in collision:
            # Wall collision
            if (i.id == "W" or i.id == "D"):
                # Put user at the edge of the wall the hit
                i.collision(self)
                self.isMoving = False
                self.stop()

        # Check for death
        if (self.HP <= 0):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track1))
            newi = Item(self.rect.x, self.rect.y, random.randint(0, 1))
            self.groups()[0].add(newi)
            self.groups()[1].add(newi)
            self.kill()

    ## @brief Controls Stalfos logic
    #  @details Uses the states to control the Stalfos
    def enemyLogic(self):
        
        self.oldx = self.rect.x
        self.oldy = self.rect.y

        if not self.isMoving:
            self.stop()
            self.genTravelPath()
            self.setWalkSpeed()
            self.walkStartFrame = self.frameCounter


        # While moving swap between the two sprites
        if (self.isMoving):
            if (self.frameCounter % 8 == 0):
                if (self.spriteIndex == 1):
                    self.spriteIndex = 0
                else:
                    self.spriteIndex = 1
        
            self.image = self.sprites[self.spriteIndex]
        # While resting it will use the sitting sprite
        else:
            self.image = self.sprites[1]

        if(self.isHit):
            if(self.hitCount%2 == 0):
                self.image = pygame.Surface([0,0])

    ## @brief Creates a new travel point for Stalfos
    #  @details Generates a direction to walk and the distance to move
    def genTravelPath(self):
        
        self.previousDirection = self.direction

        flag = True

        while(flag):
            
            flag = False

            self.direction = random.randint(0, 3)
            self.walkFrames = 60 * random.randint(1,3) 

            if (self.direction == self.previousDirection):
                flag = True

    ## @brief Sets the walk speed of the Stalfos
    #  @details Sets speed based on the direction
    def setWalkSpeed(self):

        if (self.direction == 0):
            self.xSpeed = -STALFOS_SPEED
        elif (self.direction == 1):
            self.xSpeed = STALFOS_SPEED
        elif (self.direction == 2):
            self.ySpeed = STALFOS_SPEED
        else:
            self.ySpeed = -STALFOS_SPEED
    
    ## @brief Stops the Stalfos
    #  @details Sets the Stalfos speed in the x direction and the y direction to zero
    def stop(self):
        ## The current x-directional speed for Stalfos in movement/stationary state.
        self.xSpeed = 0
        ## The current y-directional speed for Stalfos in movement/stationary state.
        self.ySpeed = 0

## @brief Creates the sprite list for Stalfos
#  @details Iterates through a sprite sheet to pull images for the sprite array
#  @return sprites Array if the sprites that represent the Stalfos    
def populateSprites():
    
    # Create empty sprite list
    sprites = []
    
    # Load sprite sheet
    sheet = SpriteSheet(SPRITE_MAP)

    # Populate spritelist
    sprite = sheet.get_image(0, 0, 32, 32)
    sprites.append(sprite)
    
    sprite = sheet.get_image(32, 0, 32, 32)
    sprites.append(sprite)

    return sprites