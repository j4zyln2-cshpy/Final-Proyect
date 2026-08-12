# COMPLETADO COJONES

import sys 
import pygame
from src.core.config import screen_width, fps, screen_height, game_title
from src.core.sprite_manager import SpriteManager
from src.core.sound_manager import SoundManager
from src.ui.interfaz import InterfazUI
from database.db_manager import init_db, guardar_partida,  obtener_mejores_puntajes

def test9():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"{game_title}: PRUEBA N° 9 DJFKJFKJFKFKFJKFJKF, o(≧∀≦)o")
    clock = pygame.time.Clock()
    init_db()

    sprite_mgr = SpriteManager()
    sound_mgr = SoundManager()
    interfaz = InterfazUI()

    sprite_mgr.load_sprite("mapa", "mapa_base.png")
    sprite_mgr.load_sprite("torre", "torre_base.png")
    sprite_mgr.load_sprite("duende", "duende.png")

    sound_mgr.play_music("Game_Transcurrency.mp3")

    # datos de prueba:
    data_player = {"oro": 100, "puntos": 0, "oleada": 1, "torre_hp": 100, "max_hp": 100}

    duende_x = 50.0
    duende_vel = 80.0
    torre_x = screen_width - 120
    game_over = False
    paused = False

    executing = True
    while executing:
        dt = clock.tick(fps) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 executing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     paused = True

                if not game_over and not paused:
                    if (event.key == pygame.K_1 and data_player["oro"] >= 20):
                        data_player["oro"] -= 20
                        data_player["puntos"] += 10
                        print("Compraste al Espadachin :3")
                    elif(event.key == pygame.K_2 and data_player["oro"] >= 25):
                        data_player["oro"] -= 25
                        data_player["puntos"] += 20
                        print("Compraste al Hechizero :0")

        if not game_over and not paused:
            duende_x += duende_vel * dt

            if duende_x <= torre_x - 40:
                data_player["torre_hp"] -= 15 * dt

                if data_player["torre_hp"] <= 0:
                    data_player["torre_hp"] = 0
                    game_over = True
                    print("JUEGO ACABADO")

        img_mapa = sprite_mgr.get_sprite("mapa")
        if img_mapa:
          screen.blit(img_mapa, (0, 0))
        else:
           screen.fill((30, 35, 45))

        img_torre = sprite_mgr.get_sprite("torre")
        img_duende = sprite_mgr.get_sprite("duende")

        if img_torre:
            screen.blit(img_torre, (torre_x, screen_height - 180))
        if img_duende and not game_over:
            screen.blit(img_duende, (duende_x, screen_height - 160))

        
        interfaz.drawing(screen, data_player["oro"],data_player["puntos"], data_player["oleada"], data_player["torre_hp"], data_player["max_hp"])

        if game_over:
            ov = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            ov.fill((150, 0, 0, 160))
            screen.blit(ov, (0,0))
            font = pygame.font.SysFont("font/Pixeltype.ttf", 40, bold= True)
            txt = font.render("Perdiste", True, (255, 255, 255))

            rect = txt.get_rect(center = (screen_width, screen_height))

            screen.blit(txt, rect)
    


        pygame.display.flip()
    # FALTA POCO PAPU, NO TE DESANIMES :3

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    test9()