import pygame

class Enemigo:
    def __init__(self, tipo="Duende", x=0, y=300, velocidad=100, vida=50):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.vida = vida
        self.max_vida = vida
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.activo = True

    def update(self, dt):
        if not self.activo:
            return

        self.x += self.velocidad * dt
        self.rect.x = int(self.x)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.activo = False

    def draw(self, surface):
        if not self.activo:
            return
        if self.tipo == "Duende":
            color = (0, 200, 0)
        else:
            color = (200, 50, 50)
        pygame.draw.rect(surface, color, self.rect)