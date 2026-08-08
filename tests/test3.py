import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
import pygame
from src.core.sound_manager import SoundManager
from src.core.sprite_manager import SpriteManager

pygame.init()
pantalla = pygame.display.set_mode((800, 400))
pygame.display.set_caption("pene")
reloj = pygame.time.Clock()

sounds = SoundManager()
sprites = SpriteManager("assets/images")

sprites.load_sprite("duende", "duende.png")
sprites.load_sprite("torre_rey", "torre_rey.png")

try:
    sounds.play_music("Game_Transcurrency.mp3")
    print("SONANDO MUSICAAAAA :3")
except Exception as e:
    print(f"Jarvis, no se puo reproducir, {e} Jarvis :/")

executing = True

while executing:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.K_ESCAPE or event.type == pygame.KEYDOWN):
            executing = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sounds.play_music(sounds.sound_click)

    pantalla.fill((30,40,50))

    img_1 = sprites.get_sprite("duende", (60,60))
    img_2 = sprites.get_sprite("torre_rey", (100, 150))

    if img_1:
        pantalla.blit(img_1, (100, 280))
    if img_1:
        pantalla.blit(img_2, (650, 190))

    pygame.display.flip()
    reloj.tick(60)

    pygame.display.flip()
    reloj.tick(80)
#funciona :3
#LO QUE SUFRÍ LA PUTA MADRE
