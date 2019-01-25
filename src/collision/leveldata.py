## @file Constants.py
# @title Actor Constants
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 9 2018

from config.window import *



## Sprite map for normal block
BLOCK = 'src/actor/sprites/block.png'

## Sprite map for water block
WATER = 'src/actor/sprites/water.png'

## Sprite maps for statues
STATUE1 = 'src/actor/sprites/statue1.png'
STATUE2 = 'src/actor/sprites/statue2.png'

## @brief Returns the pixel of the x or y coordinate for placing a block
#  @detail Uses a linear equation to return the pixel for a given block
#  @param x What grid of the tile in x or y
#  @return z The pixel value of the x or y postion 
def pos(x):
    z = 48 + 32 * x
    return z

## 2-D Array, holding pre-set level data for LevelManager.py to load
## [DoorArray, BlockArray, EnemyArray, BossArray]
## DoorArray = [[Boolean, Doorstate], [], [], []], each array coresponding to it's directional index in array (0 to 3)
## BlockArray = [[x, y], [], [], ...], as many walls as you want
## EnemyArray = [[x, y, enemyID], [], [], ...], as many enemies as you want
## BossArray = Same as enemyArray, but with boss enemies
LD = [
#R[0] (You shouldn't be able to get here!)
[[], [], [], []],
#R[1] (3 K)
[[[False, 0], [False, 0], [True, 1], [False, 0]], [], [[pos(5),pos(1), "K"],[pos(4),pos(5),"K"],[pos(3),pos(2),"K"]],[]],
#R[2] (Start Room)
[[[True, 0], [True, 2], [True, 0], [False, 0]], 
	[[pos(1),pos(1),STATUE1], [pos(4),pos(1),STATUE1], [pos(7),pos(1),STATUE2], [pos(10),pos(1),STATUE2],
	[pos(1),pos(5),STATUE1], [pos(4),pos(5),STATUE1], [pos(7),pos(5),STATUE2], [pos(10),pos(5),STATUE2]], 
	[], []],
#R[3] (3 S)
[[[True, 1], [False, 0], [False, 0], [False, 0]], 
	[[pos(2),pos(2),BLOCK], [pos(3),pos(2),BLOCK], [pos(2),pos(3),BLOCK], [pos(3),pos(3),BLOCK], [pos(2),pos(4),BLOCK], [pos(3),pos(4),BLOCK],
	[pos(8),pos(2),BLOCK], [pos(9),pos(2),BLOCK], [pos(8),pos(3),BLOCK], [pos(9),pos(3),BLOCK], [pos(8),pos(4),BLOCK], [pos(9),pos(4),BLOCK]], 
	[[pos(4),pos(2),"S"],[pos(6),pos(2),"S"], [pos(11),pos(6),"S"]], []],
#R[4] (2 K, 2 S)
[[[False, 0], [True, 1], [False, 0], [True, 1]], 
	[[pos(5),pos(2),BLOCK], [pos(6),pos(2),BLOCK], [pos(5),pos(3),BLOCK], [pos(6),pos(3),BLOCK], [pos(5),pos(4),BLOCK], [pos(6),pos(4),BLOCK]], 
	[[pos(2),pos(1),"S"],[pos(9),pos(3),"S"],[pos(3),pos(5),"K"],[pos(7), pos(2),"K"]], []],
#R[5] (2 S, 1 K)
[[[False, 0], [True, 1], [True, 1], [False, 0]], 
	[[pos(5),pos(2),BLOCK], [pos(6),pos(2),BLOCK], [pos(5),pos(3),BLOCK], [pos(6),pos(3),BLOCK], [pos(5),pos(4),BLOCK], [pos(6),pos(4),BLOCK]],
	[[pos(3),pos(1),"S"],[pos(8),pos(4),"K"],[pos(4),pos(3),"S"]], []],
#R[6] (4 K)
[[[True, 1], [False, 0], [True, 1], [True, 1]], 
	[[pos(2),pos(2),BLOCK], [pos(9),pos(2),BLOCK], [pos(2),pos(4),BLOCK], [pos(9),pos(4),BLOCK]], 
	[[pos(3),pos(1),"K"],[pos(8),pos(4),"K"],[pos(5),pos(3),"K"],[pos(10),pos(5),"K"]], []],
#R[7] (5 S)
[[[True, 1], [False, 0], [False, 0], [False, 0]], 
	[[pos(2),pos(1),BLOCK], [pos(9),pos(1),BLOCK], [pos(2),pos(5),BLOCK], [pos(9),pos(5),BLOCK]], 
	[[pos(4),pos(1),"S"],[pos(4),pos(5),"S"],[pos(6),pos(2),"S"],[pos(6),pos(4),"S"],[pos(8),pos(3),"S"]], []],
#R[8] (Shop)
[[[False, 0], [False, 0], [True, 0], [False, 0]], [], [], []],
#R[9] (4 K)
[[[True, 2], [False, 0], [True, 1], [True, 1]], [[pos(5), pos(3),BLOCK], [pos(6),pos(3),BLOCK]], 
	[[pos(4),pos(0),"K"],[pos(9),pos(4),"K"],[pos(5),pos(3),"K"],[pos(1),pos(4),"K"]], []],
#R[10] (2 S)
[[[True, 1], [True, 1], [True, 1], [False, 0]], 
	[[pos(2),pos(1),BLOCK], [pos(9),pos(1),BLOCK], [pos(2),pos(5),BLOCK], [pos(9),pos(5),BLOCK],
	[pos(1),pos(1),BLOCK], [pos(10),pos(1),BLOCK], [pos(1),pos(5),BLOCK], [pos(10),pos(5),BLOCK],
	[pos(5),pos(3),BLOCK], [pos(6),pos(3),BLOCK]], 
	[[pos(6),pos(1),"S"],[pos(10),pos(3),"S"]], []],
#R[11] (2 S, 2 K)
[[[True, 1], [False, 0], [True, 1], [False, 0]], 
	[[pos(2),pos(2),BLOCK], [pos(9),pos(2),BLOCK], [pos(2),pos(4),BLOCK], [pos(9),pos(4),BLOCK]], 
	[[pos(3),pos(1),"S"], [pos(3),pos(5),"S"], [pos(8),pos(2),"K"],[pos(8),pos(6),"K"]], []],
#R[12] (6 S)
[[[True, 1], [True, 2], [False, 0], [False, 0]], 
	[[pos(1),pos(1),BLOCK,], [pos(5),pos(1),BLOCK], [pos(6),pos(1),BLOCK],[pos(10),pos(1),BLOCK], 
	[pos(1),pos(3),BLOCK,], [pos(5),pos(3),BLOCK], [pos(6),pos(3),BLOCK], [pos(10),pos(3),BLOCK], 
	[pos(1),pos(5),BLOCK,], [pos(5),pos(5),BLOCK], [pos(6),pos(5),BLOCK], [pos(10),pos(5),BLOCK]], 
	[[pos(2),pos(0),"S"], [pos(2),pos(6),"S"], [pos(4),pos(2),"S"],[pos(4),pos(5),"S"],[pos(8),pos(0),"S"],[pos(8),pos(6),"S"]], []],
#R[13] (3 S)
[[[False, 0], [True, 1], [False, 0], [True, 1]], 
	[[pos(0),pos(0),WATER],[pos(1),pos(0),WATER], [pos(2),pos(0),WATER], [pos(3),pos(0),WATER], [pos(4),pos(0),WATER], [pos(11),pos(0),WATER], 
	[pos(7),pos(0),WATER],[pos(8),pos(0),WATER],[pos(9),pos(0),WATER],[pos(10),pos(0),WATER],[pos(0),pos(1),WATER],[pos(4),pos(1),WATER],
	[pos(0),pos(1),WATER],[pos(9),pos(1),WATER],[pos(11),pos(1),WATER],[pos(0),pos(2),WATER],[pos(2),pos(2),WATER],[pos(4),pos(2),WATER],
	[pos(6),pos(2),WATER],[pos(7),pos(2),WATER],[pos(9),pos(2),WATER],[pos(11),pos(2),WATER],[pos(2),pos(3),WATER],[pos(4),pos(3),WATER],
	[pos(7),pos(3),WATER],[pos(9),pos(3),WATER],[pos(0),pos(4),WATER],[pos(2),pos(4),WATER],[pos(4),pos(4),WATER],[pos(5),pos(4),WATER],
	[pos(7),pos(4),WATER],[pos(9),pos(4),WATER],[pos(11),pos(4),WATER],[pos(0),pos(5),WATER],[pos(2),pos(5),WATER],[pos(7),pos(5),WATER],
	[pos(11),pos(5),WATER],[pos(0),pos(6),WATER],[pos(1),pos(6),WATER], [pos(2),pos(6),WATER], [pos(3),pos(6),WATER], [pos(4),pos(6),WATER], 
	[pos(11),pos(6),WATER], [pos(7),pos(6),WATER],[pos(8),pos(6),WATER],[pos(9),pos(6),WATER],[pos(10),pos(6),WATER]], 
	[[pos(0),pos(3),"S"],[pos(11),pos(3),"S"],[pos(5.5),pos(0.5),"S"]], []],
#R[14] (1 A)
[[[False, 0], [False, 0], [True, 1], [True, 1]], [[pos(7),pos(0),BLOCK],[pos(8),pos(0),BLOCK],[pos(9),pos(0),BLOCK],[pos(10),pos(0),BLOCK], [pos(11),pos(0),BLOCK],[pos(9),pos(1),BLOCK],[pos(10),pos(1),BLOCK], [pos(11),pos(1),BLOCK],[pos(9),pos(5),BLOCK],[pos(10),pos(5),BLOCK], [pos(11),pos(5),BLOCK],[pos(7),pos(6),BLOCK],[pos(8),pos(6),BLOCK],[pos(9),pos(6),BLOCK],[pos(10),pos(6),BLOCK], [pos(11),pos(6),BLOCK]], [], [[336,128,'A']]],
#R[15] (Win Room, Triforce)
[[[True, 0], [False, 0], [False, 0], [False, 0]], 
	[[pos(1),pos(1),BLOCK],[pos(2),pos(1),BLOCK],[pos(3),pos(1),BLOCK],[pos(4),pos(1),BLOCK],[pos(5),pos(1),BLOCK],[pos(6),pos(1),BLOCK],
	[pos(7),pos(1),BLOCK],[pos(8),pos(1),BLOCK],[pos(9),pos(1),BLOCK],[pos(10),pos(1),BLOCK],[pos(1),pos(2),BLOCK],[pos(10),pos(2),BLOCK],
	[pos(1),pos(3),BLOCK],[pos(10),pos(3),BLOCK],[pos(1),pos(4),BLOCK],[pos(10),pos(4),BLOCK],[pos(1),pos(5),BLOCK],[pos(2),pos(5),BLOCK],
	[pos(3),pos(5),BLOCK],[pos(4),pos(5),BLOCK],[pos(7),pos(5),BLOCK],[pos(8),pos(5),BLOCK],[pos(9),pos(5),BLOCK],[pos(10),pos(5),BLOCK],
	[pos(4),pos(2),STATUE1],[pos(3),pos(3),STATUE1],[pos(7),pos(2),STATUE2],[pos(8),pos(3),STATUE2]], 
	[], []],
#R[16] (Rupies? 2 K)
[[[False, 0], [False, 0], [True, 1], [False, 0]], 
	[[pos(5),pos(2),BLOCK],[pos(5),pos(4),BLOCK],[pos(6),pos(1),BLOCK],[pos(6),pos(5),BLOCK],[pos(7),pos(2),BLOCK],[pos(7),pos(4),BLOCK],
	[pos(8),pos(3),BLOCK]], 
	[[pos(9),pos(2),"K"],[pos(9),pos(5),"K"]], []],
#R[17] (4 S, 3 K)
[[[True, 1], [False, 0], [False, 0], [True, 1]], 
	[[pos(1),pos(1),WATER],[pos(2),pos(1),WATER],[pos(3),pos(1),WATER],[pos(8),pos(1),WATER],[pos(9),pos(1),WATER],[pos(10),pos(1),WATER],
	[pos(1),pos(2),WATER],[pos(10),pos(2),WATER],[pos(1),pos(3),WATER],[pos(10),pos(3),WATER],[pos(3),pos(3),WATER],[pos(4),pos(3),WATER],
	[pos(5),pos(3),WATER],[pos(6),pos(3),WATER],[pos(7),pos(3),WATER],[pos(8),pos(3),WATER],[pos(1),pos(4),WATER],[pos(10),pos(4),WATER],
	[pos(1),pos(5),WATER],[pos(2),pos(5),WATER],[pos(3),pos(5),WATER],[pos(8),pos(5),WATER],[pos(9),pos(5),WATER],[pos(10),pos(5),WATER]], 
	[[pos(0),pos(0),"S"],[pos(10),pos(0),"S"],[pos(4),pos(4),"S"],[pos(7),pos(4),"S"], [pos(2),pos(3),"K"],[pos(9),pos(3),"K"]], []],
#R[18] (Not in build)
[[[False, 0], [True, 0], [False, 0], [False, 0]], [], [], []]
]

## 2-D Array, acting as an x and y map of the dungeon, and showing which rooms should be accessed on a transition in a certain direction
RID = [
[0,16,17,0,0,0],
[0,18,13,0,14,15],
[8,9,10,11,12,0],
[0,5,6,7,0,0],
[0,0,4,0,0,0],
[0,1,2,3,0,0]
]
