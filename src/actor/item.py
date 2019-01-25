## @file item.py
# @title Consumable Items
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 6 2018

import pygame
import random
from .spritesheet import *
from .constants import *

## @brief Consumable Item Class
# @detail This class is used for the creation of a random consumable item, spawned once an enemy has been defeated on their last position before
# despawn
class Item(pygame.sprite.Sprite):

    ## @brief Item constructor
    # @detail A sprite subclass constructor which takes a pair of x-y coordinates, commonly those of the killed enemy, and an item type, in the form of
    # a randomly generated integer from 0 to the # of possible items
    # @param x X coordinate of the spawned item
    # @param y Y coordinate of the spawned item
    # @param typ Integer value to specify the type of consumable item
    def __init__(self, x, y, typ):
        # Parent constructor
        super().__init__()

        self.image = pygame.Surface([20,15])

        try:
            # Make wall with given width and height, and sprite if one given
            item_path = 'src/actor/sprites/items2.png'
            sheet = pygame.image.load(item_path).convert_alpha()
            item_sheet = SpriteSheet(item_path)

            ## Item sprite image
            self.image = pygame.transform.scale(sheet, (20, 15))
            self.image.set_colorkey(BLACK)

            ## List of possible item sprite images
            self.itemsprite = []
            image = item_sheet.get_image(0, 0, 32, 32)
            self.itemsprite.append(image)
            image = item_sheet.get_image(32, 0, 32, 32)
            self.itemsprite.append(image)
            image = item_sheet.get_image(64, 0, 32, 32)
            self.itemsprite.append(image)
            image = item_sheet.get_image(96, 0, 32, 32)
            self.itemsprite.append(image)
            image = item_sheet.get_image(128, 0, 32, 32)
            self.itemsprite.append(image)
            image = item_sheet.get_image(160, 0, 32, 32)
            self.itemsprite.append(image)

            self.image = self.itemsprite[typ]
        except pygame.error as message:
            print("image did not load")

        ## Item x and y position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        ## Collision ID (how other items tell what this item is)
        self.id = "I"

        # Type of item
        # Index of items:
        # 0 = heart
        # 1 = rupy
        # 2 = key
        # 3 = triforce
        # 4 = shop item
        # 5 = 2-10x rupy (random value)

        ## Integer value to determine what kind of item this is (rupee, heart, etc)
        self.type = typ


    ## @brief Collision handler for the player and the consumable item, depending on the item's type
    # @param p Player object
    def collision(self, p):
        audio_track1 = "src/sound/soundfx/get-heart.wav"
        audio_track2 = "src/sound/soundfx/get-rupee.wav"
        audio_track3 = "src/sound/soundfx/key-appear.wav"
        pygame.mixer.pre_init(32000, -16, 2, 512)
        pygame.mixer.init()
        if(self.type == 0):
            if(p.hp < p.totalhp):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track1))
                p.hp += 1
                if(p.hp > p.totalhp):
                    p.hp = p.totalhp
                p.hbar.health(p.hp)
                self.kill()
        elif(self.type == 1):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track2))
            p.rupes += 1
            p.rbar.updateText("x " + str(p.rupes))
            self.kill()
        elif(self.type == 2):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track3))
            p.keys += 1
            p.kbar.updateText("x " + str(p.keys))
            self.kill()
        elif(self.type == 3):
            p.hasWon = True
            self.kill()
        elif(self.type == 4):
            if((not p.collidbuy) & (p.rupes > 4) & (p.hp < 3)):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track1))
                p.collidbuy = True
                p.rupes -= 5
                p.hp += 1
                if(p.hp > p.totalhp):
                    p.hp = p.totalhp
                p.hbar.health(p.hp)
                p.rbar.updateText("x " + str(p.rupes))
        elif(self.type == 5):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(audio_track2))
            p.rupes += random.randint(2,10)
            p.rbar.updateText("x " + str(p.rupes))
            self.kill()
