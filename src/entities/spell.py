import pygame

class Spell: #hechizo
    def __init__(self, nombre="BOMBITAAAAS", cooldown = 10.0, dano = 50):
        self.nombre = nombre
        self.cooldown = cooldown
        self.dano = dano
        self.tiempo_restante = 0.0

    def update(self, dt):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= dt
            if self.tiempo.restante < 0:
                self.tiempo_restante = 0

    def esta_listo(self):
        return self.tiempo_restante <= 0

    def activar(self, lista_enemigos):
        if self.esta_listo():
            for enemigo in lista_enemigos:
                enemigo.recibir_dano (self.dano)
            self.tiempo_restante = self.cooldown
            return True
        return  False

 