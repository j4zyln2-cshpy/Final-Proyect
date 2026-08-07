import pygame

class Caballero:

    def __init__(self, x=600, y=300, vida=80, ataque=15, velocidad=40):
        self.x = x
        self.y = y
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.velocidad = velocidad
        self.activo = True
        self.en_combate = False
        self.rect = pygame.Rect(self.x, self.y, 28, 36)

    def update(self, dt, lista_enemigos):
        if not self.activo:
            return
        
        enemigo_cercano = None
        for enemigo in lista_enemigos:
            if enemigo.activo and self.rect.colliderect(enemigo.rect):
                enemigo__cercano = enemigo
                break
        if enemigo_cercano:
            self.en_combate = True
            enemigo_cercano.recibir_dano(self.ataque * dt)
            self.recibir_dano(enemigo_cercano.atque * dt)
        else:
            self.en_combate = False
            self.x -= self.velocidad * dt
            self.rect.x = int(self.x)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.activo = False

    def draw(self, surface):
        if not self.activo:
            return
        pygame.draw.rect(surface, (50, 100, 220), self.rect)
