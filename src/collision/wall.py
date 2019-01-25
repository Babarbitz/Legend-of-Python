## @file wall.py
# @title Wall Class
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

# Wall.py
# Holds any wall or non-traversable object in-game
import pygame
from config.window import *

## @brief This class represents the Wall class for collision for objects in the environment.
# @detail The Wall class uses the base class for visible game objects from Pygame library. 
class Wall(pygame.sprite.Sprite):
    ## @brief Constructor for the Wall class.
    # @detail Constructor for Wall class initializes a Wall object based on the x/y location and the width/height of the wall, and the sprite the collision for the wall will be created upon.
    # @param x This represents the integer value for the x-location for the Wall object to be created.
    # @param y This represents the integer value for the y-location for the Wall object to be created.
    # @param w This represents the integer value for the width of the Wall object when created.
    # @param h This represents the integer value for the height of the Wall object when created.
    # @param sprite This represents the sprite that the collison for a Wall will be present upon at all times.
    def __init__(self, x, y, w, h, sprite):
        # Parent constructor
        super().__init__()

        # Make wall with given width and height, and sprite if one given
        if(sprite == None):
            ## This represents the sprite image for Wall object.
            self.image = pygame.Surface([w,h])
            self.image.fill((50, 50, 255))
        else:
            # As far as I know the sprite should be an image string
            self.image = sprite           

        # Top left corner holds the x and y
        ## This represents rectangle for position for the sprite image of the Wall object.
        self.rect = self.image.get_rect()
        self.rect.y = y + Y_OFFSET
        self.rect.x = x

        # Collision ID
        ## This represents the ID for the Wall object, ised for collision in __main.py__.
        self.id = "W"

    ## @brief This method checks for collision with the Wall object and other sprite object.
    #  @detail The collision will be checked with the Wall and other sprite object as the object collides with the wall.
    #  @param i This is the sprite object that is passed into the method, and checks if the object is colliding with the Wall object, reseting the sprite objects location accordingly.
    def collision(self, i):
        if(i.oldx + i.rect.width <= self.rect.x):
            i.rect.x = self.rect.x - i.rect.width
        elif(i.oldx >= self.rect.x + self.rect.width):
            i.rect.x = self.rect.x + self.rect.width
        elif(i.oldy + i.rect.height <= self.rect.y):
            i.rect.y = self.rect.y - i.rect.height
        elif(i.oldy >= self.rect.y + self.rect.height):
            i.rect.y = self.rect.y + self.rect.height
