import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self,screen):
        #sub-classes will override.
        pass

    def update(self,dt):
        #sub-classes will override.
        pass

    def is_colliding_with(self,CircleShape):
        other_circle = CircleShape
        if self.position.distance_to(other_circle.position) <= self.radius + other_circle.radius:
            return True
        else:
            return False
