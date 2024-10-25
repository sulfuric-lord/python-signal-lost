import pygame
import math
from cfg import WIDTH, HEIGHT
import time

class UnderGlow:
    def __init__(self, color, screen):
        self.color = color
        self.iterations = 16
        self.screen = screen

    def draw(self):
        for i in range(1, self.iterations + 1):
            new_color = []
            for j in self.color:
                new_color.append(min(255, math.ceil(j / (i * 3))))

            height_var = int(30 * (math.sin(time.time())))

            pygame.draw.rect(
                self.screen, 
                tuple(new_color), 
                pygame.Rect(0, HEIGHT + 50 - i * 50 - height_var, WIDTH, 50)
            )
        #Отладочные данные:
        #print(f"hv: {height_var}, time.time: {time.time()}, current_time: {current_time}, sin(time): {math.sin(time.time())}")
