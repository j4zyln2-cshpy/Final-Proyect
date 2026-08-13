import pygame
from states.base_state import BaseState
import sqlite3 #obvi
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
        self.oro = 150
        self.puntos = 0
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

    def save_game(self, db_filename="database/LSD.db"): #aquí guardo los datos
        #data = {
            #"duende_x": self.duende_x,
            #"duende_speed": self.duende_speed,
            #"torre_x": self.torre_x,
            #"torre_hp": self.torre_hp,
            #"oro": self.oro,
            #"puntuacion": self.puntuacion }
        try:
            conexion = sqlite3.connect(db_filename) #primero conectamos con sqlite3
            cursor = conexion.cursor() #creamos un cursor posterior a su conexión

            query = "INSERT INTO puntuaciones (jugador, oleadas, puntos) VALUES (?,?,?)" #hago una consulta e inserto los valores del jugador, oleada y puntuación actual
            values = ("Player 1", getattr(self, "oleada", 1), self.puntos) #estos son los valores actuales, Player 1 debería de cambiarse a self.name, pero eso no lo quiero hacer ahorita JAJA

            cursor.execute(query, values) #ejecutamos la query con los valores correspodneitnes
            conexion.commit() #los "imprimimos o escribimos" en el archivo .db
            conexion.close() #y cerramos la conexión con sqlite3

            print("Puntuación guardada correctamente en la Base de Datos")
        except Exception as e:
            print(f"Error al guardar en la database: {e}")

    def load_game(self):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "LSD.db") # se me había olvidado que tenía que pasar 2 veces el nombre de la ruta del directorio
        if not os.path.exists(db_path): #en el caso de que no exista el archivo de guardado
            print("No existe un archivo de guardado previo")
            return False
        try:
            conexion = sqlite3.connect(db_path)
            cursor = conexion.cursor()

            query = "SELECT oleadas, puntos FROM puntuaciones ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchone()

            conexion.close()

            if result:
               self.oleada = result[0]
               self.puntuacion = result[1]
               print(f"Partida cargada 'exitosamente'. Puntos: {self.puntos}; Oleada: {self.oleada}")
               return True
            else:
                print("No hay ningun registro previo")
                return False
        except Exception as e:
            print(f"No encontré ningun archivo bro, sorry :/, tenemos un error de {e}")

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