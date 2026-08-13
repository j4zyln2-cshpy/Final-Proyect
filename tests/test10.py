# still in development

import sys
import pygame
import sqlite3
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.core.config import fps, game_title, screen_height, screen_width
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from database.db_manager import get_connection, init_db, guardar_partida, obtener_mejores_puntajes
from src.ui.interfaz import InterfazUI

class Tropas:
    def __init__(self, tipo, x, vel):
        self.tipo = tipo
        self.x = x
        self.vel = vel
        self.activo = True

def test_10():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"{game_title} - Test 10: ultima prueba? o((>ω< ))o")
    reloj = pygame.time.Clock()

    init_db()

    sprite_mgr = SpriteManager()
    sound_mgr = SoundManager()
    interfaz = InterfazUI()

    sprites_dict = {
        "mapa": "mapa_base.png",
        "ogro": "ogro.png",
        "torre": "torre_rey.png",
        "duende": "duende.png",
        "espadachin": "espadachin.png",
        "hechicero": "hechicero.png",
        "caballero": "caballero.png",
        "soldado": "soldado.png",
    }
    for key, val in sprites_dict.items():
        sprite_mgr.load_sprite(key, val)

    sound_mgr.play_music("Game_Transcurrency.mp3")

    partida = {
        "jugador": "Jugador1",
        "oro": 200,
        "puntos": 0,
        "oleada": 1,
        "torre_hp": 100,
        "max_hp": 100,
        "espadachines": 0,
        "hechiceros": 0,
        "caballeros": 0,
        "soldados": 0
    }

    enemigos = []
    aliados = []
    torre_x = screen_width - 140
    spawn_timer = 0.0
    game_over = False
    pausado = False
    mensaje_db = ""
    timer_mensaje = 0.0

    def guardar_sqlite():
        nonlocal mensaje_db, timer_mensaje
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO puntuaciones (jugador, oleadas, puntos) VALUES (?, ?, ?)",
                (partida["jugador"], partida["oleada"], partida["puntos"]),
            )
            cursor.execute(
                "INSERT INTO estado_partida (oro_actual, vida_torre, oleada_actual) VALUES (?, ?, ?)",
                (partida["oro"], int(partida["torre_hp"]), partida["oleada"]),
            )
            cursor.execute(
                "INSERT INTO inventario_compras (cant_espadachines, cant_hechiceros, cant_caballeros, cant_soldados) VALUES (?, ?, ?)",
                (
                    partida["espadachines"],
                    partida["hechiceros"],
                    partida["caballeros"],
                    partida["soldados"]
                ),
            )
            conn.commit()
            conn.close()
            mensaje_db = "¡GUARDADO EN LSD.DB EXITOSO!"
            timer_mensaje = 2.0
        except Exception as e:
            mensaje_db = f"ERROR AL GUARDAR: {e}"
            timer_mensaje = 2.0

    def cargar_sqlite():
        nonlocal mensaje_db, timer_mensaje
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT oro_actual, vida_torre, oleada_actual FROM estado_partida ORDER BY id DESC LIMIT 1"
            )
            res_estado = cursor.fetchone()
            cursor.execute(
                "SELECT cant_espadachines, cant_hechiceros, cant_caballeros, cant_soldados FROM inventario_compras ORDER BY id DESC LIMIT 1"
            )
            res_inv = cursor.fetchone()
            conn.close()

            if res_estado:
                partida["oro"] = res_estado[0]
                partida["torre_hp"] = res_estado[1]
                partida["oleada"] = res_estado[2]
            if res_inv:
                partida["espadachines"] = res_inv[0]
                partida["hechiceros"] = res_inv[1]
                partida["caballeros"] = res_inv[2]
                partida["soldados"] = res_inv[3]

            mensaje_db = "¡PARTIDA CARGADA DESDE LSD.DB!"
            timer_mensaje = 2.0
        except Exception as e:
            mensaje_db = f"ERROR AL CARGAR: {e}"
            timer_mensaje = 2.0

    ejecutando = True
    while ejecutando:
        dt = reloj.tick(fps) / 1000.0

        if timer_mensaje > 0:
            timer_mensaje -= dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = not pausado

                    if pausado:
                        sound_mgr.play_music("Pause.mp3")
                    else:
                        sound_mgr.play_music("Game_Transcurrency.mp3")

                if not game_over and not pausado:
                    if event.key == pygame.K_1 and partida["oro"] >= 50:
                        partida["oro"] -= 50
                        partida["espadachines"] += 1
                        partida["puntos"] += 30
                        aliados.append(Tropas("espadachin", 150, 100.0))
                    elif event.key == pygame.K_2 and partida["oro"] >= 100:
                        partida["oro"] -= 100
                        partida["hechiceros"] += 1
                        partida["puntos"] += 70
                        aliados.append(Tropas("hechicero", 150, 80.0))
                    elif event.key == pygame.K_3 and partida["oro"] >= 150:
                        partida["oro"] -= 150
                        partida["caballeros"] += 1
                        partida["puntos"] += 120
                        aliados.append(Tropas("caballero", 150, 60.0))
                    elif event.key == pygame.K_4 and partida["oro"] >= 80:
                        partida["oro"] -= 80
                        partida["soldados"] += 1
                        partida["puntos"] += 100
                        aliados.append(Tropas("soldado", 150, 60.0))

                    elif event.key == pygame.K_s:
                        guardar_sqlite()
                    elif event.key == pygame.K_l:
                        cargar_sqlite()

        if not game_over and not pausado:
            spawn_timer += dt
            if spawn_timer >= 3.5:
                spawn_timer = 0.0
                enemigos.append(
                    Tropas("duende", 0, 70.0 + (partida["oleada"] * 10))
                )
                sound_mgr.play_music("Oleada.mp3")

            for ene in enemigos:
                if ene.activo:
                    ene.x += ene.vel * dt
                    if ene.x >= torre_x - 30:
                        partida["torre_hp"] -= 12 * dt
                        if partida["torre_hp"] <= 0:
                            partida["torre_hp"] = 0
                            game_over = True
                            sound_mgr.play_music("Game_Over.mp3")

            for ali in aliados:
             img = sprite_mgr.get_sprite(ali.tipo)
             if img:
                pantalla.blit(img, (int(ali.x), screen_height - 150))
             else:
                pygame.draw.rect(
                    pantalla,
                    (50, 200, 50),
                    (int(ali.x), screen_height - 150, 30, 30),
                )
    
            for ali in aliados:
                for ene in enemigos:
                    if ali.activo and ene.activo and abs(ali.x - ene.x) < 25:
                        ali.activo = False
                        ene.activo = False
                        partida["oro"] += 35
                        partida["puntos"] += 50

            enemigos = [e for e in enemigos if e.activo]
            aliados = [a for a in aliados if a.activo]

            if partida["puntos"] >= partida["oleada"] * 300:
                partida["oleada"] += 1
                partida["oro"] += 100

        img_mapa = sprite_mgr.get_sprite("mapa")
        if img_mapa:
            pantalla.blit(img_mapa, (0, 0))
        else:
            pantalla.fill((25, 30, 40))


        img_torre = sprite_mgr.get_sprite("torre")
        if img_torre:
            pantalla.blit(img_torre, (torre_x, screen_height - 180))


        for ene in enemigos:
            img = sprite_mgr.get_sprite("duende")
            img2 = sprite_mgr.get_sprite("ogro")
            if img:
                pantalla.blit(img, (int(ene.x), screen_height - 150))
            else:
                 pygame.draw.rect(
                 pantalla,
                 (200, 50, 50),
                 (int(ene.x), screen_height - 150, 30, 30),
                 )

        for ali in aliados:
            img = sprite_mgr.get_sprite(ali.tipo)
            if img:
                pantalla.blit(img, (int(ali.x), screen_height - 150))
            else:
                pygame.draw.rect(
                    pantalla,
                    (50, 200, 50),
                    (int(ali.x), screen_height - 150, 30, 30),
                )

        interfaz.drawing(
            pantalla,
            partida["oro"],
            partida["puntos"],
            partida["oleada"],
            int(partida["torre_hp"]),
            partida["max_hp"],
        )

        if timer_mensaje > 0:
            fuente_msg = pygame.font.SysFont("Arial", 22, bold=True)
            txt = fuente_msg.render(mensaje_db, True, (255, 230, 0))
            pantalla.blit(txt, (screen_width // 2 - 140, 120))

        if pausado:
            overlay = pygame.Surface(
                (screen_width, screen_height), pygame.SRCALPHA
            )
            overlay.fill((0, 0, 0, 150))
            pantalla.blit(overlay, (0, 0))
            fuente_p = pygame.font.SysFont("Arial", 36, bold=True)
            pantalla.blit(
                fuente_p.render("PAUSA", True, (255, 255, 255)),
                (screen_width // 2 - 120, screen_height // 2),
            )
            sound_mgr.play_music("Pause.mp3")

        if game_over:
            overlay = pygame.Surface(
                (screen_width, screen_height), pygame.SRCALPHA
            )
            overlay.fill((120, 0, 0, 180))
            pantalla.blit(overlay, (0, 0))
            fuente_go = pygame.font.SysFont("Arial", 42, bold=True)
            pantalla.blit(
                fuente_go.render(
                    "GAME OVER: LA TORRE CAYÓ", True, (255, 255, 255)
                ),
                (screen_width // 2 - 220, screen_height // 2 - 20),
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    test_10()