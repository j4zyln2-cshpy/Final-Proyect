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
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS estado_partida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            oro_actual INTEGER NOT NULL,
            vida_torre INTEGER NOT NULL,
            oleada_actual INTEGER NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventario_compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            espadachines INTEGER DEFAULT 0,
            hechiceros INTEGER DEFAULT 0,
            caballeros INTEGER DEFAULT 0
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS configuracion_audio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            volumen_musica REAL DEFAULT 0.8,
            volumen_sfx REAL DEFAULT 1.0
        )
    """
    )
    conn.commit()

      

def guardar_partida(jugador, oleada, puntos, oro, vida_torre, inventario):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO puntuaciones (jugador, oleadas, puntos) VALUES (?, ?, ?)",
            (jugador, oleada, puntos),
        )

        cursor.execute(
            "INSERT INTO estado_partida (oro_actual, vida_torre, oleada_actual) VALUES (?, ?, ?)",
            (oro, vida_torre, oleada),
        )

        cursor.execute(
            "INSERT INTO inventario_compras (espadachines, hechiceros, caballeros) VALUES (?, ?, ?)",
            (
                inventario.get("espadachin", 0),
                inventario.get("hechicero", 0),
                inventario.get("caballero", 0),
            ),
        )

        conn.commit()
        conn.close()
        print("¡Partida e inventario guardados exitosamente en LSD.db!")
        return True
    except Exception as e:
        print(f"Error al guardar en DB: {e}")
        return False

def obtener_mejores_puntajes(limit=10):
    with get_connection() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT jugador, oleadas, puntos, fecha FROM puntuaciones ORDER BY puntos DESC LIMIT ?",
                              (limit,)).fetchall()

if __name__ == "__main__":
    init_db()