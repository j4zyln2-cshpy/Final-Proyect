import pygame
from entities.enemigo import Enemigo
from entities.proyectil import Proyectil
from entities.spell import Spell
from scenes.mapa import Mapa
from entities.torre import Torre

class EscenaJuego:
    def __init__(self, mapa, proyectil, spell, torre, enemigo):
        self.mapa = Mapa()
        self.proyectil = Proyectil()
        self.spell = Spell()
        self.torre = Torre()
        self.enemigo = Enemigo()
        self.oro = 100
        self.puntuacion = 0

    def generar_oleada(self):
        self.enemigos.append(Enemigo(tipo="duende", x=0, y=300))

    def update(self,dt):
        self.spell.update(dt)
        for enemigo in self.enemigos:
            enemigo(dt)
            if enemigo.activo and enemigo.rect.colliderect(self.torre.rect):
                self.torre.recibir_dano(10)
                enemigo.activo = False

            for proyectil in self.proyectiles:
                proyectil.update(dt)

            self.enemigos = [e for e in self.enemigos if e.activo]
            self.proyectiles = [j for j in self.proyectiles if j.activo]
        #actualizado para ser posterior

    def draw(self, surface):
        self.mapa.draw(surface)
        self.torre.draw(surface)
        for enemigo in self.enemigos:
            enemigo.draw(surface)
        for proyectil in self.proyectiles:
            proyectil.draw(surface)
        #actualizado para ser posterior
