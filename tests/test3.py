import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
import pygame
from src.core.sound_manager import SoundManager

pygame.init()
pantalla = pygame.display.set_mode((800, 400))
pygame.display.set_caption("pene")
reloj = pygame.time.Clock()

sounds = SoundManager()

try:
    sounds.play_music("assets/sounds/Game_Transcurrency.mp3")
    print("SONANDO MUSICAAAAA :3")
except Exception as e:
    print(f"Jarvis, no se puo reproducir, {e} Jarvis :/")

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.K_ESCAPE or event.type == pygame.KEYDOWN):
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sounds.play_music(sounds.sound_click)

    pygame.display.flip()
    reloj.tick(80)
#funciona :3
