import pygame as p
vec = p.math.Vector2


#GLOBAL SETTINGS

FPS = 60
WIDTH = 800
HEIGHT = 600

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

TITLE = "Precaution"

#PLAYER SETTINGS
MOVESPEED = 300
P_SPRITE = 'P_IDLE.png'
P_SPRITE_FLIPPED = 'tile000_flipped.png'
P_HEALTH = 300
I_FRAME = 1000
E_FRAME = 500

#ENEMY SETTINGS
E_SPRITE = 'E_IDLE.png'
E_SPEED = 310
E_HEALTH = 50
E_DAMAGE = 50
KNOCKBACK  = 20

#ENEMY2 SETTINGS
E2_SPRITE = 'E2_IDLE.png'
E2_SPEED = 100
E2_RATE = 500
E2B_LEFT = vec(0,30)
E2B_RIGHT = vec(70,30)
E2_HEALTH = 500
E2_DAMAGE = 50
E2_B_DAMAGE = 60
E2_B_LIFE = 1500

#Player BULLET SETTINGS
Bullet1 = 'BULLET.png'
B_SPEED = 500
B_LIFE = 800
B_RATE = 200
B_MOVE = vec(20,20)
RECOIL = 100
SPREAD = 6
DAMAGE = 10

#colors
SAGE = (156,175,136)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LILAC = (170, 152, 169)
YELLOW = (0, 255, 255)

#INFORMATION

#GRIDSIZE = 50X AND 40Y