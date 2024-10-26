import pygame
from screens import main_menu, level1
from cfg import WIDTH, HEIGHT, screen, running
import cfg

pygame.init()

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cfg.state == "menu":
        main_menu.draw(screen)
    elif cfg.state == "close":
        running = False
    elif cfg.state == "level1":
        level1.draw(screen)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
