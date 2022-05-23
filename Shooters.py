import pygame
screen_size = [500, 400]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('img/background.png')
spaceship = pygame.image.load("img/spaceship.png")
bullet = pygame.image.load("img/bullet.png")
planets = ['img/planet4.png', 'img/planet3.png']
p_index = 0
planet = pygame.image.load(planets[p_index])
planet_x = 140
move_direction = "right"
fired = False
bullet_y = 320
clock = pygame.time.Clock()
# loop for the game
keep_alive = True
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        fired = True
    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 20:
            fired = False
            bullet_y = 500
    screen.blit(background, [0, 0])
    screen.blit(bullet, [140, bullet_y])
    screen.blit(spaceship, [140, 300])
    if move_direction == "right":
        planet_x = planet_x + 5
        if planet_x == 400:
            move_direction = "left"
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = "right"
    screen.blit(planet, [planet_x, 20]) 
    if bullet_y < 80 and planet_x > 120 and planet_x < 180:
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        else:
            print("YOU WIN")
            keep_alive = False
    pygame.display.update()
    clock.tick(60)
