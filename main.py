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

        self.cargar_assets()

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
            "torre_base": "torre_base.png"
        }
        for key, file in sprites.items():
            self.sprite_manager.load_sprite(key, file)

    def obtener_sprite(self, sprite):
        return self.sprite_manager.get_sprite(sprite)

    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]

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

            pygame.display.flip()

    def save_file(self, data=None): #en realidad es solo para guardar tu registro actual, la data actual está vacía, necesitamos llenarla con la data del jugador
        if data is None:
            data = {
                "jugador": {"gold": 150,"points": 300},
                "torre_rey": {"hp": 100, "x_position": 650},
                "partida": {"oleada_actual": 1,"Nivel": 1}
            }
        return self.save_manager.guardar_partida(data)

# mañana habrán más funciones y más cambios

if __name__ == "__main__":
    game = Game()
    game.run()