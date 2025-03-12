import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game object groups to be drawn and updated
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #assign classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #instantiate player and asteroid spawner objects
    player = Player(PLAYER_X, PLAYER_Y)
    field = AsteroidField()
    
    #log player spawn
    print("player created at: ", player.position, "with radius: ", player.radius)
    

    


    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000

        #update all objects in updatable
        for object in updatable:
            object.update(dt)
        
        #check collision between player and asteroids
        for object in asteroids:
            player.checkCollision(object)

        #paint screen black
        screen.fill((0,0,0))
        
        #draw all objects to screen
        for object in drawable:
            object.draw(screen)
       
       
        pygame.display.flip()
        
        
        
        



if __name__ == "__main__":
    main()