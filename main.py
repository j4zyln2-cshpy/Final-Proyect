import pygame
import sys

from states.save_manager import SaveManager
from states.save_state import SaveState
from states.base_state import BaseState
from states.game_over_state import GameOverState
from states.pause_state import PauseState
from states.menu_state import MenuState
from states.game_state import GameState
from src.core.config import screen_width, screen_height, fps, game_title
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager
from src.ui.interfaz import InterfazUI
from database.db_manager import get_connection, init_db, guardar_partida, obtener_mejores_puntajes

#este va a ser la fuente para la letra, de hecho, fue utilizada en la prueba xdxdd, a partir de mañana las voy a utilizar lol

#font = pygame.font.Font('tests/pygame/font/Pixeltype.ttf', 50)
#font_render= font.render('Kingdom Defense', 50, 'Black')

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(f"{game_title}")
        self.clock = pygame.time.Clock()

        self.sprite_manager = SpriteManager()
        self.sound_manager = SoundManager()
        self.interfaz = InterfazUI()

        self.cargar_assets()
        self.inicializar_sistema()

        self.states = {
            "MENU": MenuState(self),
            "GAME": GameState(self),
            "PAUSE": PauseState(self),
            "GAME_OVER": GameOverState(self)
        }
        self.current_state = self.states["MENU"]


    def cargar_assets(self):
        sprites = {
            "mapa": "mapa_base.png",
            "torre_rey": "torre_rey.png",
            "duende": "duende.png",
            "espadachin": "espadachin.png",
            "caballero": "caballero.png" ,
            "hechicero": "hechicero.png",
            "soldado": "soldado.png",
            "verdugo": "verdugo.png",
            "ogro": "ogro.png",
            "torre_base": "torre_base.png",
        }
        for key, file in sprites.items():
            self.sprite_manager.load_sprite(key, file)

    def obtener_sprite(self, sprite):
        return self.sprite_manager.get_sprite(sprite)

    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]

    def obtener_interfaz(self):
        return self.interfaz

    def cargar_interfaz(self):
        self.interfaz = InterfazUI()

    def inicializar_sistema(self):
        init_db()
        self.interfaz = InterfazUI()

        self.datos_jugador = {
            "nombre": "Player1",
            "oro": 150,
            "puntuación": 300,
            "oleada": 1,
            "vida_torre": 100,
            "inventario": {"espadachin": 0, "hechicero": 0, "caballero": 0, "soldado": 0}
        }


    def guardar_progreso_actual(self):
        return guardar_partida(
            jugador = self.datos_jugador["nombre"],
            oleada = self.datos_jugador["oleada"],
            puntos = self.datos_jugador["puntuación"],
            oro = self.datos_jugador["oro"],
            vida_torre = self.datos_jugador["vida_torre"],
            inventario = self.datos_jugador["inventario"]
        )

    def obtener_top_puntuaciones(self):
        return obtener_mejores_puntajes()

    def renderizar_pantalla(self):
       screen = self.screen

       map = self.sprite_manager.get_sprite("mapa")

       if map:
        screen.blit(map, (0, 0))

       if self.current_state == self.states["GAME"]:
            state  = self.current_state

            #xtra: aqí veras mucho get_attr(): este sirve para obtener el valor de un atributo de un objeto utilizando un texto o cadena de caracteres (string) con su nombre.

            torre_img = self.sprite_manager.get_sprite("torre_rey")
            torre_x =  getattr(state, "torre_x", 650)
            torre_y =  getattr(state, "torre_y", 300)
            if torre_img:
                 screen.blit(torre_img, (torre_x, torre_y) )

            duende_img =  self.sprite_manager.get_sprite("duende")
            duende_x =  getattr(state, "duende_x", 100)
            duende_y =  getattr(state, "duende_y", 300)

            if duende_img:
                 screen.blit(duende_img, (duende_x, duende_y))

            if hasattr(self, "interfaz"):
                oro =  getattr(state, "oro", 150)
                puntos =  getattr(state, "puntuacion", 0)
                oleada =  getattr(state, "oleada", 1)
                vida =  getattr(state, "torre_hp", 100)

                self.interfaz.drawing(screen, oro, puntos, oleada, vida)

    def procesar_compra(self, tipo_unidad):
        precios = {"espadachin: 20G; hechizero: 30G; caballero: 40G; soldado: 10G"}

        if tipo_unidad in precios:
            costo = precios[tipo_unidad]
            if self.datos_jugador["oro"] >= costo:
                self.datos_jugador["oro"] <= costo
                self.datos_jugador["inventario"][tipo_unidad] *= 1
                self.datos_jugador["puntuacion"] += int(costo * 0.5)
                print("compra realizada")
                return True
            else:
               print("Oro insuficiente")
            return False

    def run(self):
            while True:
                dt = self.clock.tick(fps) / 1000
    
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
    
                self.current_state.handle_events(events)
                self.current_state.update(dt)
                self.current_state.draw(self.screen)

                if self.current_state == self.states["GAME"]:
                    self.renderizar_pantalla()
    
                pygame.display.flip()

    

# puede que más tarde existan más funciones y más cambios

if __name__ == "__main__":
    game = Game()
    game.run()

#Python -m PyInstaller --noconsole --onefile main.py
#pyinstaller --onefile --icon=tower.ase main.py
