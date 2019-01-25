## @file Constants.py
# @title Actor Constants
# @author Giacomo Loparco, Bilal Jaffry, Lucas Zacharewicz
# @date November 7 2018

# Actor constants

# Actor Colours
## Defines the colour black
BLACK = (0,0,0)
## Defines the colour white
WHITE = (255, 255, 255)
## Defines the colour purple
PURPLE = (255, 50, 255)
## Defines the colour red
RED = (255, 50, 50)
## Defines the color blue
BLUE = (0,0,255)

# player constants

## Defines the player's width
PLAYER_WIDTH = 15
## Defines the player's height
PLAYER_HEIGHT = 15
## Defines the player's speed
PLAYER_SPEED = 2
## Defines the player's max hp
PLAYER_MAX_HP = 3
## Defines how many frames the player collides with a locked door before a key is used
PLAYER_DOORCOUNT = 20
## Defines how long the player is uncontrollable for when entering a new room (movement to walk out of door)
PLAYER_SPAWNCOUNT = 8

## Defines the speed of the knock back applied per frame
HIT_SPEED = 12
## Defines the number of frames hit speed is applied for
HIT_TIME = 5
## Defines the number of iframes
HIT_IFRAME = 30

## Defines the width of the attack hitbox
ATK_WIDTH = 15
## Defines the height of the attack hitbox
ATK_HEIGHT = 15
## Defines the number of frames the hit stays out for
ATK_LENGTH = 10
## Defines the number of frames before the next attack can start
ATK_BUFFER = 20

## Defines the bommerang speed
BOOM_SPEED = 9
## Defines the acceleration in the opposite direction of the bommerang's travel path
BOOM_RETURN = 0.3

## Coordinate Divisor that determines range in which next sprite should render
GLOBAL_FRAME_BUFFER = 12

# Keese constants

## Defines the keese's max hp
KEESE_MAX_HP = 1
## Defines the keese's damage
KEESE_DMG = 0.5
## Defines the keese's max speed
KEESE_MAX_SPEED = 2
## Defines the keese's min speed
KEESE_MIN_SPEED = 1
## Defines the keese's minimum magnitude from its determined travel point before stopping
ACCEPTABLE_RADIUS = 20
## Defines the keese's minimum magnitude for selecting its next travel point
KEESE_MAGNITUDE_MIN = 200

# Stalfos constants

## Defines the stalfos' max hp
STALFOS_MAX_HP = 2
## Defines the stalfos' damage
STALFOS_DMG = 1
## Defines the stalfos' speed
STALFOS_SPEED = 1
## Defines the stalfos' speed during knockback
STALFOS_HIT_SPEED = 10

## Length of frames an enemy will be stunned for when hit by a boomerang
ENEMY_STUNCOUNT = 35

# Aquamentus constants

## Defines the aquamentus' max hp
AQUAMENTUS_MAX_HP = 5
## Defines the aquamentus' damage
AQUAMENTUS_DMG = 2
## Defines the aquamentus' speed
AQUAMENTUS_SPEED = 1

# Fireball constants

## Defines the fireballs damage
FIREBALL_DMG = 1
