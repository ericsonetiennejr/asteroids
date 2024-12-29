#Allow the use of code from the open-source pygame library.
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0 #Represents time since the last frame was drawn.
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player_one = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        player_one.draw(screen)
        player_one.update(dt)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        print(f"Current delta time {dt}")

if __name__ =="__main__":
    main()
