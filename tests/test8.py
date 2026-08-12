# 8° prueba, hoy implementaré interfaz, tanto en la prueba como en el juego, cambiaré la conexión de la base de datos, solo quiero jugar y convertirlo en aplicación

import sys
import pygame
from src.core.config import fps, game_title, screen_height, screen_width
from src.core.sprite_manager import SpriteManager
from src.ui.interfaz import InterfazUI
import time


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"{game_title} - Test 8: si me muero, no me recuerden")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial", 16, bold=True)

    sprite_mgr = SpriteManager()
    ui = InterfazUI()
    sprite_mgr.load_sprite("mapa", "mapa_base.png")
    sprite_mgr.load_sprite("duende", "duende.png")

    img_mapa = sprite_mgr.get_sprite("mapa")
    img_duende = sprite_mgr.get_sprite("duende")

    # estos son unos datos de prueba
    datos_jugador = {"oro": 100, "puntuacion": 150}

    paused = False #el juego NO EST'A PAUSADO POR NADA DEL MUNDO
    duende_x = 50.0
    duende_vel = 60.0

    ejecutando = True
    while ejecutando:
        dt = reloj.tick(fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True

                if not paused:
                    if (
                        event.key == pygame.K_1
                        and datos_jugador["oro"] >= 50
                    ):
                        datos_jugador["oro"] -= 50 #le resto 50 monedas de oro, las monedas de oro son 100, por lo
                        datos_jugador["puntuacion"] += 20
                        print("-Reclutado: Espadachín (-50G)")
                    elif (
                        event.key == pygame.K_2
                        and datos_jugador["oro"] >= 80
                    ):
                        datos_jugador["oro"] -= 80
                        datos_jugador["puntuacion"] += 35
                        print("Reclutado: Hechicero (-80G)")
                    elif (
                        event.key == pygame.K_3
                        and datos_jugador["oro"] >= 120
                    ):
                        datos_jugador["oro"] -= 120
                        datos_jugador["puntuacion"] += 50
                        print("Imposible pagar para el jugador en este momento")
                        time.sleep(3)
                        datos_jugador["oro"] += 120

        if not paused:
            duende_x += duende_vel * dt
            if duende_x > screen_width:
                duende_x = -40

        if img_mapa:
            pantalla.blit(img_mapa, (0, 0))

        if img_duende:
            pantalla.blit(img_duende, (int(duende_x), 260))

        ui.menu_compra(pantalla, fuente, datos_jugador)      
        ui.menu_juego(pantalla, fuente, paused)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

















































# estoy cayendo en la completa y absoluta locura, mi cuerpo no resiste