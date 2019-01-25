## @file levelmanager.py
# @title Dungeon Level Master Creator
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

import pygame
from copy import deepcopy
from .level import *
from .wall import *
from .door import *
from .leveldata import *
from .block import *
from actor.aquamentus import *
from actor.keese import *
from actor.stalfos import *
from actor.item import *
from actor.renderfont import *
from config.colour import *

## @brief Dungeon Level Creation Class
# @detail Class used as a master constructor for every dungeon levels, getting pre-written data and loading it when the game starts and when a 
# transition occurs
class LevelManager():

	keyset = [3, 7, 17]
	rupeset = [1, 16, 12]
	LD = None
	## @brief Dungeon Level Master Initializer
	# @detail The class initializer, taking empty lists, each for letting the make() function define what objects need
	# to be drawn/collidable/updatable
	# @param spritelist List of objects for the game to print (usually empty pygame.sprite.Group)
	# @param collidlist List of objects which have a collision interaction with the player (usually empty pygame.sprite.Group)
	# @param updatelist List of objects which need to be regularly updated (usually empty pygame.sprite.Group)
	def __init__(self, spritelist, collidlist, updatelist):
		## List of all rooms to load (to be altered)
		self.LD = deepcopy(LD)
		## List of objects to be printed (ie player, not invisible walls)
		self.sl = spritelist
		## List of objects that can be collided with (ie keese, not level background)
		self.cl = collidlist
		## List of objects that need to be constantly updated (ie player, not walls/static objects)
		self.ul = updatelist


	## @brief Dungeon Level Constructor
	# @detail The main function to load a given index of data from leveldata.py, and load it into the game environment
	# @param i Index of the room to be created
	def make(self, x, y):
		#Level loads the initial sprite array (Obj from level class)
		## X-Coordinate of the level in leveldata's Room ID array (RID[y][x])
		self.x = x
		## Y-Coordinate of the level in leveldata's Room ID array (RID[y][x])
		self.y = y
		## Level background
		self.level = Level()
		self.sl.add(self.level)

		self.RID = RID[y][x]

		doors = self.LD[self.RID][0]
		blocks = self.LD[self.RID][1]
		enarray = self.LD[self.RID][2]
		boss = self.LD[self.RID][3]

		self.enarray = pygame.sprite.Group()
		self.boss = pygame.sprite.Group()
		self.doors = []
		self.killed = False

		#Doors is a boolean array, starting from 0 going to 3 from left clockwise
		#True = door, False = no door
		doorcount = 0
		for door in doors:
			if(door[0]):
				# Make door obj in specified location
				door = Door(doorcount, door[1])
				self.doors.append(door)
				self.sl.add(door)
				self.cl.add(door)
				if(doorcount == 0):
					wall = Wall(0, 0, 48, 140, None)
					self.cl.add(wall)
					wall = Wall(0, 180, 48, 140, None)
					self.cl.add(wall)
				elif(doorcount == 1):
					wall = Wall(0, 0, 220, 48, None)
					self.cl.add(wall)
					wall = Wall(260, 0, 240, 48, None)
					self.cl.add(wall)
				elif(doorcount == 2):
					wall = Wall(432, 0, 48, 140, None)
					self.cl.add(wall)
					wall = Wall(432, 180, 48, 140, None)
					self.cl.add(wall)
				else:
					wall = Wall(0, 272, 220, 48, None)
					self.cl.add(wall)
					wall = Wall(260, 272, 240, 48, None)
					self.cl.add(wall)
			else:
				if(doorcount == 0):
					wall = Wall(0, 0, 48, 320, None)
					self.cl.add(wall)
				elif(doorcount == 1):
					wall = Wall(0, 0, 480, 48, None)
					self.cl.add(wall)
				elif(doorcount == 2):
					wall = Wall(432, 0, 48, 320, None)
					self.cl.add(wall)
				else:
					wall = Wall(0, 272, 480, 48, None)
					self.cl.add(wall)
			doorcount += 1

		#Blocks is an array of x and y coords to put small walls in the map down
		for block in blocks:
			#Go make a wall or somesuch (Wall w/ sprite)
			a = Block(block[0], block[1], block[2])
			self.sl.add(a)
			self.cl.add(a)

		#EnArray is an array of x-and-y coords, along with enemy type
		# K = Keese
		# S = Skelly
		for enemy in enarray:
			if(enemy[2] == 'K'):
				a = Keese(enemy[0], enemy[1])
				self.sl.add(a)
				self.cl.add(a)
				self.ul.add(a)
				a.stuncount = 20
				self.enarray.add(a)
			elif(enemy[2] == 'S'):
				a = Stalfos(enemy[0],enemy[1])
				self.sl.add(a)
				self.cl.add(a)
				self.ul.add(a)
				a.obj = self.cl
				a.stuncount = 20
				self.enarray.add(a)
		
		for b in boss:
			if (b[2] == 'A'):
				boss = Aquamentus(b[0],b[1])
				self.sl.add(boss)
				self.cl.add(boss)
				self.ul.add(boss)
				self.boss.add(boss)
				for i in boss.fireballs:
					self.sl.add(i)
					self.cl.add(i)
					self.ul.add(i)
					i.obj = self.cl
				boss.obj = self.cl


		## Misc room spawnings (ie shop room)
		if(self.RID == 8):
			a = Item(224,220,4)
			self.sl.add(a)
			self.cl.add(a)
			a = Render_Font(62, 144, "BUY A HEART FOR 5 RUPES!", 15, WHITE)
			self.sl.add(a)

		elif(self.RID == 15):
			a = Item(48+32*5.5,48+32*4.5,3)
			self.sl.add(a)
			self.cl.add(a)

		elif(self.RID == 0):
			a = Render_Font(62, 144, "YOU SHOULDN'T BE HERE", 17, RED)
			self.sl.add(a)

	## @brief Dungeon level transition function, used to go to an adjacent level, clear all current data, and load new room data
	# @param j Value to add to the current index to get to new room
	def transition(self, xchange, ychange):
		self.y += ychange
		self.x += xchange
		self.sl.empty()
		self.cl.empty()
		self.ul.empty()
		## Make the door you went through always unlocked
		if(xchange == 1):
			self.LD[self.RID][0][2][1] = 0
		elif(xchange == -1):
			self.LD[self.RID][0][0][1] = 0
		elif(ychange == 1):
			self.LD[self.RID][0][3][1] = 0
		else:
			self.LD[self.RID][0][1][1] = 0
		self.make(self.x, self.y)

	## @brief Function to open all blocked doors in the current dungeon room (usually used when all enemies defeated, locked doors stay locked)
	def open(self):
		for i in self.doors:
			if(i.state == 1):
				i.openDoor()
		for i in self.LD[self.RID][0]:
			if i[1] == 1:
				i[1] = 0

	## @brief Function to store current data, open all blocked doors, and possibly spawn a key/prize when all enemies defeated
	# @detail When all enemies in a room are killed, this function is called, changing the enemy array in leveldata.py for the current
	# level to an empty array (so enemies don't reload once you enter again), running the self.open() function to open all blocked
	# doors, and if the roomID is a predetermined key/rupy room, spawn a key/rupy in the middle of the room
	def endroom(self):
		self.killed = True
		self.open()
		self.LD[self.RID][2] = []
		self.LD[self.RID][3] = []
		if(self.RID in self.keyset):
			self.keyset.remove(self.RID)
			a = Item(240, 176 + 56, 2)
			self.sl.add(a)
			self.cl.add(a)
		elif(self.RID in self.rupeset):
			self.rupeset.remove(self.RID)
			a = Item(240, 176 + 56, 5)
			self.sl.add(a)
			self.cl.add(a)
	
	## @brief Clears the levelmanager's update lists
	# @detail Empty all sprite lists for the game (spritelist, collisionlist, and updatelist), usually used in transition from one room to another
	def clear(self):
		self.sl.empty()
		self.cl.empty()
		self.ul.empty()


				
