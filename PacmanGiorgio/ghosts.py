from constants import *
from entity import Entity
from vector import Vector2

class Ghost(Entity):
    def __init__(self, node):
        Entity.__init__(self, node)
        self.name = GHOST
        self.points = 200
        self.directionMethod = self.goalDirection

    def goalDirection(self, directions):
        distances = []
        for direction in directions:
            vec = self.node.position + self.directions[direction] * TILEWIDTH - self.targetPosition
            distances.append(vec.magnitudeSquared())
        index = distances.index(min(distances))
        return directions[index]

