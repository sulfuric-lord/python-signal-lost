import pygame
import random
import math
import time
import cfg
from cfg import WIDTH, HEIGHT, screen, state
from mechanics.glow import UnderGlow
from mechanics.particles import ParticleSystem, Particle
from mechanics.button import Button
from mechanics.ingame.main_mechanic import Puzzle
glow_color = (100, 50, 50)

puzzle = Puzzle(2, 3, screen)

def draw(screen):

    screen.fill((0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    under_glow = UnderGlow(glow_color, screen)
    under_glow.draw()

    puzzle.draw()