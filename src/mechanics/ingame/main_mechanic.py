import pygame
from cfg import HEIGHT, WIDTH

class SpinAxis:
    def __init__(self, up, down, screen) -> None:
        self.up = up
        self.down = down
        self.screen = screen

class Puzzle:
    def __init__(self, rows, cols, screen) -> None:
        self.rows = rows
        self.cols = cols
        self.screen = screen
        self.color = (50, 50, 50)
        self.radius = 30
        self.spinaxis_list = [[SpinAxis(1, 2, self.screen) for i in range(cols)] for j in range(rows)]

    def draw(self):

        new_width = WIDTH - 200
        new_height = HEIGHT - 100

        # Рассчитываем ширину и высоту каждого ячейки
        cell_width = new_width // self.cols
        cell_height = new_height // self.rows

        # Определяем начальную позицию для центров кругов
        start_x = (new_width - (cell_width * self.cols)) // 2 + cell_width // 2
        start_y = (new_height - (cell_height * self.rows)) // 2 + cell_height // 2

        center_points = []

        # Рассчитываем координаты центров кругов
        for i in range(self.cols):
            for j in range(self.rows):
                center_points.append((start_x + cell_width * i, start_y + cell_height * j))

        print(center_points)

        # Рисуем круги
        for center in center_points:
            pygame.draw.circle(self.screen, self.color, center, self.radius)


