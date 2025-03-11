# Asteroids: My second guided project from boot.dev

import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots, drawable, updatable)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        print(asteroids)
        print(shots)

        asteroids_to_kill = []
        bullets_to_kill = []
        for asteroid in asteroids:
            if asteroid.collission(player) == True:
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collission(bullet) == True:
                    asteroids_to_kill.append(asteroid)
                    bullets_to_kill.append(bullet) # pLEASE WORK
        for asteroid in asteroids_to_kill:
            asteroid.split()
        for bullet in bullets_to_kill:
            bullet.kill()
        #for asteroid in asteroids:
            #for bullet in shots:
                #print("Checking for collission...")
                #if asteroid.collission(bullet) == True:
                    #asteroid.kill()
                    #bullet.kill()
                    #print("This should destroy the asteroid and the bullet")
        pygame.display.flip()
        #print(dt)

if __name__ == "__main__":
    main()