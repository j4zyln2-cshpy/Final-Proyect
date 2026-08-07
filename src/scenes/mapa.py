import pygame

class Mapa:
    def __init__(self, ancho=800, alto=400):
        self.ancho = ancho
        self.alto = alto
        self.linea_camino_y = 332

    def draw(self, surface):
        surface.fill((40, 50, 60))
        pygame.draw.line(surface, (100, 100, 100), (0, self.linea_camino_y), (self.ancho, self.linea_camino_y), 5)