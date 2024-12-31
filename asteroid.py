import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        screen_object = screen
        pygame.draw.circle(screen_object,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt
