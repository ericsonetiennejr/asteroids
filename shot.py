import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        screen_object = screen
        pygame.draw.circle(screen_object,"white",self.position,self.radius,1)

    def update(self,dt):
        self.position += self.velocity*dt