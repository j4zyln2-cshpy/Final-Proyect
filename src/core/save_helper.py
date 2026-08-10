from states.save_manager import SaveManager

def generate_savegame(gold, points, life_tower, tower_x_position = 650, oleada = 1):
    save_manager= SaveManager("database/savegame.json")

    data = {
        "jugador": {"gold": gold, "points": points, },
        "torre_rey": {"hp": life_tower, "x_position": tower_x_position},
        "partida": {"oleada_actual": oleada, "Nivel": 1 }
    }

    return save_manager.guardar_partida(data)
