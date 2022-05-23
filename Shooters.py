import pygame
screen_size = [500, 400]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('img/background.png')
planet = pygame.image.load("img/planet4.png")
#spaceship & bullet image
spaceship = pygame.image.load("img/spaceship.png")
bullet = pygame.image.load("img/bullet.png")
planet_x = 140
move_direction = "right"
fired = False
bullet_y = 320
pygame.event.get()
keys = pygame.key.get_pressed()
# for play keyevent
if keys[pygame.K_SPACE] == True:
    fired = True
if fired is True:
    bullet_y = bullet_y - 5
    if bullet_y == 50:
        fired = False
        bullet_y = 500
clock = pygame.time.Clock()
# loop for the game
keep_alive = True
while keep_alive:
    screen.blit(background, [0, 0])
    screen.blit(bullet, [140, bullet_y])
    screen.blit(spaceship, [140, 300])
    if move_direction == "right":
        planet_x = planet_x + 5
    if planet_x == 500:
        move_direction = "left"
    else:
        planet_x = planet_x - 5
    if planet_x == 0:
        move_direction = "right"
    screen.blit(planet, [planet_x, 20]) 
    pygame.display.update()
    clock.tick(60)
