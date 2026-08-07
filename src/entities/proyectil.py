import pygame

class Proyectil:
    def __init__(self, x, y, objetivo_x, dano=20, velocidad=300):
        self.x = x
        self.y = y
        self.objetivo_x = objetivo_x
        self.dano = dano
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.activo = True

    def update(self, dt):
        if not self.activo:
            return

        if self.x < self.objetivox:
            self.x += self.velocidad * dt #OS LO DIJE
            if self.x >= self.objetivo_x:
                self.activo = False #llegó a destino
        else:
            self.x -= self.velocidad * dt
            if self.x <= self.objetivo_x:
                self.activo = False


        self.rect.x = int(self.x)

    def draw(self, surface):
        if self.activo:
            pygame.draw.circle(surface, (255, 165, 0), (int(self.x), int(self.y)), 9)