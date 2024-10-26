import pygame
import math
from cfg import HEIGHT, WIDTH

class Element:
    def __init__(self, screen, typeof, position) -> None:
        self.screen = screen
        self.typeof = typeof
        self.color = (0, 0, 255)
        self.radius = 15
        self.position = position
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

class SpinAxis:
    def __init__(self, x, y, up, down, screen) -> None:
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.screen = screen
        self.radius = 10

    def draw(self):
        pygame.draw.circle(self.screen, (30, 30, 30), (self.x, self.y), self.radius)

class Key:
    def __init__(self, password, screen) -> None:
        self.password = password
        self.radius = 50
        self.position = (700, 250)
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (100, 100, 100), self.position, self.radius)

class Puzzle:
    def __init__(self, rows, cols, screen) -> None:
        self.rows = rows
        self.cols = cols

        new_width = WIDTH - 200
        new_height = HEIGHT - 100

        cell_width = new_width // self.cols
        cell_height = new_height // self.rows

        start_x = (new_width - (cell_width * self.cols)) // 2 + cell_width // 2
        start_y = (new_height - (cell_height * self.rows)) // 2 + cell_height // 2

        self.center_points = []

        for i in range(self.cols):
            for j in range(self.rows):
                self.center_points.append([start_x + cell_width * i, start_y + cell_height * j])

        self.screen = screen
        self.color = (50, 50, 50)
        self.radius = 30

        self.elements_position = self.calculate_element_positions()

        self.key = Key(1, self.screen)

    def calculate_element_positions(self):
        angles = [math.pi / 2, 3 * math.pi / 2]
        element_radius = self.radius
        positions = []

        for cx, cy in self.center_points:
            circle_positions = []
            for angle in angles:
                x = cx + element_radius * math.cos(angle)
                y = cy + element_radius * math.sin(angle)
                circle_positions.append((x, y))
            positions.append(circle_positions)

        return positions

    def draw(self):
        print(self.center_points)

        for center in self.center_points:
            pygame.draw.circle(self.screen, self.color, tuple(center), self.radius)

        for circle_elements in self.elements_position:
            for pos in circle_elements:
                element = Element(self.screen, "default", pos)
                element.draw()

        self.key.draw()