import pygame
import sys

#pd: todavía no voy a añadir ni el savemanager ni el save state, solo quiero confirmar algunas cosas antes de hacer colisiones y guardado
from states.base_state import BaseState
from states.game_over_state import GameOverState
from states.pause_state import PauseState
from states.menu_state import MenuState
from states.game_state import GameState
from src.core.config import screen_width, screen_height, fps, game_title
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager

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
            "torre": "torre_rey.png",
            "duende": "duende.png",
            "espadachin": "espadachin.png",
        }
        for key, file in sprites.items():
            self.sprite_manager.load_sprite(key, file)

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

if __name__ == "__main__":
    game = Game()
    game.run()