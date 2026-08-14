import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'LSD.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout= 15.0)
    conn.row_factory = sqlite3.Row
    try:
       conn.execute("PRAGMA journal_mode=WAL;")
    except sqlite3.OperationalError:
        pass
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
            oleada_actual INTEGER NOT NULL,
            posicion_duende REAL NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventario_compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            espadachines INTEGER DEFAULT 0,
            hechiceros INTEGER DEFAULT 0,
            caballeros INTEGER DEFAULT 0,
            soldados INTEGER DEFAULT 0,
            mejora_nivel_torre INTEGER DEFAULT 1
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

      
def guardar_partida(jugador, oleada, puntos, oro, vida_torre, inventario, posicion_duende):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO puntuaciones (jugador, oleadas, puntos) VALUES (?, ?, ?)",
            (jugador, oleada, puntos)
        )

        cursor.execute(
            "INSERT INTO estado_partida (oro_actual, vida_torre, oleada_actual, posicion_duende) VALUES (?, ?, ?, ?)",
            (oro, vida_torre, oleada, posicion_duende)
        )

        cursor.execute(
            "INSERT INTO inventario_compras (espadachines, hechiceros, caballeros, soldados) VALUES (?, ?, ?, ?)",
            (
                inventario.get("espadachin", 0),
                inventario.get("hechicero", 0),
                inventario.get("caballero", 0),
                inventario.get("soldado", 0)
            )
        )

        conn.commit()
        print("¡Partida e inventario guardados exitosamente en LSD.db!")
        return True

    except Exception as e:
        print(f"Error al guardar en DB: {e}")
        return False
    finally:
        if conn:
            conn.close()

def obtener_mejores_puntajes(limit=10):
    with get_connection() as conn:
        cursor = conn.cursor()
        return cursor.execute("SELECT jugador, oleadas, puntos, fecha FROM puntuaciones ORDER BY puntos DESC LIMIT ?",
                              (limit,)).fetchall()


def cargar_partida():
    try:
        with get_connection() as c:
            cur = c.cursor()
            row = cur.execute("SELECT * FROM estado_partida ORDER BY id DESC LIMIT 1").fetchone()
            if row:
                inv = cur.execute("SELECT * FROM inventario_compras ORDER BY id DESC LIMIT 1").fetchone()
                inventando = {
                    "espadachin": inv["espadachines"] if inv else 0,
                    "caballeros": inv["caballeros"] if inv else 0,
                    "soldados": inv["soldados"] if inv else 0,
                    "hechiceros": inv["hechieros"] if inv else 0,
                    }
                return {
                    "oro": row["oro_actual"],
                    "vida_torre": row["vida_torre"],
                    "oleada": row["oleada_actual"],
                    "inventario": row["inventario"],
                    "posicion_duende": row["posicion_duende"]
                }
    except Exception as e:
        print(f"Error al cargar: {e}")

    return None

                

if __name__ == "__main__":
    init_db()