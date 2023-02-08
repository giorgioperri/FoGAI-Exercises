import pygame
from vector import Vector2
from constants import *
import numpy as np

class Pellet(object):
    def __init__(self, row, col):
        self.name = PELLET
        self.position = Vector2(col * TILEWIDTH, row * TILEHEIGHT)
        self.color = WHITE
        self.radius = int(4 * TILEWIDTH / 16)
        self.collideRadius = int(4 * TILEWIDTH / 16)
        self.points = 10
        self.visible = True

    def render(self, screen):
        if self.visible:
            p = self.position.asInt()
            pygame.draw.circle(screen, self.color, p, self.radius)

class PowerPellet(Pellet):
    def __init__(self, row, col):
        Pellet.__init__(self, row, col)
        self.name = POWERPELLET
        self.radius = int(8 * TILEWIDTH / 16)
        self.points = 50
        self.flashTime = 0.2
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer > self.flashTime:
            self.visible = not self.visible
            self.timer = 0

class PelletGroup(object):
    def __init__(self, pelletfile):
        self.pelletList = []
        self.powerPelletList = []
        self.createPelletList(pelletfile)
        self.numEaten = 0

    def update(self, dt):
        for powerpellet in self.powerPelletList:
            powerpellet.update(dt)

    def createPelletList(self, pelletfile):
        data = self.readPelletFile(pelletfile)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in ['.', '+']:
                    self.pelletList.append(Pellet(row, col))
                elif data[row][col] in ['p', 'P']:
                    pp = PowerPellet(row, col)
                    self.pelletList.append(pp)
                    self.powerPelletList.append(pp)

    def readPelletFile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')

    def isEmtpy(self):
        if len(self.pelletList) == 0:
            return True
        return False

    def render(self, screen):
        for pellet in self.pelletList:
            pellet.render(screen)