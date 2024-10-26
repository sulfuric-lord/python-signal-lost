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


puzzle = Puzzle(3, 3, screen, ["SRC1", "SRC0", "SRC1",
                               "DFLT", "NOT", "DFLT",
                               "NOT", "DFLT", "NOT"]
                               ,[37, 15])

def draw(screen):

    screen.fill((0, 0, 0))

    under_glow = UnderGlow(glow_color, screen)
    under_glow.draw()

    puzzle.draw()