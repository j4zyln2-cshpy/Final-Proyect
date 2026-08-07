import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.entities.enemigo import Enemigo
from src.entities.torre import TorreRey

duende = Enemigo(tipo="Duende", x=0, velocidad=100)
torre = TorreRey(x=700, y=300)
dt = 0.016  

for paso in range(1000):
        duende.update(dt)
        if abs(duende.x - torre.x) <= 20:
            torre.recibir_dano(10)
            print(f"Impacto en paso {paso}, Vida Torre: {torre.vida}")
            break