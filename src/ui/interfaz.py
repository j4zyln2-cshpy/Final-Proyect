import pygame

class InterfazUI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self, surface, juego):
        texto_oro = self.font.render(f"Oro: {juego.oro}", True, (255, 215, 0))
        texto_vida = self.font.render(f"Torre HP: {juego.torre.vida/{juego.torrevida.maxima}}", True, (255, 255, 255))

        cd = int(juego.spell.tiempo_restante)
        if cd == 0:
            txt_spell = "Hechizo: Listo"
        else:
            f"Hechizo CD: {cd}s"

        texto_spell = self.font.render(txt_spell, True, (100, 200, 255))

        surface.blit(texto_oro, (20,20))
        surface.blit(texto_vida, (20,50))
        surface.blit(texto_spell, (20,80))