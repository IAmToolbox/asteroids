# Asteroids: My second guided project from boot.dev

import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        pygame.display.flip()
        print(dt)

if __name__ == "__main__":
    main()