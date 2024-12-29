#Allow the use of code from the open-source pygame library.
import pygame
from constants import *
def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0 #Represents time since the last frame was drawn.
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick()/1000 #Convert from ms to s.
        print(f"Current delta time {dt}")

if __name__ =="__main__":
    main()