import pygame

class InterfazUI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 20)

    def menu_juego(self, screen, fuente, game_pause):
        width, height = screen.get_size()
        pygame.draw.line(screen, (70, 80, 100), (0, 50), (width, 50), 2)
        pygame.draw.rect(screen, (20, 25, 35), (0, 0, width, 50))

        txt_menu = fuente.render (
            "[ESC] Pausa | [S] Guardar Juego", True, (200, 212, 225)
        )
        screen.blit(txt_menu, (20, 15))

        if game_pause:
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            txt_pausa = fuente.render(
            "PAUSE", True, (255, 220, 100)
            )
            rect_pausa = txt_pausa.get_rect(
            center=(width // 2, height // 2)
            )
            screen.blit(txt_pausa, rect_pausa)

    def menu_compra(self,  screen, font, data_player ):
        gold = data_player.get("oro", 150)
        points = data_player.get("puntuación", 0)

        ancho, alto = screen.get_size()
        panel = 70
        panel_y = alto - panel

        pygame.draw.rect(screen, (15, 20, 28), (0, panel_y, ancho, panel))
        pygame.draw.line(screen, (210, 170, 250), (0, panel_y), (ancho, panel), 2)

        txt_gold = font.render(f"Oro: {gold} G ", True, (255, 215, 0))
        txt_points = font.render(f"Puntos: {points}", True, (180, 220, 255))
        screen.blit(txt_gold, (20, panel_y + 25))
        screen.blit(txt_points, (140, panel_y + 25))


        options = [
            ("[1] Espadachin (50G)", gold >= 50),
            ("[2] Hechicero (80G)", gold >= 80), 
            ("[3] Caballero (120G)", gold >= 120)
        ]
        x_offset = 280
        for text, access in options:
            color = (100, 230, 120) if access else (150, 70, 70)
            txt = font.render(text, True, color)
            screen.blit(txt, (x_offset, panel_y + 25))
            x_offset += 170

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

    def drawing(self, pantalla, oro, puntos, oleada, vida_torre, max_vida = 100):

        txt_info = f"Oro: {oro}, Puntos: {puntos}, Oleada: {oleada}"
        img_info = self.font.render(txt_info, True, (255, 255, 255))
        pantalla.blit(img_info, (20, 20))

        ancho_barra_vida = 200
        alto_barra = 20
        x_barra = 20
        y_barra = 55

        vida_porcentaje = max(0, vida_torre) / max_vida
        pygame.draw.rect(pantalla, (200, 0, 0), (x_barra, y_barra, ancho_barra_vida, alto_barra))
        pygame.draw.rect(pantalla, (0, 200, 0), (x_barra, y_barra, int(ancho_barra_vida * vida_porcentaje), alto_barra))
        pygame.draw.rect(pantalla, (255, 255, 255), (x_barra, y_barra, ancho_barra_vida, alto_barra), 2)

        txt_tienda= "[1]Espadachin (10G), [2] Cabllero (50G), [3] Hechicero (30G), [4] Soldado (20G)"
        img_tienda= self.font.render(txt_tienda, True, (240, 200, 80))
        pantalla.blit(img_tienda, (20, 80))



       