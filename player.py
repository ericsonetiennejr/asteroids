from constants import *
from circleshape import CircleShape
import pygame
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation+90)*self.radius /1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self,dt):
        movement_vector = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += movement_vector * PLAYER_SPEED*dt
    
    def update(self,dt):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_a]:
            self.rotate(dt)
        
        if keys[pygame.K_s]:
            self.move(dt*-1)

        if keys[pygame.K_d]:
            self.rotate(dt*-1)



    def draw(self,screen):
        screen_object = screen
        pygame.draw.polygon(screen_object,"white",self.triangle(),width=2)



