import pygame
import os
import json
from src.core.config import dir_database

class SaveManager:
    def __init__(self, filename="savegame.json"):
        self.filepath = os.path.join(dir_database, filename)

    def guardar_partida(self, data_game):
        try:
           os.makedirs(os.path.dirname(self.filepath), exist_ok = True)
          
           with open(self.filepath, "w", encoding="utf-8") as pene:
               json.dump(data_game, pene, indent = 4)
           print(f"Partida guardada en {self.filepath}")
           return True
        except Exception as e:
            print(f"Error al guardar partida: {e}")
            return None

    def cargar_partida(self):
        if not os.path.exists(self.filepath):
            print("No pudimos cargar el archivo papi :( ")
            return None

        try:
            with open(self.filepath, "r", encoding="utf-8") as nose:
                data = json.load(nose)
            print("Partida cargada exitosamente")
            return data
        except Exception as e:
            print(f"Error al cargar: {e}")
            return None