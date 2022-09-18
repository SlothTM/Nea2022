import pygame as p
from Settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class POV:
    def __init__(self,width,height):
        self.pov = p.Rect(0,0 , width, height)
        self.width = width
        self.height = height

    def track(self , entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, follow):
        x = -follow.rect.x + int(WIDTH/2)
        y = -follow.rect.y + int(HEIGHT/2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)

        self.camera = p.Rect(x,y, self.width, self.height)

       

       
