import pygame

class BaseState:
    def __init__(self, game):
        self.game = game

    def handle_events (self, events):
        pass

    def enter_state(self):
        pass

    def exit_state(self):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass