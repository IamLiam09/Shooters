import pygame
screen_size = [500, 400]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('img/background.png')
planet = pygame.image.load()
# loop for the game
keep_alive = True
while keep_alive:
    screen.blit(background, [0, 0])
    pygame.display.update()