import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_click = pygame.mixer.Sound("assets/sounds/Confirm_Click.mp3")
        self.sound_game_over = pygame.mixer.Sound("assets/sounds/Game_Over.mp3")

    def play_music(self, file_path, loop = -1):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(0.4) #lo que sería volumen al 40%
        pygame.mixer.music.play(loop)

    def play_sfx(self, sonido):
        pass