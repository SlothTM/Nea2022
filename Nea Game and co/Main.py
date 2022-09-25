#IMPORTS
import pygame as p
from Settings import *
from Sprites import *
import sys
from os import path
from Maps import *

def draw_health(surf,x ,y , perc):
    if perc < 0: 
        perc == 0
    fill = perc * BAR_LEGNTH
    outline_rect = p.Rect(x,y, BAR_LEGNTH,BAR_HEIGHT)
    fill_rect = p.Rect(x,y, fill , BAR_HEIGHT)
    if perc > 0.7:
        col = GREEN
    elif perc > 0.3:
        col = YELLOW
    else:
        col = RED
    p.draw.rect(surf,col , fill_rect)
    p.draw.rect(surf, WHITE, outline_rect, 2)


class Game:
    def __init__(self): #initialize things we want once game starts
        p.init() # initialise a p window
        self.screen = p.display.set_mode((WIDTH,HEIGHT)) #Make the p window have the height and width ive set
        p.display.set_caption(TITLE) # make the title Preccaution
        self.clock = p.time.Clock()  #fps
        p.key.set_repeat(200,100)
        self.running = True
        self.load()
        
    def load(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'Idle')
        enemy_folder = path.join(game_folder,'Enemy Idle')
        proj_folder = path.join(game_folder,'BULLET')
        map_folder = path.join(game_folder, 'MAPS')
        self.map = TiledMap(path.join(map_folder, 'RMAP1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_sprite = p.image.load(path.join(image_folder, P_SPRITE)).convert_alpha()
        self.enemy1_sprite = p.image.load(path.join(enemy_folder, E_SPRITE)).convert_alpha()
        self.enemy2_sprite = p.image.load(path.join(enemy_folder, E2_SPRITE)).convert_alpha()
        self.bullet1_sprite = p.image.load(path.join(proj_folder, Bullet1)).convert_alpha()


    def new(self): #reset game
        self.all_sprites = p.sprite.Group()
        self.tiles = p.sprite.Group()
        self.enemy = p.sprite.Group()
        self.enemy2 = p.sprite.Group()
        self.bullet = p.sprite.Group()
        self.ebullet = p.sprite.Group()
        
        '''for row, dots in enumerate(self.map.data):
            for col, dot in enumerate(dots):
                if dot == '1':
                    Tile(self, col,row)
                if dot == 'P':
                    self.player = Player(self, col, row)
                if dot == 'E':
                    Enemy(self, col, row)
                if dot == 'T':
                    Enemy2(self, col, row)
'''
        for object in self.map.tmxdata.objects:
            if object.name == 'PLAYER':
                self.player = Player(self, object.x, object.y)
            if object.name == 'WALL':
                wall_object(self, object.x, object.y, object.width, object.height)
            if object.name == 'E1':
                Enemy(self, object.x, object.y)
            if object.name == 'E2':
                Enemy2(self, object.x, object.y)
                
        self.POV = POV(self.map.width,self.map.height)

    def start(self): # game loop:
        self.run = True
        while self.run:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.POV.update(self.player)
        cooldown = p.time.get_ticks()
        
        hits = p.sprite.spritecollide(self.player,self.enemy,False,False)
        for hit in hits:
            if cooldown - self.player.last_hit > I_FRAME:
                self.player.last_hit = cooldown
                self.player.health -= E_DAMAGE
                hit.vel = vec(0,0)
            
        hits = p.sprite.spritecollide(self.player,self.enemy2,False,False)
        for hit in hits:
            if cooldown - self.player.last_hit > I_FRAME:
                self.player.last_hit = cooldown
                self.player.health -= E2_DAMAGE
                hit.vel = vec(0,0)
            
        
        hits = p.sprite.spritecollide(self.player,self.ebullet,True,False)
        for hit in hits:
            self.player.health -= E2_B_DAMAGE
            hit.vel = vec(0,0)
        
        if self.player.health <= 0:
            self.run = False

        shots = p.sprite.groupcollide(self.enemy,self.bullet,False,True)
        for hit in shots:
            hit.health -= DAMAGE
            hit.vel = vec(0,0)

        shots2 = p.sprite.groupcollide(self.enemy2,self.bullet,False,True)
        for hit in shots2:
            hit.health -= DAMAGE
            hit.vel = vec(0,0)

    def events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                if self.run:
                    self.run = False
                self.running = False
            if event.type == p.KEYDOWN:
                pass

    def show_grid(self):
        for x in range(0,WIDTH, TILESIZE):
            p.draw.line(self.screen , WHITE, (x,0), (x, HEIGHT))
        for y in range(0,WIDTH, TILESIZE):
            p.draw.line(self.screen , WHITE, (0,y), (WIDTH, y))

    def draw(self):
        self.screen.blit(self.map_img, self.POV.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.POV.track(sprite))
        draw_health(self.screen,16,10,self.player.health/P_HEALTH)
        #self.show_grid()
        p.display.flip()

    def start_screen(self):
        pass

    def over(self):
        pass
        

g = Game()
g.start_screen()
while g.running:
    g.new()
    g.start()
    g.over()

p.quit()