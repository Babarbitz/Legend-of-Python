## @file renderfont.py
# @title Render_Font Class
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 8 2018


import pygame

## @brief This class represents the Render_Font object.
# @detail The Render_font uses the Pygame library, and is a subclass of the pygame.sprite class
class Render_Font(pygame.sprite.Sprite):
	## @brief Initializer for a rendered font sprite object
	# @detail Initializer function, takes an x, y, string, font size and colour, and returns a sprite object
	# of the given string at the given x and y coordinates
	# @param x Text sprite x coordinate
    # @param y Text sprite y coordinate
    # @param string Text of the text sprite (what string will be displayed)
    # @param fontsize Size of the text
    # @param color Colour of the text
	def __init__(self, x, y,string,fontsize,color):
		super().__init__()

		pygame.font.init()
		self.color = color
		self.myfont = pygame.font.Font('src/config/the-legend-of-zelda-nes.ttf', fontsize)
		textsurface = self.myfont.render(string, False, color)
		## This represents the sprite image for the Render_Font object.
		self.image = textsurface
		## This represents rectangle for  position for the sprite image of the Render_Font object.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	## @brief Function to update the string of an existing text sprite
	# @param string New string to be displayed
	def updateText(self, string):
		self.image = self.myfont.render(string, False, self.color)
