import pygame
import sys

from states.base_state import BaseState
from states.game_over_state import GameOverState
from states.pause_state import PauseState
from states.menu_state import MenuState
from states.game_state import GameState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Kingdom Defense 1D | BETA")
        self.clock = pygame.time.Clock()

        self.states = {
            "MENU": MenuState(self),
            "GAME": GameState(self)
        }
        self.current_state = self.states["MENU"]

    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000

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