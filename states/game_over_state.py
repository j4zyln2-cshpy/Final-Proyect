import pygame
import os
from states.base_state import BaseState

class GameOverState(BaseState):
    def __init__(self, game):
        super().__init__(game) #"encripto" la variable game 
        self.font_title =  pygame.font.SysFont("Arial", 44, bold=True)
        self.font_options = pygame.font.SysFont("Arial", 28)
        self.options = ["REINTENTAR", "MENU PRINCIPAL"] #creo opciones para el usuario, de momento solo serán 2 xdddddd
        self.selected_index = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.select_option()

    def select_option(self):
        selected = self.options[self.selected_index]
        if selected == "REANUDAR":
            self.game.change_state("GAME")
        elif selected == "GUARDAR PARTIDA":
            if "GAME" in self.game.states:
                self.game.states["GAME"].reset()
            self.game.change_state("GAME")
        elif selected == "mMENU PRINCIPAL":
            self.game.change_state("MENU")

    def draw(self, surface):
               
               surface.fill((30, 10, 10))
       
               title_surf = self.font_title.render("PERDISTE XD", True, (230, 50, 50))
               title_rect = title_surf.get_rect(center=(surface.get_width() // 2, 200))
               surface.blit(title_surf, title_rect)
       
               for i, option in enumerate(self.options):
            
                   if i == self.selected_index:
                       color = (255, 215, 0)
                       text_str = f"{option}"
                   else:
                       color = (180, 180, 180)
                       text_str = f"{option}"
                   opt_surf = self.font_options.render(text_str, True, color)
                   opt_rect = opt_surf.get_rect(center=(surface.get_width() // 2, 300 * i * 45))
                   surface.blit(opt_surf, opt_rect)