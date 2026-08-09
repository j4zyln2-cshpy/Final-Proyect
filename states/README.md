# STATES

Este directorio implementa el patrón de diseño, me encatana llamarlo StateMachine, aunque solamente se llamará states actualmente xd, para gestionar las transiciones de pantalla del videojuego.

## Archivos: Estados, Módulos y Clases

* `base_state.py`: clase principal, tiene la interfaz obligatoria (handle_events, update,`draw) para todos los estados, pero estará vacío salvo que sea necesario opara el juego, cosa que no lo veo xd
* `menu_state.py`: la clase para la pantalla de inicio del juego, se encarga de gestionar la selección de opciones
* `game_state.py`: bucle de juego activo. contiene la simulación el spawn de enemigos,colisiones y actualización de la "batalla".
* `pause_state.py`: estado de pausa del juego, permite guardar la partida en JSON mediante *SaveManager* y reanudar el combate, pero eso será en las pruebas, en el juego "original", hará lo mismo pero en *LSD.db*
* `game_over_state.py`: pantalla de fin de juego, se activa cuando la vida de la Torre Rey llega a 0, permitiendo reiniciar o regresar al menú.
* `save_state.py`: estados para guardar la partida, permitirá al usuario reanudar el juego guardando lo último que el usuario vió para que vuelva a jugar desde el punto del cual "partió" *inserte gata bajo la lluvia audio miku.mp3*
* `save_manager.py`: director de sonido, debería de ir en src, pero me dió flojera XD