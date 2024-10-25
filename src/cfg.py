import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
state = 'menu'

def change_state(scene):
    global state
    state = scene