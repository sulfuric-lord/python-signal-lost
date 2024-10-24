import pygame
import random
from cfg import WIDTH, HEIGHT

class Particle:
    def __init__(self, x, y, color, velocity, lifetime) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.velocity =  velocity
        self.lifetime = lifetime
        self.init_lifetime = lifetime
        self.size = random.randint(1, 10)

        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.surface.fill(color)
    
    def update(self):
        self.y -= self.velocity

        fade_factor = max(0, self.lifetime / self.init_lifetime)
        alpha = int((fade_factor / 2) * 255)

        self.surface.set_alpha(alpha)

        self.lifetime -= 1
    
    def is_alive(self):
        return self.lifetime > 0
    
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    

class ParticleSystem:
    def __init__(self, screen) -> None:
        self.particles = []
        self.screen = screen

    def add_particle(self):
        part = Particle(random.randint(0, WIDTH), HEIGHT - 10, (255, 255, 255), random.randint(1, 5), random.randint(10, 50))
        self.particles.append(part)
    
    def update(self):
        for p in self.particles:
            p.update()
        
        self.particles = [p for p in self.particles if p.is_alive()]
        #Отладочные данные:
        #print(len(self.particles))
    
    def draw(self):
        for particle in self.particles:
            particle.draw(self.screen)