## @file keese.py
# @title Keese Enemy
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import random

from .enemy import *
from .constants import *
from .spritesheet import *
from .item import *
from config.window import *

SPRITE_MAP = 'src/actor/sprites/keese.png'

## @brief This class represents the Keese enemy
class Keese(Enemy):

    ## @brief Constructor for Keese
    #  @details Constructor takes two parameters, the x and y coordinates
    #  @param x X coordinate of the starting postion of the Keese
    #  @param y Y coordinate of the starting postion of the Keese
    def __init__(self, x, y):
        
        # Call superclass constructor
        Enemy.__init__(self,x,y)

        ## Whether the Keese is moving
        self.isMoving = False
        ## Whether the Keese can stop
        self.canStop = False
        ## Whether the Keees is resting
        self.isResting = False

        ## Point the Keese is traveling to
        self.travelPoint = [0,0]
        ## The amount of frames the Keese will rest for
        self.restTime = 0
        ## The frame the Keese starts resting
        self.restStartFrame = 0
        ## The frame the Keese starts flying on
        self.flyStartFrame = 0
        ## The sprite list index
        self.spriteIndex = 0

        ## Keese max health
        self.maxHP = KEESE_MAX_HP
        ## Keese current health
        self.HP = KEESE_MAX_HP

        ## Keese damage
        self.dmg = KEESE_DMG

        # Load the sprite sheet
        try:
            sheet = pygame.image.load(SPRITE_MAP).convert_alpha()
            ## Keese current sprite
            self.image = pygame.transform.scale(sheet, (32,32))
            self.image.set_colorkey(BLACK)
            
            ## Keese sprite list
            self.sprites = populateSprites()
            ## Set Keese starting sprite
            self.image = self.sprites[0]
        except pygame.error as message:
            print("image did not load")

        ## The current x-directional speed for Keese in movement/stationary state.
        self.xSpeed = 0
        ## The current y-directional speed for Keese in movement/stationary state.
        self.ySpeed = 0
        ## Integer value representing the buffer for the number of hits for Keese after being hit by player character.
        self.hitCount = 0
        ## Represents the current state if Keese has collided with player character attack.
        self.isHit = False

    
    ## @brief Sets the Keese rest length
    #  @details Generates a random number between [1,2] inclusive as the
    #  rest time between movements and sets the rest start frame to the
    #  current frame
    def genRestLength(self):

        self.restTime = random.randint(1,2)
        self.restStartFrame = self.frameCounter        

    ## @brief Creates a new travel point for Keese
    #  @details Generate a random point to move to between 0 an the width - 30
    #  of the screen for the x coordinate and between 0 and the height - 30 of
    #  the screen for the y coordinate
    def genTravelPoint(self):
    
        flag = True

        # Will only generate points that are not the current point and points that are a certain magnitude away for more seemless movement
        while(flag):
            flag = False

            x = random.randint(0, Wwidth - 30)
            y = random.randint(Y_OFFSET , Wheight - 30)

            if (x == self.rect.x or y == self.rect.y):
                flag = True

            # Calculate magnitude of movement, if less than threshold choose new one
            magnitude = (abs(x - self.rect.x)**2 + abs(y - self.rect.y)**2)**(1/2)

            if (magnitude < KEESE_MAGNITUDE_MIN):
                flag = True

        self.travelPoint = [x, y]

    ## @brief Iterates through the sprite list
    #  @details Swaps between the two sprites that are avalible for the keese
    def switchSprite(self):
        if (self.spriteIndex == 0):
            self.spriteIndex = 1
        else:
            self.spriteIndex = 0

    ## @brief Stops the Keese
    #  @details Sets the Keese speed in the x direction and the y direction to zero
    def stop(self):

        self.xSpeed = 0
        self.ySpeed = 0

    ## @brief Sets the Keese x and y movement speed
    #  @details Compares the two lengths of travel (x and y) and sets the speed
    #  in which ever direction is longer to the max speed and the other to a
    #  scalar multiple of the max speed based on the ratio of the two lengths
    def setMoveSpeed(self):
        
        yDistance = self.travelPoint[1] - self.rect.y
        xDistance = self.travelPoint[0] - self.rect.x

        # If the x distance is longer, make x direction the max speed, and set y porpotional to x
        if (abs(xDistance) > abs(yDistance)):
            self.xSpeed = KEESE_MAX_SPEED
            self.ySpeed = (yDistance / xDistance) * self.xSpeed
        elif (abs(xDistance) < abs(yDistance)):
            self.ySpeed = KEESE_MAX_SPEED
            self.xSpeed = (xDistance / yDistance) * self.ySpeed
        else:
            self.xSpeed = KEESE_MAX_SPEED
            self.ySpeed = KEESE_MAX_SPEED

        # Check to see if any speeds are below the minimum, if so set them to the minimum
        if (abs(self.xSpeed) < KEESE_MIN_SPEED):
            self.xSpeed = KEESE_MIN_SPEED
        
        if (abs(self.ySpeed) < KEESE_MIN_SPEED):
            self.ySpeed = KEESE_MIN_SPEED

        # Set the direction (Positive = down, right | Negative = up, left)
        if (xDistance < 0):
            self.xSpeed = -1 * abs(self.xSpeed)
        else:
            self.xSpeed = abs(self.xSpeed)

        if (yDistance < 0):
            self.ySpeed = -1 * abs(self.ySpeed)
        else:
            self.ySpeed = abs(self.ySpeed)

    ## @brief Evaluates the state of the Keese
    #  @details Evalautes if the Keese if moving, if it can stop, if it is in 
    #  iframes, and if it has died
    def checkState(self):
        audio_track1 = "src/sound/soundfx/enemy-die.wav"
        pygame.mixer.pre_init(32000, -16, 2 , 512)
        pygame.mixer.init()
        # Check for movement
        if (self.xSpeed != 0 or self.ySpeed != 0):
            self.isMoving = True
        else:
            self.isMoving = False

        # Check if stop conitions are met
        if ((abs(self.travelPoint[0] - self.rect.x) < ACCEPTABLE_RADIUS) or ((abs(self.travelPoint[1] - self.rect.y)) < ACCEPTABLE_RADIUS)):
            self.canStop = True
        else: self.canStop = False

        # Count down hit i-frames
        if (self.isHit):
            self.hitCount -= 1
            if(self.hitCount == 0):
                self.isHit = False

        # Check for death
        if (self.HP <= 0):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track1))
            newi = Item(self.rect.x, self.rect.y, random.randint(0, 1))
            self.groups()[0].add(newi)
            self.groups()[1].add(newi)
            self.kill()

    ## @brief Controls Keese logic
    #  @details Uses the states to control the Keese
    def enemyLogic(self):

        # While moving swap between the two sprites
        if (self.isMoving):

            flyFrameLength = self.frameCounter - self.flyStartFrame
            
            if (flyFrameLength <= 60):
                if (flyFrameLength % 12 == 0):
                    self.switchSprite() 
            else:
                if (flyFrameLength % 8 == 0):
                    self.switchSprite()

            self.image = self.sprites[self.spriteIndex]
        # While resting it will use the sitting sprite
        else:
            self.image = self.sprites[1]

        if self.isResting:
            if ( (self.frameCounter - self.restStartFrame) == self.restTime * 60): # 60 being the frames per second
                self.isResting = False
                self.genTravelPoint()
                self.setMoveSpeed()
        else:
            if not self.isMoving:
                self.genTravelPoint()
                self.setMoveSpeed()
                self.flyStartFrame = self.frameCounter
            # Movement Logic
            if self.canStop:
                self.stop()
                self.genRestLength()
                self.isResting = True
                
## @brief Creates the sprite list for Keese
#  @details Iterates through a sprite sheet to pull images for the sprite array
#  @return sprites Array if the sprites that represent the Keese       
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
