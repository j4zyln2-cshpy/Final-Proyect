import pygame

class TorreBase:
    def __init__(self, x=700, y=250, vida=100, nivel=1):
        self.x = x
        self.y = y
        self.vida = vida
        self.vida_maxima = vida
        self.nivel = nivel
        self.rect = pygame.Rect(self.x, self.y, 60, 100)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def mejorar(self):
        self.nivel += 1
        self.vida_maxima += 50
        self.vida = self.vida_maxima

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 120), self.rect)

class TorreMagica(TorreBase):
    def _init__(self, x, y, vida = 150, nivel = 1):
        super().__init__(x, y)
        self.vida = vida
        self.nivel = nivel
        self.vida_maxima = vida
        self.cadencia_dispaeo = 2.0
        self.cooldown_disparo = 0.0

    def update(self, dt):
        if self.cooldown.disparo > 0:
            self.cooldown_disparo -= dt

    def mejorar(self):
            self.nivel += 1
            self.vida_maxima += 50
            self.vida = self.vida_maxima

class TorreRey(TorreBase):
    def __init__(self, x, y):
        super().__init__(x, y, vida=300)
        self.es_rey = True

    def esta_destruida(self):
        return self.vida <= 0

