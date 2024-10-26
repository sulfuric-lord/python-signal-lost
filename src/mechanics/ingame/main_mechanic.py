import pygame
import math
from cfg import HEIGHT, WIDTH
from mechanics.button import Button


class Laser:
    def __init__(self, start_pos, is_one=True):
        self.start_pos = start_pos
        self.points = [start_pos]
        self.is_one = is_one 
        self.color = (0, 0, 255) if is_one else (255, 0, 0)

    def add_point(self, point):
        self.points.append(point)
    
    def draw(self, screen):
        if len(self.points) > 1:
            pygame.draw.lines(screen, self.color, False, self.points, 2)
class Element:
    def __init__(self, screen, typeof, position) -> None:
        self.screen = screen
        self.typeof = typeof
        if self.typeof == "DFLT":
            self.color = (30, 30, 30)
        elif self.typeof == "NOT":
            self.color = (255, 0, 0)
        elif self.typeof == "OR":
            self.color = (0, 255, 0)
        elif self.typeof == "AND":
            self.color = (0, 0, 255)
        elif self.typeof == "DBLR":
            self.color = (255, 255, 0)
        elif self.typeof == "SRC0":
            self.color = (255, 0, 255)
        elif self.typeof == "SRC1":
            self.color = (255, 255, 255)
        self.radius = 25
        self.position = position

    def process_laser(self, input_laser):
        if self.typeof == "NOT":
            return Laser(self.position, not input_laser.is_one)
        elif self.typeof == "DFLT":
            return Laser(self.position, input_laser.is_one)
        elif self.typeof == "OR":
            return Laser(self.position, input_laser.is_one or False)
        elif self.typeof == "AND":
            return Laser(self.position, input_laser.is_one and True)
        return input_laser

        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

class Key:
    def __init__(self, screen):
        self.position = (700, 250)
        self.screen = screen
        self.output_laser = None

    def update_output(self, laser):
        self.output_laser = laser

    def draw(self):
        pygame.draw.circle(self.screen, (100, 100, 100), self.position, 50)
        
class Puzzle:
    def __init__(self, rows, cols, screen, logic_list, button_offset) -> None:
        self.screen = screen
        self.button_func = ""
        self.rows = rows
        self.cols = cols
        self.logic_list = logic_list
        self.button_offset = button_offset

        self.buttons_list = []
        self.create_buttons()

        self.elements_list = self.create_elements(logic_list)

        self.key = Key(self.screen)

        self.lasers = []
        self.update_lasers()

    def update_lasers(self):
        self.lasers = []  

        for row in range(self.rows):

            start_element = self.elements_list[row * self.cols]
            if start_element.typeof in ["SRC0", "SRC1"]:

                is_one = start_element.typeof == "SRC1"
                start_pos = start_element.position
                current_laser = Laser(start_pos, is_one)

                for col in range(self.cols):
                    element = self.elements_list[row * self.cols + col]  
                    current_laser.add_point(element.position)  
                    current_laser = element.process_laser(current_laser)  


                current_laser.add_point(self.key.position)
                self.lasers.append(current_laser)
                self.key.update_output(current_laser)


    def create_buttons(self):
        count_func = 1
        for i in range(self.cols):
            for j in range(self.rows - 1):
                print("Кнопка сделана")
                button_x = (WIDTH - 200) // self.cols * i + (WIDTH - 200) // self.cols // 2
                button_y = (HEIGHT - 100) // self.rows * (j + 1)
                top_element_index = j + i * self.rows
                bottom_element_index = (j + 1) + i * self.rows
                
                self.buttons_list.append(
                    Button(
                        button_x - self.button_offset[0], 
                        button_y - self.button_offset[1], 
                        75, 25, 
                        (255, 255, 255), 
                        (200, 200, 200), 
                        (100, 100, 100), 
                        15, 
                        self.screen, 
                        (top_element_index, bottom_element_index),
                        "Change"
                    )
                )
                count_func += 1

    def create_elements(self, logic_list):
        elements_list = []
        logic_list_counter = 0
        for i in range(self.cols):
            for j in range(self.rows):
                x = (WIDTH - 200) // self.cols * i + (WIDTH - 200) // self.cols // 2
                y = (HEIGHT - 100) // self.rows * j + (HEIGHT - 100) // self.rows // 2
                elements_list.append(Element(self.screen, logic_list[logic_list_counter], [x, y]))
                logic_list_counter += 1
        return elements_list


    def swap_logic_indexes(self, index1, index2):

        pos1 = self.elements_list[index1].position
        pos2 = self.elements_list[index2].position

        self.elements_list[index1], self.elements_list[index2] = self.elements_list[index2], self.elements_list[index1]
        
        self.elements_list[index1].position = pos1
        self.elements_list[index2].position = pos2

        self.update_lasers()

    def draw(self):
        
        for element in self.elements_list:
            element.draw()
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        for button in self.buttons_list:
            button.check_inp(mouse_pos)
            if button.click(mouse_pos, mouse_pressed):
                indices = button.click_func 
                self.swap_logic_indexes(indices[0], indices[1])
            button.draw()

        for laser in self.lasers:
            laser.draw(self.screen)

        self.key.draw()