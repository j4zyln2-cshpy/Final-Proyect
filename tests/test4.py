import sys
import pygame
from src.core.config import (
    fps, game_title, screen_width, screen_height, ground_y_position
)
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from states.save_manager import SaveManager

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"{game_title}: Pene, digo, Prueba 4")
    reloj = pygame.time.Clock()

    sprites = SpriteManager()
    sounds = SoundManager()
    save = SaveManager()

    sprites.load_sprite("mapa", "mapa_base.png")
    sprites.load_sprite("torre", "torre_rey.png")
    sprites.load_sprite("monstruo", "monstruo.png")

    sounds.play_music("Game_Transcurrency.mp3")

    duende_x = 0
    velocidad_duende = 80
    torre_x = 700
    message = "Teclas: [S] Guardar, esc Salir"

    executing = True
    while executing:
        dt = reloj.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    executing = False

                elif event.key == pygame.K_SPACE:
                    sounds.play_sfx("click")
                    message = "VAMOS, SI ESTÁ REPRODUCIDO CARAJOOO"

                elif event.key == pygame.K_s:
                    datos_simulados = {
                        "oro": 200,
                        "puntuacion": 500,
                        "torre_vida": 300,
                        "duende_x": duende_x,
                    }
                    if save.guardar_partida(datos_simulados):
                        sounds.play_sfx("click")
                        message = (
                            "Estado guardado exitosamente en database"
                        )
                    else:
                        message = "Error al intentar guardar XD."


        if duende_x < torre_x - 40:
            duende_x += velocidad_duende * dt

        # --- RENDERIZADO / DRAW ---
        # 1. Dibujar Fondo de Mapa
        img_mapa = sprites.get_sprite(
            "mapa", size=(screen_width, screen_height)
        )
        if img_mapa:
            pantalla.blit(img_mapa, (0, 0))
        else:
            pantalla.fill((40, 50, 60))

        img_torre = sprites.get_sprite("torre", size=(80, 100))
        img_monster = sprites.get_sprite("monstruo", size=(40, 40))

        if img_torre:
            pantalla.blit(img_torre, (torre_x, ground_y_position - 80))
        if img_monster:
            pantalla.blit(img_monster, (int(duende_x), ground_y_position- 30))

        fuente = pygame.font.SysFont("Arial", 18)
        txt = fuente.render(message, True, (255, 255, 255))
        pantalla.blit(txt, (20, 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

#APROBADA MIERDA, VAMOS