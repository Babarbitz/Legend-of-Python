## @file enemy.py
# @title Enemy Template
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
import random
from .constants import *
from config.window import *

## @brief Superclass for representing an Enemy
class Enemy(pygame.sprite.Sprite):

    ## @brief Constructor for Enemy
    #  @details Constructor takes two parameters, the x and y coordinates
    #  @param x X coordinate of the starting postion of the Enemy
    #  @param y Y coordinate of the starting postion of the Enemy
    def __init__(self, x, y):
        
        # Call superclass constructor
        super().__init__()

        ## Enemy Pygame surface
        self.image = pygame.Surface([32, 32])

        ## Rectanlge that represents enemy
        self.rect = self.image.get_rect()
        ## Enemy x postion
        self.rect.x = x
        ## Enemy y postion
        self.rect.y = y + Y_OFFSET

        ## Enemy Id type
        self.id = "E"
        
        ## Wether the enemy is hit
        self.isHit = False
        ## Remaining stun frames
        self.stuncount = 0

        # Set enemy stats
        # These will be overwritten by the subclass

        ## Enemy max health
        self.maxHP = 0
        ## Enemy current health
        self.HP = 0

        ## Enemy damage
        self.dmg = 0

        # Hit Stats
        ## This represents the  buffer for the number of hits for the Enemy after being hit by player character.
        self.hitCount = 0
        ## Represents the direction Enemy is hit in by player character attack.
        self.hitdir = 0

        ## Enemy speed in the x direction
        self.xSpeed = 0
        ## Enemy speed in the y direction
        self.ySpeed = 0

        ## Total number of frames the enemy has been alive
        self.frameCounter = 0

    ## @brief Empty function for evaluating Enemy state
    def checkState(self):
        pass

    ## @brief Moves the Enemy
    #  @details Adds the x speed and y speed to the x and y postion of the 
    #  Enemy
    def move(self):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    ## @brief Empty function for logic of Enemy
    def enemyLogic(self):
        pass

    ## @brief Update loop for a Enemy
    #  @details Checks state, does the logic, and then moves Enemy
    def update(self):
        if(self.stuncount == 0):
            self.checkState()

            self.enemyLogic()

            self.move()

            self.frameCounter += 1
        else:
            self.stuncount -= 1

    ## @brief Hit dectetion for Enemy
    #  @details Handles health, iframes and knockback direction
    #  @param direc Direction of the knockback
    def hit(self, direc):
        if(not self.isHit):
            self.hitdir = direc
            self.isHit = True
            self.HP -= 1
            self.hitCount = 30
