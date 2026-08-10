import pygame
from states.base_state import BaseState
import json #obvi
import os

class GameState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("Segoe UI", 25)
        self.reset()

    def reset(self):
        self.duende_x = 50.0
        self.duende_speed = 100.0
        self.torre_x = 700.0
        self.torre_hp = 100.0
        self.max_torre_hp = 100.0
        self.oro = 0
        self.puntuacion = 0
        self.is_game_over = False

    def handle_events(self, event):
        for event in event:
            if event.type == pygame.QUIT:
                self.game.change_state("MENU")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_state("PAUSE")
                elif event.key == pygame.K_s:
                    self.save_game()
                elif event.key == pygame.K_l:
                    self.load_game()

    def update(self, dt):
        if self.duende_x < self.torre_x -30:
            self.duende_x += self.duende_speed * dt
        else:
            self.torre_hp = -15 * dt
            if self.torre_hp <= 0:
                self.torre_hp = 0
                self.is_game_over = True
                self.game.change_state("GAME_OVER")

    def save_game(self, filename="savegame.json"): #aquí guardo los datos
        data = {
            "duende_x": self.duende_x,
            "duende_speed": self.duende_speed,
            "torre_x": self.torre_x,
            "torre_hp": self.torre_hp,
            "oro": self.oro,
            "puntuacion": self.puntuacion
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Su partida se ha guardado correctamente") #me lo saqué de kirby dreamland

    def load_game(self, filename="savegame.json"):
        if not os.path.exists(filename):
            print("No existe un archivo de guardado previo")
            return False
        try:
            with open(filename, "r") as file:
                print("pene")
                data = json.load(file)
                self.duende_x = data.get("duende_x", self.duende_x) #necesito recibir al "duende" creado en el constructor
                self.duende_speed =  data.get("duende_speed", self.duende_speed) #necesito reibir la velocidad del duente, tmb creado en el constructor
                self.torre_x =  data.get("torre_x", self.torre_x) #necesito recibir a la torre creado en el constructor
                self.torre_hp = data.get("torre_hp", self.torre_hp)
                self.max_torre_hp = data.get("max_torre_hp", self.max_torre_hp)
                self.oro = data.get("oro", self.oro)
                self.puntuacion = data.get("puntuacion", self.puntuacion)
            print("Partida cargada exitosamente :3")
        except FileNotFoundError:
            print("No encontré ningun archivo bro, sorry :/")

    def draw(self, surface):
        surface.fill((40,50,60))

        pygame.draw.line(surface, (100,100,100), (50,400), (750,400), 5)
        pygame.draw.rect(surface, (50,200,50), (int(self.duende_x,), 370, 30, 30))
        pygame.draw.rect(surface, (50,100,250), (self.torre_x, 330, 40, 70))

        bar_width = 100
        hp_ratio = max(0.0, self.torre_hp / self.max_torre_hp)
        pygame.draw.rect(surface, (200, 50, 50), (int(self.torre_x)- 30, 300, bar_width, 10))
        pygame.draw.rect(surface, (50, 200, 50), (int(self.torre_x) - 30, 300, int(bar_width * hp_ratio), 10))

        info = self.font.render(f"Controls: Pausa[ESC/P]; Guardar: [S], Cargar: [L]; HP Torre: {int(self.torre_hp)}", True, (255, 255, 255))
        surface.blit(info, (20,20))