import pygame
import os
from .config import dir_sounds

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.ruta_base = dir_sounds
        self.sound_effects = {} #necesito identificar los efectos de clicks, como cofnrimaciones de clicks por ejemplo
        #self.sound_click = pygame.mixer.Sound("assets/sounds/Confirm_Click.mp3") -- musica de clicks xd
        #self.sound_game_over = pygame.mixer.Sound("assets/sounds/Game_Over.mp3") -- musica de game over

    def play_music(self, file_name, loop = -1, volumencito = 0.4):
      file_path = os.path.join(self.ruta_base, file_name)
      try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file_path) #carga la musica del archivo
        pygame.mixer.music.set_volume(volumencito) #lo que sería volumen al 40%
        pygame.mixer.music.play(loop) #la reproduce en un ciclo determinado 
      except Exception as e:
         print(f"Problemita al reproducir música, {e}")

    def reproducir_sonidos_clicks (self, effect_s): #lo crré principalmente porque me gusta usar soniditos xd
       if effect_s in self.sound_effects:
          self.sound_effects[effect_s].play()
       else:
          print(f"Effect not founded <(＿　＿)>")
       
    def stop_all(self):
       pygame.mixer.music.stop()
       pygame.mixer.stop()

    