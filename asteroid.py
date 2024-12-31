import pygame
import random
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rotation_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_vector = self.velocity.rotate(rotation_angle)
            second_vector = self.velocity.rotate(rotation_angle*-1)

            
            first_fragment = Asteroid(self.position.x,self.position.y,new_radius)
            second_fragment = Asteroid(self.position.x,self.position.y,new_radius)
            
            first_fragment.velocity = first_vector * 1.2
            second_fragment.velocity = second_vector * 1.2

