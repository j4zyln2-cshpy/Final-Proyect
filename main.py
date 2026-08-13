import sys
import pygame
from database.db_manager import (
    get_connection,
    guardar_partida,
    init_db,
    obtener_mejores_puntajes,
)
from src.core.config import fps, game_title, screen_height, screen_width
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from src.ui.interfaz import InterfazUI
from states.game_over_state import GameOverState
from states.game_state import GameState
from states.menu_state import MenuState
from states.pause_state import PauseState


class GameMacro:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.RESIZABLE
        )
        pygame.display.set_caption(f"{game_title} - Macro Version")
        self.clock = pygame.time.Clock()

        self.sprite_manager = SpriteManager()
        self.sound_manager = SoundManager()
        self.interfaz = InterfazUI()

        self.cargar_assets()
        init_db()

        self.reset_jugador()

        self.enemigos = []
        self.defensores = []
        self.proyectiles = []

        self.estado_actual = "MENU"
        self.spawn_timer = 0.0

    def reset_jugador(self):
        self.datos_jugador = {
            "nombre": "Player1",
            "oro": 150,
            "puntuacion": 300,
            "oleada": 1,
            "vida_torre_rey": 100,
            "inventario": {
                "espadachin": 0,
                "hechicero": 0,
                "caballero": 0,
                "soldado": 0,
            },
        }

    def cargar_assets(self):
        sprites = {
            "mapa": "mapa_base.png",
            "fondo_menu": "fondo_menu.png",
            "monstruo": "monstruo.png",
            "icono_oro": "icono_oro.png",
            "torre_magica": "torre_magica.png",
            "torre_rey": "torre_rey.png",
            "torre_base": "torre_base.png",
            "duende": "duende.png",
            "espadachin": "espadachin.png",
            "caballero": "caballero.png",
            "hechicero": "hechicero.png",
            "soldado": "soldado.png",
            "proyectil_flecha": "proyectil_flecha.png",
            "proyectil_bomba": "proyectil_bomba.png",
        }
        for key, file in sprites.items():
            self.sprite_manager.load_sprite(key, file)

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado
        # Adaptación dinámica de la música
        if nuevo_estado == "MENU":
            self.sound_manager.play_music("Menu_Principal.mp3")
        elif nuevo_estado == "GAME":
            self.sound_manager.play_music("Game_Transcurrency.mp3")
        elif nuevo_estado == "PAUSE":
            self.sound_manager.play_music("Pause.mp3")
        elif nuevo_estado == "GAME_OVER":
            self.sound_manager.stop_music()
            self.sound_manager.play_music("Game_Over.mp3")

    def desplegar_defensa(self, tipo):
        costos = {
            "espadachin": 50,
            "hechicero": 30,
            "caballero": 70,
            "soldado": 40,
        }
        costo = costos.get(tipo, 40)

        if self.datos_jugador["oro"] >= costo:
            self.datos_jugador["oro"] -= costo

            proyectil_tipo = None
            if tipo == "soldado":
                proyectil_tipo = "proyectil_flecha"
            elif tipo == "hechicero":
                proyectil_tipo = "proyectil_bomba"

            self.defensores.append(
                {
                    "tipo": tipo,
                    "sprite": tipo,
                    "proyectil": proyectil_tipo,
                    "cooldown": 0.0,
                    "vida": 80,
                    "x": 450.0,
                    "y": 300,
                    "activo": True,
                }
            )
            print(f"Defensor {tipo} desplegado correctamente.")

    def spawn_enemigos(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= 3.0:
            self.spawn_timer = 0.0
            oleada = self.datos_jugador["oleada"]

            self.enemigos.append(
                {
                    "tipo": "duende",
                    "x": -20.0,
                    "y": 300,
                    "vel": 60.0 + (oleada * 10),
                    "vida": 40,
                    "activo": True,
                }
            )

    def actualizar_combate_y_movimiento(self, dt):
        for dfc in self.defensores:
            if not dfc["activo"]:
                continue
            if dfc["proyectil"]:
                dfc["cooldown"] += dt
                if dfc["cooldown"] >= 1.2 and len(self.enemigos) > 0:
                    dfc["cooldown"] = 0.0
                    self.proyectiles.append(
                        {
                            "sprite": dfc["proyectil"],
                            "x": dfc["x"] - 15,
                            "y": dfc["y"] + 10,
                            "vel": -220.0,
                            "activo": True,
                        }
                    )

        for p in self.proyectiles:
            if p["activo"]:
                p["x"] += p["vel"] * dt
                if p["x"] < 0:
                    p["activo"] = False

        torre_x = 650
        for ene in self.enemigos:
            if not ene["activo"]:
                continue

            bloqueado = False
            # Choque Enemigo - Defensor
            for dfc in self.defensores:
                if dfc["activo"] and abs(ene["x"] - dfc["x"]) < 30:
                    bloqueado = True
                    dfc["vida"] -= 10 * dt
                    ene["vida"] -= 20 * dt

                    if dfc["vida"] <= 0:
                        dfc["activo"] = False
                    if ene["vida"] <= 0:
                        ene["activo"] = False
                        self.datos_jugador["oro"] += 30
                        self.datos_jugador["puntuacion"] += 50
                    break

            if not bloqueado:
                ene["x"] += ene["vel"] * dt

            for p in self.proyectiles:
                if p["activo"] and abs(p["x"] - ene["x"]) < 25:
                    p["activo"] = False
                    ene["vida"] -= 25
                    if ene["vida"] <= 0:
                        ene["activo"] = False
                        self.datos_jugador["oro"] += 35
                        self.datos_jugador["puntuacion"] += 60

            if ene["x"] >= torre_x:
                ene["activo"] = False
                self.datos_jugador["vida_torre_rey"] -= 20

                if self.datos_jugador["vida_torre_rey"] <= 0:
                    self.datos_jugador["vida_torre_rey"] = 0
                    guardar_partida(
                        self.datos_jugador["nombre"],
                        self.datos_jugador["oleada"],
                        self.datos_jugador["puntuacion"],
                        self.datos_jugador["oro"],
                        self.datos_jugador["vida_torre_rey"],
                        self.datos_jugador["inventario"],
                    )
                    self.cambiar_estado("GAME_OVER")

        self.enemigos = [e for e in self.enemigos if e["activo"]]
        self.defensores = [d for d in self.defensores if d["activo"]]
        self.proyectiles = [p for p in self.proyectiles if p["activo"]]

    def renderizar_juego(self):
        screen = self.screen

        mapa = self.sprite_manager.get_sprite("mapa")
        if mapa:
            screen.blit(mapa, (0, 0))

        if self.estado_actual == "GAME":
            t_magica = self.sprite_manager.get_sprite("torre_magica")
            t_rey = self.sprite_manager.get_sprite("torre_rey")
            t_base = self.sprite_manager.get_sprite("torre_base")

            if t_magica:
                screen.blit(t_magica, (650, 150))
            if t_rey:
                screen.blit(t_rey, (650, 300))
            if t_base:
                screen.blit(t_base, (650, 450))

            for dfc in self.defensores:
                img = self.sprite_manager.get_sprite(dfc["sprite"])
                if img:
                    screen.blit(img, (dfc["x"], dfc["y"]))

            duende_img = self.sprite_manager.get_sprite("duende")
            for ene in self.enemigos:
                if duende_img:
                    screen.blit(duende_img, (ene["x"], ene["y"]))

            for p in self.proyectiles:
                p_img = self.sprite_manager.get_sprite(p["sprite"])
                if p_img:
                    screen.blit(p_img, (p["x"], p["y"]))

            self.interfaz.drawing(
                screen,
                self.datos_jugador["oro"],
                self.datos_jugador["puntuacion"],
                self.datos_jugador["oleada"],
                self.datos_jugador["vida_torre_rey"],
            )

        elif self.estado_actual == "MENU":
            fondo = self.sprite_manager.get_sprite("fondo_menu")
            if fondo:
                screen.blit(fondo, (0, 0))

        pygame.display.flip()

    def run(self):
        self.cambiar_estado("GAME")  

        #estados: GAME, MENU, GAME_OVER, PAUSE

        while True:
            dt = self.clock.tick(fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.estado_actual == "GAME":
                        if event.key == pygame.K_1:
                            self.desplegar_defensa("espadachin")
                        elif event.key == pygame.K_2:
                            self.desplegar_defensa("hechicero")
                        elif event.key == pygame.K_3:
                            self.desplegar_defensa("caballero")
                        elif event.key == pygame.K_4:
                            self.desplegar_defensa("soldado")
                        elif event.key == pygame.K_s:
                            guardar_partida(
                                self.datos_jugador["nombre"],
                                self.datos_jugador["oleada"],
                                self.datos_jugador["puntuacion"],
                                self.datos_jugador["oro"],
                                self.datos_jugador["vida_torre_rey"],
                                self.datos_jugador["inventario"],
                            )

            if self.estado_actual == "GAME":
                self.spawn_enemigos(dt)
                self.actualizar_combate_y_movimiento(dt)

            self.renderizar_juego()


if __name__ == "__main__":
    game = GameMacro()
    game.run()

#Python -m PyInstaller --noconsole --onefile main.py
#pyinstaller --onefile --icon=tower.ase main.py

# casi terminado