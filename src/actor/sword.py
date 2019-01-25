## @file sword.py
# @title Player Sword
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 8 2018
import pygame
from .spritesheet import *
from .constants import *

## @brief Player Sword Class
# @detail Class for the creation and deletion of the sword sprite object, made when the player attacks
class Sword(pygame.sprite.Sprite):
	## @brief Sword constructor, taking an x and y coordinate, and the direction for the sword to be pointing (player direction)
	# @param x Sword's x coordinate
	# @param y Sword's y coordinate
	# @param direction Sword's direction (integer from 0 to 3, starting left, going clockwise)
	def __init__(self, x, y, direction):
		super().__init__()

		sword_path = 'src/actor/sprites/attack_basic_sword.png'
		sheet = pygame.image.load(sword_path).convert_alpha()
		sword_sheet = SpriteSheet(sword_path)

		## Array of all possible sword directions (following usual directional standards, 0-3, starting at left going clockwise)
		self.sprite = []
		image = sword_sheet.get_image(28,0,26,14)
		self.sprite.append(image)
		image = sword_sheet.get_image(14,0,14,26)
		self.sprite.append(image)
		image = sword_sheet.get_image(54,0,26,14)
		self.sprite.append(image)
		image = sword_sheet.get_image(0,0,14,26)
		self.sprite.append(image)


		if(direction == 0):
			## Sprite image of the sword
			self.image = pygame.transform.scale(sheet, (26,14))
			self.image.set_colorkey(BLACK)
			self.image = self.sprite[0]
			## Below is for testing
			#self.image = pygame.Surface([26, 14])
			#self.image.fill((200, 0, 0))

		elif(direction == 1):
			self.image = pygame.transform.scale(sheet, (14,26))
			self.image.set_colorkey(BLACK)
			self.image = self.sprite[1]

		elif(direction == 2):
			self.image = pygame.transform.scale(sheet, (26,14))
			self.image.set_colorkey(BLACK)
			self.image = self.sprite[2]

		elif(direction == 3):
			self.image = pygame.transform.scale(sheet, (14,26))
			self.image.set_colorkey(BLACK)
			self.image = self.sprite[3]

		## X and Y position of the sword
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
