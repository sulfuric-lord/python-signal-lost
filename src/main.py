import pygame
from screens import main_menu
from cfg import WIDTH, HEIGHT, screen

pygame.init()

clock = pygame.time.Clock()
game_state = 'menu'


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        main_menu.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
