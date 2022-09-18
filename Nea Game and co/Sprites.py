import pygame as p
from Settings import *
from random import uniform
import time
vec = p.math.Vector2

def hit_wall(sprite, group, direction):
    if direction == 'x':
        hits = p.sprite.spritecollide(sprite,group, False)
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right
            sprite.vel.x = 0
            sprite.rect.x = sprite.pos.x

    if direction == 'y':
        hits = p.sprite.spritecollide(sprite,group, False)
        if hits:
            if hits[0].rect.centery > sprite.rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height
            if hits[0].rect.centery < sprite.rect.centery:
                sprite.pos.y = hits[0].rect.bottom
            sprite.vel.y = 0
            sprite.rect.y = sprite.pos.y

class Player(p.sprite.Sprite):
    def __init__(self, Game , x , y):
        self.groups = Game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game 
        self.image =  Game.player_sprite
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) *TILESIZE
        self.facing_left = False
        self.flipped_sprite = p.transform.flip(self.image, True, False)
        self.previous = 0
        self.health = P_HEALTH
        self.last_hit = 0
        
        

    def movement(self):
        self.vel = vec(0, 0) 
        keys = p.key.get_pressed()
        if keys[p.K_a]:
            self.facing_left = True
            self.vel.x = -MOVESPEED
        if keys[p.K_d]:
            self.facing_left = False
            self.vel.x = MOVESPEED
        if keys[p.K_w]:
            self.vel.y = -MOVESPEED
        if keys[p.K_s]:
            self.vel.y = MOVESPEED
        if self.vel.x != 0 and self.vel.y != 0 :
            self.vel *= 0.7071
        if keys[p.K_RIGHT]:
            now = p.time.get_ticks()
            self.facing_left = False
            if now - self.previous >B_RATE:
                self.previous = now 
                direction = vec(1,0)
                pos = self.pos + B_MOVE
                Bullet(self.Game, pos, direction)
                self.vel = vec(-RECOIL, 0)
        if keys[p.K_LEFT]:
            now = p.time.get_ticks()
            self.facing_left = True
            if now - self.previous >B_RATE:
                self.previous = now 
                direction = vec(-1,0)
                pos = self.pos + B_MOVE
                Bullet(self.Game, pos, direction)
                self.vel = vec(+RECOIL, 0)

    def update(self):
        self.track_mouse = (self.pos - p.mouse.get_pos()).angle_to(vec(1,0))%360
        self.movement()
        self.pos += self.vel * self.Game.dt
        self.rect.x = (self.pos.x)
        hit_wall(self, self.Game.tiles,'x')
        self.rect.y = (self.pos.y)
        hit_wall(self, self.Game.tiles,'y')
        if self.facing_left:
            self.image = self.flipped_sprite
        else:
            self.image = self.Game.player_sprite
                
class Enemy(p.sprite.Sprite):
    def __init__(self, Game, x, y):
        self.groups = Game.all_sprites , Game.enemy
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.enemy1_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(x,y) * TILESIZE
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.flipped_sprite = p.transform.flip(self.image,True,False)
        self.player_on_left = True 
        self.health = E_HEALTH
               

    def update(self):
        track_player = (self.Game.player.pos - self.pos).angle_to(vec(1,0))%360
        hcooldown = p.time.get_ticks()
        if track_player <= 90:
            self.image = self.Game.enemy1_sprite
        elif track_player >= 270:
            self.image = self.Game.enemy1_sprite
        else:
            self.image = self.flipped_sprite
        if hcooldown - self.Game.player.last_hit > E_FRAME:
            self.acc = vec(E_SPEED, 0).rotate(-track_player)
            self.acc += self.vel* -1
            self.vel += self.acc * self.Game.dt
            self.pos += self.vel * self.Game.dt + 0.5 * self.acc * self.Game.dt ** 2
        self.rect.x = (self.pos.x)
        hit_wall(self, self.Game.tiles,'x')
        self.rect.y = (self.pos.y)
        hit_wall(self, self.Game.tiles,'y')
        if self.health == 0:
            self.kill()

class Enemy2(p.sprite.Sprite):
    def __init__(self, Game, x, y):
        self.groups = Game.all_sprites , Game.enemy2
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.enemy2_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(x,y) * TILESIZE
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.flipped_sprite = p.transform.flip(self.image,True,False)
        self.player_on_left = True 
        self.health = E2_HEALTH      
        self.previous = 0
        

    def update(self):
        track_player = (self.Game.player.pos - self.pos).angle_to(vec(1,0))%360
        now = p.time.get_ticks()
        hcooldown = p.time.get_ticks()
        if track_player <= 90:
            self.image = self.Game.enemy2_sprite
            direction = vec(1,0).rotate(-track_player)
            bpos = self.pos + E2B_RIGHT
        elif track_player >= 270:
            self.image = self.Game.enemy2_sprite
            direction = vec(1,0).rotate(-track_player)
            bpos = self.pos + E2B_RIGHT
        else:
            self.image = self.flipped_sprite
            direction = vec(1,0).rotate(-track_player)
            bpos = self.pos + E2B_LEFT
        if hcooldown - self.Game.player.last_hit > E_FRAME:
            self.acc = vec(E2_SPEED, 0).rotate(-track_player)
            self.acc += self.vel* -1
            self.vel += self.acc * self.Game.dt
            self.pos += self.vel * self.Game.dt + 0.5 * self.acc * self.Game.dt ** 2
            if now - self.previous > E2_RATE:
                self.previous = now 
                EBullet(self.Game, bpos, direction)
        self.rect.x = (self.pos.x)
        hit_wall(self, self.Game.tiles,'x')
        self.rect.y = (self.pos.y)
        hit_wall(self, self.Game.tiles,'y')
        if self.health == 0:
            self.kill()
        

    

class Tile(p.sprite.Sprite):
    def __init__(self, Game, x, y):
        self.groups = Game.all_sprites , Game.tiles
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = p.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Bullet(p.sprite.Sprite):
    def __init__(self, Game, pos , direction):
        self.groups = Game.all_sprites , Game.bullet
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.bullet1_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-SPREAD,SPREAD)
        self.vel = direction.rotate(spread) * B_SPEED
        self.spawn_time = p.time.get_ticks()
        self.damage = 5

    def update(self):
        self.pos += self.vel * self.Game.dt
        self.rect.center = self.pos
        if p.sprite.spritecollideany(self,self.Game.tiles):
            self.kill()
        if p.time.get_ticks() - self.spawn_time > B_LIFE:
            self.kill()

class EBullet(p.sprite.Sprite):
    def __init__(self, Game, pos , direction):
        self.groups = Game.all_sprites , Game.ebullet
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.bullet1_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-SPREAD,SPREAD)
        self.vel = direction.rotate(spread) * B_SPEED
        self.spawn_time = p.time.get_ticks()
        self.damage = 5

    def update(self):
        self.pos += self.vel * self.Game.dt
        self.rect.center = self.pos
        if p.sprite.spritecollideany(self,self.Game.tiles):
            self.kill()
        if p.time.get_ticks() - self.spawn_time > E2_B_LIFE:
            self.kill()