BOSS AND BOSS BULLET CLASSES

class BBullet(p.sprite.Sprite):
    def __init__(self, Game, pos , direction):
        self.groups = Game.all_sprites , Game.bbullet
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.bullet1_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        self.vel = direction * B_SPEED
        self.spawn_time = p.time.get_ticks()
        self.damage = 5

    def update(self):
        self.pos += self.vel * self.Game.dt
        self.rect.center = self.pos
        if p.sprite.spritecollideany(self,self.Game.tiles):
            self.kill()
        if p.time.get_ticks() - self.spawn_time > E2_B_LIFE:
            self.kill()

class BIG(p.sprite.Sprite):
    def __init__(self, Game, x, y):
        self.groups = Game.all_sprites, Game.boss
        p.sprite.Sprite.__init__(self,self.groups)
        self.Game = Game
        self.image = Game.boss_sprite
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.flipped_sprite = p.transform.flip(self.image,True,False)
        self.player_on_left = True 
        self.health = E_HEALTH
        self.bpos = 0
        self.direction = 0
        self.previous = 0

    def pick_action(self):
        action = random.randint(0,2)
        if action == 0:
            self.attack1()
        if action == 1:
            self.attack2()
        if action == 2:
            self.attack3()

    def update(self):
        track_player = (self.Game.player.pos - self.pos).angle_to(vec(1,0))%360
        hcooldown = p.time.get_ticks()
        a_rate = p.time.get_ticks()
        player_dist = self.Game.player.pos - self.pos
        if player_dist.length_squared() < DETECT_RADIUS**2:
            if a_rate - self.previous > E_ACTION_RATE:
                self.pick_action()
                self.previous = a_rate
            if track_player <= 90:
                self.image = self.Game.boss_sprite
                self.direction = vec(1,0).rotate(-track_player)
                self.bpos = self.pos + E2B_RIGHT
            elif track_player >= 270:
                self.image = self.Game.boss_sprite
                self.direction = vec(1,0).rotate(-track_player)
                self.bpos = self.pos + E2B_RIGHT
            else:
                self.image = self.flipped_sprite
                self.direction = vec(1,0).rotate(-track_player)
                self.bpos = self.pos + E2B_LEFT
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
        
    def attack1(self):
        pass
    def attack2(self):
        pass
    def attack3(self):
        pass


BOSS SETTINGS

#BOSS SETTINGS
BIGBOSS = 'BOSS.png'
E_ACTION_RATE = 1000
ONEZERO = vec(1,0)
ONEONE = vec(1,1)
ZEROONE = vec(0,1)
M_ONEONE = vec(-1,1)
M_ONEZERO = vec(-1,0)
M_ONE_ONE = vec(-1,-1)
ZERO_ONE = vec(0,-1)
ONE_ONE= vec(1,-1)

A_1_RATE = 100


BOSS IMPORTS PUT WHERE NEEDED

self.boss_sprite = p.image.load(path.join(enemy_folder, BIGBOSS)).convert_alpha()
self.boss = p.sprite.Group()
self.bbullet = p.sprite.Group()
if object.name == 'BOSS':
    BIG(self, object.x, object.y)