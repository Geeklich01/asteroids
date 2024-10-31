import pygame
from constants import *
from player import Player

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    dt = 0

    Player.containers = (updatable, drawable)
    player =  Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(0)
        dt = clock.tick(60)/1000
        for uptbl in updatable:
            uptbl.update(dt)
        for drbl in drawable:
            drbl.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
