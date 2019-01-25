## @file door.py
# @title Dungeon Door
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018
import pygame
from actor.spritesheet import *
from config.window import *

#Door is 64x + 40y

## @brief Dungeon Door Class
# @detail This class is used to place a door on one of four places of a dungeon room, to allow the player to walk through and
# traverse to other rooms within the dungeon
class Door(pygame.sprite.Sprite):
    ## @brief Door constructor, making a door on the specified side of the dungeon
	# @param direction Integer value of the wall the door will be on (direction from centre of room)
	def __init__(self, direction, state):
		# Parent constructor
		super().__init__()

		# Get door sprite
		dungeon_path = 'src/actor/sprites/dungeonsprite.png'
		sheet = pygame.image.load(dungeon_path).convert()
		dungeon_sheet = SpriteSheet(dungeon_path)

		self.dungeon_sheet = dungeon_sheet

		## DOOR STATE	
		# 0 = open
		# 1 = blocked (objective door)
		# 2 = locked (key door)
		## State of the door, integer value on whether the door is open(0), blocked by an objective(1), or locked(2) (blocked = eg. kill all enemies in room to open)
		self.state = state
		if(self.state > 2):
			self.state = 0

		self.dir = direction

		if(direction == 0):
			#674x, 0y, 40w, 64h
			## Sprite image of the door
			self.image = pygame.transform.scale(sheet, (40, 64))
			self.image.set_colorkey(BLACK)
			image = dungeon_sheet.get_imageNT(674, 0 + 74 * self.state, 40, 64)
			self.image = image

			## X and y coordinates of the image
			self.rect = self.image.get_rect()
			self.rect.y = 128 +Y_OFFSET
			self.rect.x = 8

		elif(direction == 1):
			#486x, 24y, 64w, 40h
			self.image = pygame.transform.scale(sheet, (64, 40))
			self.image.set_colorkey(BLACK)
			image = dungeon_sheet.get_imageNT(486, 24 + 74 * self.state, 64, 40)
			self.image = image

			self.rect = self.image.get_rect()
			self.rect.y = 8+Y_OFFSET
			self.rect.x = 208
		elif(direction == 2):
			#628x, 0y, 40w, 64h
			self.image = pygame.transform.scale(sheet, (40, 64))
			self.image.set_colorkey(BLACK)
			image = dungeon_sheet.get_imageNT(628, 0 + 74 * self.state, 40, 64)
			self.image = image

			self.rect = self.image.get_rect()
			self.rect.y = 128+Y_OFFSET
			self.rect.x = 432

		elif(direction == 3):
			#558x, 24y, 64w, 40h
			self.image = pygame.transform.scale(sheet, (64, 40))
			self.image.set_colorkey(BLACK)
			image = dungeon_sheet.get_imageNT(558, 24 + 74 * self.state, 64, 40)
			self.image = image

			self.rect = self.image.get_rect()
			self.rect.y = 272+Y_OFFSET
			self.rect.x = 208

		else:
			print("Non-valid Direction for Door.py!")  

		# Collision ID
		## Collision ID (to help other objects identify what they are colliding with and how to react)
		self.id = "D"


	## @brief This method checks for collision with the Door object and other sprite object.
    #  @detail The collision will be checked with the Door and other sprite object as the object collides with the wall.
    #  @param i This is the sprite object that is passed into the method, and checks if the object is colliding with the Door object, reseting the sprite objects location accordingly.
	def collision(self, i):
		if(i.oldx + i.rect.width <= self.rect.x):
			i.rect.x = self.rect.x - i.rect.width
		elif(i.oldx >= self.rect.x + self.rect.width):
			i.rect.x = self.rect.x + self.rect.width
		elif(i.oldy + i.rect.height <= self.rect.y):
			i.rect.y = self.rect.y - i.rect.height
		elif(i.oldy >= self.rect.y + self.rect.height):
			i.rect.y = self.rect.y + self.rect.height

	## @brief Function to set a door state and sprite to open
	# @detail Changes a blocked door (state 1/2) to an open door (state 0), changing collision attributes and sprites respectively
	def openDoor(self):
		self.state = 0

		if(self.dir == 0):
			self.image = self.dungeon_sheet.get_imageNT(674, 0, 40, 64)

		elif(self.dir == 1):
			self.image = self.dungeon_sheet.get_imageNT(486, 24, 64, 40)

		elif(self.dir == 2):
			self.image = self.dungeon_sheet.get_imageNT(628, 0, 40, 64)

		elif(self.dir == 3):
			self.image = self.dungeon_sheet.get_imageNT(558, 24, 64, 40)

