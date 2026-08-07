import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'LSD.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntuaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jugador TEXT NOT NULL,
        oleadas INTEGER NOT NULL,
        puntos INTEGER NOT NULL,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
    conn.commit()

def guardar_partida(jugador, oleadas, puntos):
    with get_connection() as conn: 
         cursor = conn.cursor()
         cursor.execute("INSERT INTO puntuaciones (jugador, oleadas, puntos) VALUES (?,?,?)",(jugador,oleadas,puntos))
         conn.commit()

def obtener_mejores_puntajes(limit=10):
    with get_connection() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT jugador, oleadas, puntos, fecha FROM puntuaciones ORDER BY puntos DESC LIMIT ?",
                              (limit,)).fetchall()

if __name__ == "__main__":
    init_db()