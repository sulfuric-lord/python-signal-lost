import pygame
import random
import math
import time
import cfg
from cfg import WIDTH, HEIGHT, screen, state
from mechanics.glow import UnderGlow
from mechanics.particles import ParticleSystem, Particle
from mechanics.button import Button


glow_color = (255, 80, 124)

part_sys = ParticleSystem(screen)

buttons = []
buttons.append(Button(280, 380, 240, 50, (255, 255, 255), (200, 200, 200), (100, 100, 100), 30, screen, 'level1', "Start Game"))
buttons.append(Button(280, 460, 240, 50, (255, 255, 255), (200, 200, 200), (100, 100, 100), 30, screen, "exit", "Exit"))

button_func = ""

logo_size = 480

raw_logo = pygame.image.load("src/assets/images/SL_logo.png")
logo = pygame.transform.scale(raw_logo, (logo_size, logo_size // 2))
logo_rect = logo.get_rect(center = (WIDTH // 2, (HEIGHT // 2) - 150))

angle = 0

def draw(screen):
    global button_func

    #Изменения логотипа:
    scale_aspect = 0.9 + 0.1 * math.sin(time.time())
    logo_new_size = int(logo_size * scale_aspect)

    scaled_logo = pygame.transform.scale(raw_logo, (logo_new_size, logo_new_size // 2))

    global angle
    angle = 10 * (math.sin(time.time() / 2))
    logo = pygame.transform.rotate(scaled_logo, angle)

    logo_rect = logo.get_rect(center = (WIDTH // 2, (HEIGHT // 2) - 150))
    screen.fill((0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    under_glow = UnderGlow(glow_color, screen)
    under_glow.draw()

    if random.random() > 0.6:
        part_sys.add_particle()
    
    part_sys.update()
    part_sys.draw()

    for button in buttons:
        button.check_inp(mouse_pos)
        if button.click(mouse_pos, mouse_pressed):
            button_func = button.click_func
        
        button.draw()

    screen.blit(logo, logo_rect.topleft)

    if button_func == "exit":
        cfg.change_state("close")
    elif button_func == "level1":
        cfg.change_state("level1")