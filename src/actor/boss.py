## @file Boss.py
# @title Boss Template
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
import random
from .constants import *
from config.window import *

## @brief Superclass for representing a Boss
class Boss(pygame.sprite.Sprite):

    ## @brief Constructor for Boss
    #  @details Constructor takes two parameters, the x and y coordinates
    #  @param x X coordinate of the starting postion of the Boss
    #  @param y Y coordinate of the starting postion of the Boss
    def __init__(self, x, y):
        
        # Call superclass constructor
        super().__init__()

        ## Boss Pygame surface
        self.image = pygame.Surface([64, 64])

        # Set the values for the rectangle that defines the objects bounds
        ## Rectanlge that represents boss
        self.rect = self.image.get_rect()
        ## X postion of the boss
        self.rect.x = x
        ## Y postion of the boss
        self.rect.y = y+Y_OFFSET

        # Set id to type 'Enemy'
        ## Boss ID
        self.id = "E"
        
        ## Wether the boss is hit or not
        self.isHit = False

        ## The amount of stun frames the boss has remaining
        self.stuncount = 0

        # Set enemy stats
        # These will be overwritten by the subclass

        ## Boss' max health
        self.maxHP = 0
        ## Boss' current health
        self.HP = 0

        ## Boss' damage
        self.dmg = 0

        ## Boss' hit count
        self.hitCount = 0

        ## Boss' speed in the x direction
        self.xSpeed = 0
        ## Boss' speed in the y direction
        self.ySpeed = 0

        ## Total number of frames the boss has been alive for
        self.frameCounter = 0
    
    ## @brief Empty function for evaluating Boss state
    def checkState(self):
        pass

    ## @brief Moves the Boss
    #  @details Adds the x speed and y speed to the x and y postion of the 
    #  Boss
    def move(self):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    ## @brief Empty function for logic of Boss
    def bossLogic(self):
        pass

    ## @brief Update loop for a Boss
    #  @details Checks state, does the logic, and then moves Boss
    def update(self):
        if(self.stuncount == 0):
            self.checkState()

            self.bossLogic()
            # Hacky fix for slower boss movement but what ever
            if (self.frameCounter % 2 == 0):
                self.move()

            self.frameCounter += 1
        else:
            self.stuncount -= 1

    ## @brief Hit dectetion for Boss
    #  @details Handles health and iframes
    def hit(self, dir):
        if(not self.isHit):
            self.HP -= 1
            self.hitCount = 50
            self.isHit = True