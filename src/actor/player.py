## @file Player.py
# @title Playable Characer
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 6 2018

import pygame
from .constants import *
from .spritesheet import SpriteSheet
from .sword import *
from .boomerang import *
from config.window import *
import os

## @brief Player Class
# @detail A pygame sprite subclass for defining the creation of the game's playable character, as well as its interactions with both the user and other
# entities within the game
class Player(pygame.sprite.Sprite):

    ## @brief Player constructor
    # @detail The constructor for the player object, used within the initialization of the game. The only arguments passed are an initial x and y
    # position, as well as heads-up-display (HUD) elements.
    # @param x Initial player x coordinate
    # @param y Initial player y coordinate
    # @param hud Array of HUD elements which act directly with the user's tracked values (health bar, rupy/key count)
    def __init__(self, x, y, hud):
        # Parent constructor
        super().__init__()
        
        # Make an image of the sprite (can replace fill with img)
        #self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        file_path = 'src/actor/sprites/spritesheet_link2.png'
        attack_path = 'src/actor/sprites/attack_basic.png'
        
        sheet = pygame.image.load(file_path).convert_alpha()

        ## Player sprite image
        self.image = pygame.transform.scale(sheet, (32,32))
        self.image.set_colorkey(BLACK)
        # Used in collision purposes
        # P = player, W = wall, I = item

        ## Collision ID (To tell other objects what this object is)
        self.id = "P"

        ## Boolean value to tell the game when the player has left the room, and a room transition is needed
        self.leveltrans = False;
     

        ## Player x and y position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        ## Animation sprites for player walking left
        self.walkLeft = []
        ## Animation sprites for player walking right
        self.walkRight = []
        ## Animation sprites for player walking up
        self.walkUp = []
        ## Animation sprites for player walking down
        self.walkDown = []
        ## Animation sprites for player attacking
        self.attacksprite = []
        # Starting Position is Link facing Down
        # Creates a SpriteSheet Object( Class is below def update(self): function)
        sprite_sheet = SpriteSheet(file_path)
        attack_sheet = SpriteSheet(attack_path)

        
        # Grabs the sprite at the specific location specified and appends the image to the respective list

        # Down
        image = sprite_sheet.get_image(0,0,32,32)
        self.walkDown.append(image)                           
        image = sprite_sheet.get_image(32,0,32,32)
        self.walkDown.append(image)
        
        # Up                           
        image = sprite_sheet.get_image(64,0,32,32)
        self.walkUp.append(image)                         
        image = sprite_sheet.get_image(96,0,32,32)
        self.walkUp.append(image)

        # Left                          
        image = sprite_sheet.get_image(128,0,32,32)
        self.walkLeft.append(image)
        image = sprite_sheet.get_image(160,0,32,32)
        self.walkLeft.append(image)
        
        # Right
        image = sprite_sheet.get_image(224,0,32,32)
        self.walkRight.append(image)
        image = sprite_sheet.get_image(192,0,32,32)
        self.walkRight.append(image)

        # Attack (index is self.dir)
        image = attack_sheet.get_image(64, 0, 32, 32)
        self.attacksprite.append(image)
        image = attack_sheet.get_image(32, 0, 32, 32)
        self.attacksprite.append(image)
        image = attack_sheet.get_image(96, 0, 32, 32)
        self.attacksprite.append(image)
        image = attack_sheet.get_image(0, 0, 32, 32)
        self.attacksprite.append(image)

        ## List of objects that the player can collide with
        self.obj = None

        ## Health bar corresponding to the player's health
        self.hbar = hud[0]
        ## Rupee bar corresponding to the player's rupy count
        self.rbar = hud[1]
        ## Key bar corresponding to the player's key count
        self.kbar = hud[2]

        # Character Vars to keep track of

        ## Player's maximum HP amount
        self.totalhp = PLAYER_MAX_HP

        ## Player's current HP amount (starts at max)
        self.hp = PLAYER_MAX_HP

        ## Player's rupee counter
        self.rupes = 0

        ## Player's key counter
        self.keys = 0

        ## Whether the player is currently colliding with anything
        self.collision = False

        ## Whether the player has collided with the shop object
        self.collidbuy = False

        ## How long the player needs to walk into a locked door to use a key and unlock it
        # (Prevents touching and unlocking doors by accident)
        self.doorcount = PLAYER_DOORCOUNT

        self.hbar.health(self.totalhp)

        ## Checks whether the player has just entered a room
        self.spawning = False
        ## Number of frames before the user can take control of the player when they enter a room
        self.spawncount = PLAYER_SPAWNCOUNT

        # Vars for enemy hit and flyback effect

        ## Boolean allowing and stoping the player from moving
        self.moveable = True
        ## Boolean to tell whether the player is attacking or not
        self.attackbool = False
        ## Attack counter, to control how long the attack lasts
        self.attackcount = 0
        ## Holder for a sword object when attacking
        self.attacksword = None
        ## Holder for a boomerang object when using item
        self.item = None
        ## Boolean to tell whether the player is using their boomerang or not
        self.itembool = None
        ## Player's x value one frame ago
        self.oldx = self.rect.x
        ## Player's y value one frame ago
        self.oldy = self.rect.y
        
        # Direction array, starting from left going clockwise, 0 to 3
        ## Boolean array to tell which directional buttons are pressed or not (starting left going clockwise, dirbool[0] is left, dirbool[1] is up, etc)
        self.dirbool = [False, False, False, False]
        ## Current direction the player is facing
        self.dir = 0
        ## Boolean on whether the player was recently hit
        self.hit = False
        ## How long a hit counts for on the player (how long until self.hit turns off)
        self.hitcount = 0
        ## Per-frame unit speed of player
        self.speed = PLAYER_SPEED
        ## Whether debug mode is on/off
        self.debug = False
        
        self.kbar.updateText("x " + str(self.keys))

        self.rbar.updateText("x " + str(self.rupes))

        ## Has the player won or not
        self.hasWon = False
    ## @brief Function to move the player in a specified direction
    def movechar(self):
        if(self.dir == 0):
            self.rect.x -= self.speed
        elif(self.dir == 1):
            self.rect.y -= self.speed
        elif(self.dir == 2):
            self.rect.x += self.speed
        elif(self.dir == 3):
            self.rect.y += self.speed

    ## @brief Function to store which movement buttons are being pressed and let go of by the user
    # @param d Direction related to the button pressed (integer value from 0 to 3, starting from the left and going clockwise)
    # @param b Boolean value on whether the button is pressed or not
    def move(self, d, b):
        self.dirbool[d] = b

    ## @brief Function to react to the user pressing the attack button, putting the player into an attack animation and spawning a sword for the duration
    def attack(self):
        #draw a sword for a few frames and make it hit the enemy
        if((not self.attackbool) and (self.moveable)):
            audio_track1 = "src/sound/soundfx/sword-slash.wav"
            pygame.mixer.pre_init(32000, -16, 2, 512)
            pygame.mixer.init()
            self.attackbool = True
            self.attackcount = ATK_LENGTH + ATK_BUFFER
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track1))
            if(self.dir == 0):
                self.attacksword = Sword(self.rect.x-self.rect.height/2 - 2, self.rect.y + self.rect.height/2 - 3, self.dir)
            elif(self.dir == 1):
                self.attacksword = Sword(self.rect.x + 5, self.rect.y - self.rect.height/2 - 5, self.dir)
            elif(self.dir == 2):
                self.attacksword = Sword(self.rect.x + self.rect.width - 6, self.rect.y + self.rect.height/2 - 3, self.dir)
            elif(self.dir == 3):
                self.attacksword = Sword(self.rect.x + self.rect.width/2 - 3, self.rect.y + self.rect.height - 8, self.dir)
            self.groups()[0].add(self.attacksword)
            self.moveable = False

    ## @brief Function to react to the user pressing the use item button, putting the player into an attack animation and spawning a boomerang for the duration
    def useitem(self):
        audio_track2 = "src/sound/soundfx/boomerang.wav"
        pygame.mixer.pre_init(32000, -16, 2, 512)
        pygame.mixer.init()
        if(not self.itembool and not self.attackbool and self.moveable):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track2))
            self.itembool = True
            self.item = Boomerang(self.rect.x, self.rect.y, self.dir, self.obj, self)
            self.groups()[0].add(self.item)
            self.groups()[1].add(self.item)
            self.moveable = False

    ### UPDATE LOOP FUNCTIONS

    ## @brief Update function for player movement and according sprite animation
    def moveupdate(self):
        # Movement
        self.oldx = self.rect.x
        self.oldy = self.rect.y

        if(self.spawning):
            self.movechar()
            self.spawncount -= 1
            if(self.spawncount == 0):
                self.spawning = False
                self.spawncount = PLAYER_SPAWNCOUNT

        elif(self.moveable):
            if(self.dirbool[self.dir]):
                self.movechar()
            else:
                a = 0
                for i in self.dirbool:
                    if i:
                        self.dir = a
                        self.movechar()
                    a += 1

        if(self.rect.x > Wwidth - 50 or self.rect.x < 18 or self.rect.y > Wheight + Y_OFFSET - 108 or self.rect.y < Y_OFFSET + 18):
            self.leveltrans = True

        ###
        # Render Appropriate Sprites According to movement
        if self.dir == 2:
            frame = (self.oldx // GLOBAL_FRAME_BUFFER) % len(self.walkRight)
            self.image = self.walkRight[frame]
        elif self.dir == 0:
            frame = (self.oldx// GLOBAL_FRAME_BUFFER) % len(self.walkLeft)
            self.image = self.walkLeft[frame]
        elif self.dir == 1:
            frame = (self.oldy// GLOBAL_FRAME_BUFFER) % len(self.walkUp)
            self.image = self.walkUp[frame]
        elif self.dir == 3:
            frame = (self.oldy// GLOBAL_FRAME_BUFFER) % len(self.walkDown)
            self.image = self.walkDown[frame]
        
        ###

    ## @brief Update function for attack and boomerang conditions, as well as handing user collision with enemies (damage taken)
    # @detail Checks sword collision on enemies, and checks the timeout on both the sword and boomerang attack animations, telling the player
    # when they can move again. Also updates the player and reacts accordingly to recieving damage.
    def attackupdate(self):
        if(self.attackbool):
            self.attackcount -= 1
            if(self.attackcount > ATK_BUFFER):
                self.image = self.attacksprite[self.dir]
                swordcollid = pygame.sprite.spritecollide(self.attacksword, self.obj, False)
                for i in swordcollid:
                    if (i.id == "E"):
                        i.hit(self.dir)
            elif(self.attackcount == ATK_BUFFER):
              
                self.moveable = True
                self.attacksword.kill()
                self.attacksword = None
            elif(self.attackcount == 0):
                self.attackbool = False

        elif(self.itembool):
            self.image = self.attacksprite[self.dir]
            if(self.item.killable):
                self.moveable = True
                self.item.kill()
                self.item = None
                self.itembool = False
                self.attackbool = True
                self.attackcount = ATK_BUFFER

        # Attack bounceback and invincibility frames
        if(self.hit == True):
            self.hitcount -= 1
            if(self.hitcount%2 == 0):
                self.image = pygame.Surface([0,0])
            if(self.hitcount > HIT_IFRAME):
                if(self.dir == 0):
                    self.rect.x += HIT_SPEED
                elif(self.dir == 1):
                    self.rect.y += HIT_SPEED
                elif(self.dir == 2):
                    self.rect.x -= HIT_SPEED
                elif(self.dir == 3):
                    self.rect.y -= HIT_SPEED
            elif(self.hitcount == HIT_IFRAME):
                self.moveable = True
            elif(self.hitcount == 0):
                self.hit = False

    ## @brief Update function to check collisions between the player and any specified collidable objects, and call their respective collision events
    def collisionupdate(self):
        #spritecollide(sprite, group, dokill, collided = None)
        # Character and object collision
        self.collision = False
        collision = pygame.sprite.spritecollide(self, self.obj, False)
        audio_track3 = "src/sound/soundfx/link-hurt.wav"
        pygame.mixer.pre_init(32000, -16, 2, 512)
        pygame.mixer.init()
        for i in collision:
            self.collision = True
            # Wall collision
            if (i.id == "W"):
                # Put user at the edge of the wall the hit
                i.collision(self)
            # Item collision
            elif (i.id == "I"):
                # Consume item
                i.collision(self)
            # Enemy collision
            elif ((i.id == "E") & (self.hit == False)):
                # Stop movement update, throw backwards
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track3))
                if(self.hp - i.dmg <= 0):
                    self.hp -= i.dmg
                    self.hbar.health(0)
                    if(self.attacksword != None):
                        self.attacksword.kill()
                        self.attacksword = None
                    if(self.item != None):
                        self.item.kill()
                        self.item = None
                    self.moveable = False
                    ## Sprite function to delete a sprite object and all relations of the object in the project
                    self.kill()
                else:
                    self.hp -= i.dmg
                    if(self.attacksword != None):
                        self.attacksword.kill()
                        self.attacksword = None
                    if(self.item != None):
                        self.item.kill()
                        self.item = None
                    self.itembool = False
                    self.attackbool = False
                    self.attackcount = 0
                    self.hbar.health(self.hp)
                    self.hit = True
                    self.moveable = False
                    self.hitcount = HIT_TIME + HIT_IFRAME

            elif (i.id == "D"):
                # Open door
                if((i.state == 0) & (self.hit == False)):
                    pass
                # Locked door
                elif(i.state == 2):
                    if(self.keys > 0):
                        if(self.doorcount == 0):
                            i.openDoor()
                            self.keys -= 1
                            self.kbar.updateText("x " + str(self.keys))
                            self.doorcount == PLAYER_DOORCOUNT
                        else:
                            self.doorcount -= 1
                            i.collision(self)
                    else:
                        i.collision(self)
                # Blocked door
                else:
                    i.collision(self)
        if(not self.collision):
            self.collidbuy = False
            self.doorcount = PLAYER_DOORCOUNT

    ## @brief Player master update function, running all update functions, repeated in main file loop
    def update(self):

        self.moveupdate()
        self.attackupdate()
        if(not self.debug):
            self.collisionupdate()



