import pygame 
import sys

from states.base_state import BaseState
from states.game_state import GameState

class MenuState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game #self.game = game, 
        self.font = pygame.font.SysFont("Arial", 32) #en este caso, le indico al programa que la fuente para el videojuego sea Arial, de tamaño 32
        self.options = ["NUEVA PARTIDA", "CARGAR PARTIDA", "SALIR"] #opciones disponibles para el usuario
        self.selected_index = 0

    def handle_events(self, event):
            for event in event:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #creo un evento en pygame, event.type es un atributo entero que representa la categoría especifica de un evento, como presionar una tecla, click de un mouse, o cerrar la ventana
                    #en este caso una tecla fue presionada  
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                         self.select_option()
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                         self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                         self.selected_index = (self.selected_index - 1) % len(self.options)

    def select_option(self):
        selected = self.options[self.selected_index]
        if selected == "NUEVA PARTIDA":
              if "GAME" in self.game.states:
                   self.game.states["GAME"].reset()
              self.game.change_state("GAME")
        elif selected == "CARGAR PARTIDA":
             if "GAME" in self.game.states:
                  if self.game.states["GAME"].load_game():
                       self.game.change_state("GAME")
        elif selected == "SALIR":
             pygame.quit()
             sys.exit()

    def draw(self, surface):
         surface.fill((20, 20, 30))
         texto_titulo = self.font.render("KINGDOM DEFENSE 1D", True, (255, 215, 0)) #renderiza el titulo del juego
         texto_instruccion = self.font.render("Presiona ENTER para Empezar", True, (250, 250, 250)) #renderiza la instrucción para el usuario

         surface.blit(texto_titulo, (200, 200)) # esto me permite dibujar pixeles para el videojuego, en este caso me permite el tituo
         surface.blit(texto_instruccion, (160,300)) #mientras que con esto dibuja la instrucción para el usuario 

    