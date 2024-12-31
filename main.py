#Allow the use of code from the open-source pygame library.
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0 #Represents time since the last frame was drawn.
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable_objects = pygame.sprite.Group()
    drawable_objects = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable_objects,drawable_objects)
    Asteroid.containers = (asteroids,updatable_objects,drawable_objects)
    AsteroidField.containers = (updatable_objects)
    main_field = AsteroidField()
    player_one = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        for member in drawable_objects:
            member.draw(screen)
        for member in updatable_objects:
            member.update(dt)
        for member in asteroids:
            if player_one.is_colliding_with(member) == True:
                print("Game over!")
                exit()
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        print(f"Current delta time {dt}")

if __name__ =="__main__":
    main()
