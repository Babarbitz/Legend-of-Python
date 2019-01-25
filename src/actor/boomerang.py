## @file Boomerang.py
# @title Boomerang Weapon
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 6 2018

import pygame
from .spritesheet import *
from .constants import *

SPRITE_MAP = 'src/actor/sprites/boomerang.png'

## @brief Boomerang Weapon Class
# @detail The class holding the creation, behaviour, and collision effects of the player's boomerang weapon
class Boomerang(pygame.sprite.Sprite):

	## @brief Boomerang constructor
	# @detail A sprite subclass constructor that takes an x and y position (the players), a direction for the boomerang's trajectory, a list of 
	# collidable objects, as well as the player object (to add to the collision list)
	# @param x X coordinate of boomerang spawn
	# @param y Y coordinate of boomerang spawn
	# @param direction Direction of boomerang path
	# @param obj List of objects to check for collision with the boomerang
	# @param player Player object to also check collision for
	def __init__(self, x, y, direction, obj, player):
		#Pygame sprite constructor
		super().__init__()

		## Boomerang sprite image
		self.image = pygame.Surface([16, 16])
		# Load the sprite sheet
		sheet = pygame.image.load(SPRITE_MAP).convert_alpha()
		self.image = pygame.transform.scale(sheet, (16,16))
		self.image.set_colorkey(BLACK)

		## Position of boomerang
		self.rect = self.image.get_rect()

		## Initial travel direction of boomerang
		self.dir = direction

		## Boomerang initial update speed
		self.speed = BOOM_SPEED

		## List of objects the boomerang could collide with
		self.obj = obj
		self.obj.add(player)

		## Boolean to tell when the boomerang should be deleted
		self.killable = False

		## List of sprites for boomerang
		self.sprites = populateSprites()
		
		## Index of the current sprite
		self.spriteIndex = 0

		## Total number of frames boomerang is onscreen
		self.frameCounter = 0

		#Trajectory calculations
		if(direction == 0):
			self.spriteIndex = 3
			self.rect.x = x - 16
			self.rect.y = y + 8

		elif(direction == 1):
			self.spriteIndex = 0
			self.rect.x = x + 8
			self.rect.y = y - 16

		elif(direction == 2):
			self.spriteIndex = 1
			self.rect.x = x + 32
			self.rect.y = y + 8

		elif(direction == 3):
			self.spriteIndex = 2
			self.rect.x = x + 8
			self.rect.y = y + 32

	## @brief Boomerang position updating function, updating position based on changing trajectory speed
	def moveupdate(self):
		if(self.dir == 0):
			self.rect.x -= self.speed
		elif(self.dir == 1):
			self.rect.y -= self.speed
		elif(self.dir == 2):
			self.rect.x += self.speed
		elif(self.dir == 3):
			self.rect.y += self.speed
		self.speed -= BOOM_RETURN

	## @brief Boomerang collision updating function, constantly checking for collisions and acting accordingly
	def collisionupdate(self):
		itemcollid = pygame.sprite.spritecollide(self, self.obj, False)
		for i in itemcollid:
			if i.id == "W" or i.id == "D":
				if(self.speed > 0):
					self.speed = -self.speed
			elif i.id == "E":
				if(not i.isHit):
					i.stuncount = int(ENEMY_STUNCOUNT * stuncoeffient(self.frameCounter)) + 10
				if(self.speed > 0):
					self.speed = -self.speed
			elif i.id == "P":
					i.groups()[2].remove(i)
					self.killable = True

	## @brief Updates the boomerang sprite every 10 frames
	def spriteupdate(self):
		# Use 1 as it skips first frame
		if (self.frameCounter % 10 == 0):
			self.spriteIndex += 1
		
		# If it iterates past the max amount of sprites start at the beginning
		if self.spriteIndex == 4:
			self.spriteIndex = 0
		
		self.image = self.sprites[self.spriteIndex]

	## @brief Boomerang updating function, repeatedly running moveupdate and collisionupdate
	def update(self):
		self.moveupdate()
		self.spriteupdate()
		self.collisionupdate()
		self.frameCounter += 1

		
	## @brief Default collision function to satisfy other class collision calls to this object
	def collision(self):
		pass;

## @brief Creates the sprite list for Boomerang
#  @details Iterates through a sprite sheet to pull images for the sprite array
#  @return sprites Array if the sprites that represent the Boomerang
def populateSprites():
	# Create empty sprite list
	sprites = []
    
	# Load sprite sheet
	sheet = SpriteSheet(SPRITE_MAP)

	# Populate spritelist
	sprite = sheet.get_image(0, 0, 16, 16)
	sprites.append(sprite)

	sprite = sheet.get_image(16, 0, 16, 16)
	sprites.append(sprite)

	sprite = sheet.get_image(32, 0, 16, 16)
	sprites.append(sprite)

	sprite = sheet.get_image(48, 0, 16, 16)
	sprites.append(sprite)

	return sprites

## @brief Finds the coeffient for the stun value
#  @detail Uses a quadradic equation with the frame counter to find the coefficent
#  @param x The current frame of the boomerang
#  @return c The coefficent for the boomerang stun
def stuncoeffient(x):
	c = -0.001 * (x * (x - 65))
	return c