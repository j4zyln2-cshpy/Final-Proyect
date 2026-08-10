import sys
import pygame
from src.core.config import screen_height, screen_width, fps, game_title
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from states.save_manager import SaveManager

def bolainas():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"prueba 7 de {game_title} xd: hoy será la integración casi total")
    clock = pygame.time.Clock()

    sprite_mgr = SpriteManager()
    sound_mgr = SoundManager()
    save_dt = SaveManager()

    sprite_mgr.load_sprite("mapa", "mapa_base.png")
    sprite_mgr.load_sprite("duende", "duende.png")
    sprite_mgr.load_sprite("torre_rey", "torre_rey.png")

    img_mapa = sprite_mgr.get_sprite("mapa")
    img_duende = sprite_mgr.get_sprite("duende")
    img_torre = sprite_mgr.get_sprite("torre_rey")

    data_saved = save_dt.cargar_partida()

    if data_saved:
        oro = data_saved["jugador"]["gold"]
        puntos = data_saved["jugador"]["points"]
        vida_torre = data_saved["torre_rey"]["hp"]
    else:
        oro. puntos, vida_torre = 100, 0, 150

    duende_x = 50
    duende_vel = 60
    torre_x = 600
    duende_rango = 30

    cooldown_ataque = 0.8
    tiempo_acumulado = 0.0
    tim_msj = 0
    font = pygame.font.SysFont("font/Pixeltype.ttf", 50)

    executing = True
    while executing:
        dt = clock.tick(fps) / 1000 #a 60 fps el que se pregunte nojoddkjdkffjkgdjgkdjgdkjgkgjkgjgkjgkjgkgjkgjkgjgkjgkjgkg malditos geis

        for event in pygame.event.get():
            if event.type == pygame.QUIT and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    executing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                 statement = {
                      "jugador": {"oro": oro, "puntaje": puntos},
                      "torre_rey": {"vida": vida_torre, "posicion_x": torre_x},
                      "partida": {"oleada_actual": 1, "nivel": 1} #el primer nivel es en el bosque
                 }
                 if save_dt.guardar_partida(statement):
                      tim_msj = 2.0

        distance = abs((duende_x + 40)- torre_x)
        colision = distance <= duende_rango

        if not colision: duende_x += duende_vel * dt
        else: 
             tiempo_acumulado += dt
             if tiempo_acumulado >= cooldown_ataque and vida_torre > 0:
                  vida_torre = max(0, vida_torre - 10)
                  tiempo_acumulado = 0.0 #llega a 0, fin

        if img_mapa:
             pantalla.blit(img_mapa, (0,0))
        else:
             pantalla.fill((40, 45, 55))

        if img_duende:
             pantalla.blit(img_duende, (int(duende_x), 260))
        if img_torre:
             pantalla.blit(img_torre, (int(torre_x), 200))

        txt_stats = font.render(
            f"Oro: {oro}; Puntos: {puntos}, Vida de La Torre: {vida_torre} HP" , True, (255, 255, 255),
        )
        pantalla.blit(txt_stats, (20, 20))

        if tim_msj > 0:
             tim_msj -= dt
             tt_save = font.render("Partida guardada xd", True, (80, 240, 120))
             pantalla.blit(tt_save, (400, 20))

        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    bolainas()