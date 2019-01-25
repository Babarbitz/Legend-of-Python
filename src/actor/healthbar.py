## @file healthbar.py
# @title HealthBar Class
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
from .constants import *
from .spritesheet import SpriteSheet

## @brief This class represents the HealthBar for the user controlled player character.
# @detail The HealthBar class uses the base class for visible game objects from Pygame library. 
class Health_Bar(pygame.sprite.Sprite):
    ## @brief Constructor HealthBar class.
    # @detail Constructor for class initializes the x and y location of the HealthBar object.
    # @param x this represents the x-coordinate at which the HealthBar object will be drawn.
    # @param y this represents the y-coordinate at which the HealthBar object will be drawn.
    def __init__(self, x, y):
        super().__init__()

        file_health_path = 'src/actor/sprites/healthbar.png'

        health_sheet = pygame.image.load(file_health_path).convert_alpha()
        ## This represents the sprite image for the Health_Bar object.
        self.image = pygame.transform.scale(health_sheet, (32,32))
        self.image.set_colorkey(BLACK)
        ## This represents the spritesheet for the image for the Health_Bar object, containing all sprites associated with the health bar.
        self.h_sprite_sheet = SpriteSheet(file_health_path)
        ## This represents rectangle for position for the sprite image of the Health_Bar object.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    ## @brief Method to update the current sprite image for the healthbar.
    # @detail This method will allow the HealthBar to update as soon as the player character is damaged/receives health.
    # @param i value represening the number of heart sprites to render to screen.
    def health(self, i):
        self.image = self.h_sprite_sheet.get_image(0,0,(32 * i),32)
    

   
