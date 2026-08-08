import os
import pygame

class SpriteManager:
    def __init__(self, base_path="assets/images"): #necesitamos una ruta base para que el sprite manager sepa cuales son los sprites a utilizar
        self.base_path = base_path
        self.sprites = {}

    def load_sprite(self, name, filename):
        path = os.path.join(self.base_path, filename)
        try:
           surface = pygame.image.load(path).convert_alpha()
           self.sprites[name] = surface
           print(f"Sprite cargado: {name}")
        except pygame.error as e:
           print(f"We have problems to change the sprite: {e}, sorry :( ")

    def get_sprite(self, name, size=None):
        if name not in self.sprites:
            print(f"Warning: The sprite '{name}' it's not charged :v")
            return None

        sprite = self.sprites[name]
        if size:
            return pygame.transform.scale(sprite, size)
        return sprite
        