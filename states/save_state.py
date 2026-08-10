import pygame
from states.save_manager import SaveManager
from states.base_state import BaseState

class SaveState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = self.font.SysFont("Arial" , 20)
        self.save_manager = SaveManager()
        self.mensaje = "Presiona 'G' para Guardar o 'ESC' para irte a donde quieras XD"

    def handle_events(self, events):
       for event in events:
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   self.game.change_state("GAME")

               elif event.key == pygame.K_g:
                   game_scene = self.game.estado_juego
                   data = {
                       "oro": game_scene.oro,
                       "puntuacion": game_scene.puntuacion,
                       "torre_vida": game_scene.torre.vida,
                       "enemigos": [
                           {"tipo": e.tipo, "x": e.x, "vida": e.vida} for e in game_scene.enemigos if e.activo
                       ],
                   }

                   if self.save_manager.guardar_partida(data):
                       self.mensaje = "Partida Guardada, Presiona ESC"
                   else:
                       self.mensaje = "Error al guardar. Intenta de nuevo"
       
    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((20, 20, 30))
        txt = self.font.render(self.mensaje, True, (255, 215, 0))
        surface.blit(txt, (150, 190))