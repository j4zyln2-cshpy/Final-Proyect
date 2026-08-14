import sys
import pygame
from database.db_manager import ( get_connection,guardar_partida,init_db, obtener_mejores_puntajes, cargar_partida)
from src.core.config import fps, game_title, screen_height, screen_width
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from src.ui.interfaz import InterfazUI
from states.game_over_state import GameOverState
from states.game_state import GameState
from states.menu_state import MenuState
from states.pause_state import PauseState


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.RESIZABLE
        )
        pygame.display.set_caption(f"{game_title}")
        self.clock = pygame.time.Clock()

        self.sprite_manager = SpriteManager()
        self.sound_manager = SoundManager()
        self.interfaz = InterfazUI()

        self.cargar_assets()
        init_db()

        self.font_titulo = pygame.font.Font("font/Pixeltype.ttf", 64)
        self.font_sub = pygame.font.Font("font/Pixeltype.ttf", 36)
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
            "posicion_duende": 0.0,
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
        if nuevo_estado == "MENU":
            self.sound_manager.play_music("Menu_Principal.mp3")
        elif nuevo_estado == "GAME":
            self.sound_manager.play_music("Game_Transcurrency.mp3")
        elif nuevo_estado == "PAUSE":
            self.sound_manager.play_music("Pause.mp3")
        elif nuevo_estado == "GAME_OVER":
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
            try:
                self.sound_manager.play_music("Oleada.mp3")
            except Exception as e:
                print(f"Problemas con el audio por: {e}")

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
                        self.datos_jugador["posicion_duende"]
                    )
                    self.cambiar_estado("GAME_OVER")

        self.enemigos = [e for e in self.enemigos if e["activo"]]
        self.defensores = [d for d in self.defensores if d["activo"]]
        self.proyectiles = [p for p in self.proyectiles if p["activo"]]

    def renderizar_juego(self):
        screen = self.screen

        info_pantalla = pygame.display.Info()
        self.screen_width = info_pantalla.current_w
        self.screen_height = info_pantalla.current_h

        mapa = self.sprite_manager.get_sprite("mapa")
        if mapa:
            mapota = pygame.transform.scale(mapa, (self.screen_width, self.screen_height))
            screen.blit(mapota, (0,0))


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


        elif self.estado_actual == "PAUSE":
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            cx = screen.get_width() // 2
            cy = screen.get_height() // 2

            try:
                font_p = pygame.font.Font("font/Pixeltype.ttf", 64)
                font_sub = pygame.font.Font("font/Pixeltype.ttf", 36)
            except Exception:
                font_p = pygame.font.SysFont("Arial", 50, bold=True)
                font_sub = pygame.font.SysFont("Arial", 28)

            txt_p = font_p.render("JUEGO EN PAUSA", True, (255, 215, 0))
            txt_sub = font_sub.render(
                "Presiona [ P ] para Continuar", True, (255, 255, 255)
            )

            screen.blit(txt_p, (cx - txt_p.get_width() // 2, cy - 60))
            screen.blit(txt_sub, (cx - txt_sub.get_width() // 2, cy + 20))

        elif self.estado_actual == "GAME_OVER":
   
            screen.fill((25, 5, 5))

            cx = screen.get_width() // 2
            cy = screen.get_height() // 2

            try:
                font_go = pygame.font.Font("font/Pixeltype.ttf", 72)
                font_sub = pygame.font.Font("font/Pixeltype.ttf", 36)
            except Exception:
                font_go = pygame.font.SysFont("Arial", 60, bold=True)
                font_sub = pygame.font.SysFont("Arial", 28)

            txt_go = font_go.render("PERDISTE XD", True, (255, 50, 50))
            txt_puntos = font_sub.render(
                f"Puntuacion Final: {self.datos_jugador['puntuacion']}",
                True,
                (255, 215, 0),
            )
            txt_inst = font_sub.render(
                "Presiona ESC para volver al Menu", True, (200, 200, 200)
            )

            screen.blit(txt_go, (cx - txt_go.get_width() // 2, cy - 80))
            screen.blit(
                txt_puntos, (cx - txt_puntos.get_width() // 2, cy - 10)
            )
            screen.blit(txt_inst, (cx - txt_inst.get_width() // 2, cy + 50))

        elif self.estado_actual == "MENU":
            screen.fill((15, 15, 25))
            fondo = self.sprite_manager.get_sprite("fondo_menu")
            if fondo:
                fondox = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
                screen.blit(fondox, (0, 0))

            try:
                font_titulo = pygame.font.Font("font/Pixeltype.ttf", 60)
                font_sub = pygame.font.Font("font/Pixeltype.ttf", 32)
            except Exception:
                font_titulo = pygame.font.SysFont("Arial", 50, bold=True)
                font_sub = pygame.font.SysFont("Arial", 28)

            cx = screen.get_width() // 2

            txt_m = font_titulo.render("Kingdom Defense 1D / Last Standing Defense", True, (255, 215, 0))
            txt_inst = font_sub.render("Presiona [ G ] para Jugar", True, (255, 255, 255))

            screen.blit(txt_m, (cx - txt_m.get_width() // 2, 80))
            screen.blit(txt_inst, (cx - txt_inst.get_width() // 2, 150))

            controles = [
                "[1] Poner al Espadachin ($50)",
                "[2] Poner al Hechicero ($30)",
                "[3] Poner al Caballero ($70)",
                "[4] Poner al Soldado ($40)",
                "[P] Pausa / Reanudar",
                "[S] Guardar Partida"
                "[L] Cargar Partida"
            ]



            y_offset = 220
            for linea in controles:
                color = (255, 215, 0) if "---" in linea else (220, 220, 220)
                txt_c = font_sub.render(linea, True, color)
                screen.blit(txt_c, (cx - txt_c.get_width() // 2, y_offset))
                y_offset += 35


        pygame.display.flip()

    def guardar_progreso(self):
        pos_duende = self.enemigos[0]["x"] if len(self.enemigos) > 0 else 0.0

        data = guardar_partida(
             self.datos_jugador["nombre"],
             self.datos_jugador["oleada"],
             self.datos_jugador["puntuacion"],
             self.datos_jugador["oro"],
             self.datos_jugador["vida_torre_rey"],
             self.datos_jugador["inventario"],
              pos_duende,
        )
        if data:
            print("Datos guardados con éxito")

    def cargar_partida_lol(self):
        data = cargar_partida()
        if data:
            self.datos_jugador["oro"] = data["oro"]
            self.datos_jugador["vida_torre"] = data["vida_torre"]
            self.datos_jugador["oleada"] = data["oleada_actual"]
            self.datos_jugador["inventario"] = data["inventario"]
            print("Partida cargada EXITOSAMENTE COÑO")
        else:
            print("No se encontró ninguna partida guardada previa.")

    def run(self):
        self.cambiar_estado("MENU")


        while True:
            dt = self.clock.tick(fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.estado_actual == "MENU":
                        if event.key == pygame.K_g:
                            self.reset_jugador()
                            self.cambiar_estado("GAME")


                    elif self.estado_actual == "GAME":
                        if event.key == pygame.K_p:
                            self.cambiar_estado("PAUSE")
                        elif event.key == pygame.K_1:
                            self.desplegar_defensa("espadachin")
                        elif event.key == pygame.K_2:
                            self.desplegar_defensa("hechicero")
                        elif event.key == pygame.K_3:
                            self.desplegar_defensa("caballero")
                        elif event.key == pygame.K_4:
                            self.desplegar_defensa("soldado")
                        elif event.key == pygame.K_s:
                            pos_duende = self.enemigos[0]["x"] if len(self.enemigos) > 0 and "x" in self.enemigos[0] else 0.0
                            guardar_partida(
                                self.datos_jugador["nombre"],
                                self.datos_jugador["oleada"],
                                self.datos_jugador["puntuacion"],
                                self.datos_jugador["oro"],
                                self.datos_jugador["vida_torre_rey"],
                                self.datos_jugador["inventario"],
                                pos_duende
                            )
                        elif event.key == pygame.K_l:
                            self.cargar_partida_lol()

                    elif self.estado_actual == "PAUSE":
                        if event.key == pygame.K_p:
                            self.cambiar_estado("GAME")

                    elif self.estado_actual == "GAME_OVER":
                        if event.key == pygame.K_ESCAPE:
                            self.cambiar_estado("MENU")

            if self.estado_actual == "GAME":
                self.spawn_enemigos(dt)
                self.actualizar_combate_y_movimiento(dt)

            self.renderizar_juego()

if __name__ == "__main__":
    game = Game()
    game.run()

#Python -m PyInstaller --noconsole --onefile main.py
#pyinstaller --onefile --icon=tower.ase main.py

# casi terminado