import pygame
import random
from cfg import WIDTH, HEIGHT, screen
from mechanics.glow import UnderGlow
from mechanics.particles import ParticleSystem, Particle


glow_color = (0, 255, 128)
part_sys = ParticleSystem(screen)

def draw(screen):

    screen.fill((0, 0, 0))

    under_glow = UnderGlow(glow_color, screen)
    under_glow.draw()
    if random.random() > 0.8:
        part_sys.add_particle()
    
    part_sys.update()
    part_sys.draw()

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    return 'menu' 