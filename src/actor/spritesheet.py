## @file spritesheet.py
# @title SpriteSheet Class
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018
import pygame
from .constants import *

## @brief This class represents the SpriteSheet object, allowing sprites to be loaded and processed.
# @detail The SpriteSheet class uses the Pygame library to load images and change the transperancy on those images.
class SpriteSheet(object):
    ## @brief Constructor for the SpriteSheet class.
    # @detail This constructor initializes an image file using the Pygame library.
    # @param file_name This is the string representing the path to the image file.
    def __init__(self, file_name):
        ## This represents the current spritesheet loaded from the specific file_name path.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    ## @brief Accessor to return an image splice from the loaded SpriteSheet.
    # @detail This accessor returns an image splice based on the x,y location and the height and width of the image.
    # @param x The x-coordinate for starting point of the splice on the SpriteSheet.
    # @param y The y-coordinate for starting point of the splice on the SpriteSheet.
    # @param width The width of the splice on the SpriteSheet.
    # @param height The height of the splice on the SpriteSheet.
    # @return image This returns the newly spliced image after removing the image background transparency.
    def get_image(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image
    ## @brief Accessor to return an image splice from the loaded SpriteSheet, WITHOUT removing the image background.
    # @detail This accessor returns an image splice based on the x,y location and the height and width of the image.
    # @param x The x-coordinate for starting point of the splice on the SpriteSheet.
    # @param y The y-coordinate for starting point of the splice on the SpriteSheet.
    # @param width The width of the splice on the SpriteSheet.
    # @param height The height of the splice on the SpriteSheet.
    # @return image This returns the newly spliced image WITHOUT removing the image background transparency.
    def get_imageNT(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image
