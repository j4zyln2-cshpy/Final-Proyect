*WARNING: No sabía que titulo ponerle, así que le puse un título relacionado a mi nombre de usuario. en este documento tendré todo lo que lleve hasta ahorita, actualizaciones por día, cambios sencillos, como hice mis pruebas, como creé mis clases, y mis decisiones actuales, está incompleto y mañana será actualizado*

-- Fecha: 12 de agosto de 2026

# Kingdom Defense / Last Standing Defense: Proyecto hecho para Coderhub Academy lol

Kingdom Defense es un videojuego sencillo de estrategia y defensa de torres (o Tower Defense) ambientado en un eje unidimensional, pero al inicio con dibujos feos y música sacada de internet, posteriormente se harán cambios posteriores. El jugador tendrá que ser lo suficientemente inteligente para aguantar la mayor cantidad de tiempo posible sin morir. Como esta es una función MUUUUUUUUY primeriza y sin intención de hacer un proyecto muy completo, lo más probable es que la única animación que hagan los personajes sea movimientos MUUUUUUUY lentos de izquierda a derecha o viceversa.

## Personajes y entes principales:

* *Defensores*: Espadachin, Caballero, Ogro, Soldado
* *Enemigos*: Ogro, Duende, Monstruo, Verdugo
* *Torres*: Torre_Rey, Torre_Mágica, Torre_Base
* *Armas y Defensas*: Flechas, Bombas, Fundíbulo, Muralla, Foso,


## Justificación del Proyecto:

Motivos: ninguno, simplemente lo quise crear JAJAJA, aunque obviamente estará más cutre que cagar con diarrea, simplemente tuve la necesidad de crear una arquitectura efectiva para un juego que simule la Defensa de una Torre, o hacer un videojuego interactivo en 2D/1D usando Pygame como herramienta y libería principal

A través de esta propuesta, tengo 3 mini objetivos sencillos y de aplicación practica en el desarrollo:

1. **State Pattern**: Gestionar la transición entre menú, juego activo, pausas y GAME OVER (PERDISTE XD)
2. **Persistencia de Datos**: CON SQLITE debo garantizar un almacenamiento estructurado, seguro y efectivo, mi soporte fueron las 4 tablas mencionadas XD, la ruta es `database/LSD.DB`
3. **Gestión de Recursos**: Cargar, Instanciar y Manejar Dibujos y Audios, mis mejores panas en este caso son SpriteManager (ruta: `src/core/sprite_manager`) y SoundManager (ruta: `src/core/sound_manager`)

pd: usted mismo puede determinar el hecho de si fueron cumplidos o no, salvo el segundo, que fue un exito JAJAJA
pd2: QUE NO SON SPRITES

## ¿Por qué Pygame?

**Simplicidad**: Es ligero, literalmente el proyecto completo lo podrías tener con los requerimientos y ni cuenta te darías, no dependes de otras dependencias
**Es perfecto para juegos uni o bidiomensionales**: Incluso ofrece soporte y documentación para manipular superficies, renderizado, reproducción de audio y dibujos, control de tiempo y loop de juego, etc
**Control Total**: Me permite gestionar el tiempo delta, cola de eventos, estados, a pesar de que en otros motores ya venga automatizado
**Experiencia previa (y porque era la única solución viable)**: He desarrollado algunos juegos en pygame, relativamente pequeños, como este proyecto, a pesar de las 9309309309390390390390390904940940 carpetas con 5-6 archivos como mucho JAJA (como por ejemplo: un juego RPG)
**Nó me quedó de otra**: Era esto o volver a usar Flask ya teniendo como 3 proyectos con el fockin madito pero hijepta flask joe

## Requisitos e Instalación

* Lenguaje: Python (3.10 o superior, aunque recomiendo 3.13)
* Librería principal: Pygame 2.5.0, 
* Persistencia: Módulo json y archivo db

-- Opción 1: pip install -r requirements.txt
-- Opción 2: pip install pygame 


## Instrucciones de Ejecución

1. Clonas o descargas el repositorio: copias el link con git clone y lo guardas en una carpeta o "destinatario de repositorio"

2. (opcional el env, obligatorio el resto) crear un entorno virtual e instalar las dependencias:

python -m venv lsd
lsd\Scripts\activate
pip install -r requirements.txt 

eso o descargas directo pygame

3. Ejecutas el juego desde el punto de entrada: python main.py


## Ejecución del archivo principal

python main.py


## Algunas Decisiones Tomadas:

1) Patrón State: Todos heredan a través de la clave o estado base (BaseState). Por ejemplo, la clase GameState alterna un poco entre alguna que otra de las clases o estados restantes, para asi poder tener mejor en mira la lógica de interfaces, bucles, etc

2) Managers:

  * *SpriteManager*: Carga, almacena y escala las imágenes PNG para evitar lecturas e imagenes repetitivas

  * *SoundManager*: Administra la reproducción de música en bucle y efectos de sonido (SFX)

  * *SaveManager*: Maneja la serialización y lectura del estado en database/savegame.json de manera no bloqueante

3) Colisiones 1D: Como trabajé con un único eje, para evitar que sea a montones, logré descubrir que el rango de ataque omite cajas de colisión 2D que pygame tiene pero no están implementadas, al igual que motores como por ejemplo Godot, calculandose solamente la distancia entre coordenadas X. la fórmula es sencilla:

| Xunidad - X objetivo | <= Rango

4) "Cambio" definitivo para la Persistencia de datos: Al inicio lo más lógico sería guardar todo en un archivo savegame.json, y de hecho, esa fue mi idea de prueba. Pero, LSD.db era siempre el archivo donde se iban a sobreescribir, guardar y cargar los datos, hecha en SQLITE. Y la verdad, es muchiísimo mejor, ya que puede guardar estadísticas de diferentes usuarios, y se pueden hacer diferentes tipos de consultas para obtener datos en específico, si, debería de cambiar posteriormente a otra aplicación de database, pero al ser un proyecto relativamente de aprendizaje, usé esta (y es perfecto para esta clase de proyectos)

5) Separar el Bucle Principal de la Interfaz: ¿Por qué no hice una interfaz en el main.py?. Decidí mantener las pantallas principales (como Menú, Juego, Game Over) fuera del archivo principal, la primera vez que lo intenté estructurar así con otro proyecto (que fue un Ping Pong sencillo) fue un completo fiasco, además de que se ve feo, genera código que ni Dios entiende y es más díficil de depurar en Python, si va lento, el hecho de que te tenga que cargar Interfaces, Menu, Game Over, Pausa, el juego en sí, tus funciones para animaciones principales, etc etc, es horrible, tarda un buen rato ya que Python no es precisamente un lenguaje rápido nisiquiera con archivos que tengan más de 5 lineas de código. Bueno, el punto es que los decidí separar para poder implementarlos dentro de main.py sin tener que crearlos desde el mismo archivo, sino que al ser diferentes estados/partes/animaciones/flujos les decidí dar su espacio, y así sea más fácil de manejar eso que un archivo con 5000 líneas de código para un juego que a un videogame developer le costaría 5 horas.


## Historial de Desarrollo y Registro

-2 de Agosto:

  *Creación de estructura del proyecto, Configuración del repositorio Git y creación de ALGUNAS variables de configuración global en config.py*

-3 de Agosto:

  *Primer Test, inicialización de Pygame, creación de ventana principal, entradas básicas*

-4 de Agosto:

  *Test 2, simulación del movimiento en el eje x*

-5 de Agosto:

  *Test 3, Implementación sencilla de estados, direcotres y manejo de carga de imágenes PNG y audios MP3 y WAV*

-6 de Agosto:

  *Mini Ensamblado y unificación rápida. mini culminación de prueba 3*

-7 de Agosto:

  *Culminación de Test 3 yTest 4, integración del módulo SaveManager para escribir y leer estados de partida*

-8 de Agosto:

  *Test 5, Validación en consola de la regla de detención por rango de ataque y cooldown*

-9 de Agosto:

  *Test 6, Renderizado de entidades y comprobación de colisiones*

-10 de Agosto:

  *Test 7, integtación definitiva de Sprites, Mapa y Guardado Silencioso, implementación de cambios para guardar partida, eliminando superficie en save_game*

-11 de Agosto:

  *Test 8, creación de este archivo, correcciones y preparaciones para la implementación de la Interfaz UI y el sistema económico del juego*

- 12 de Agosto:
  
  *Cambio de ruta para el archivo de guardado, añadidura de funciones para la clase Game en main.py, finalización de documentación*

- 15 de Agosto:

  *entrega definitiva del proyecto*


## Estructura del Archivo de Guardado de prueba:

Archivo 1: {
    "duende_x": 117.09999999999992, #posición en el eje x del duende
    "duende_speed": 100.0, #el atributo de velocidad del duende
    "torre_x": 700.0, # la posición en el eje x de la torre
    "torre_hp": 100.0, # la vida/hp de la torre
    "oro": 0, #el oro acumulado
    "puntuacion": 0 #los puntos del jugador
}

Archivo 2: {
    "jugador": { #datos del jugador
        "gold": 100, #oro acumulado
        "points": 20 #puntos del jugador
    },
    "torre_rey": { #datos de la torre_rey
        "hp": 100, #vida de la torre_rey
        "x_position": 600 #posicion x de la torre
    },
    "partida": { #datos de la partida
        "oleada_actual": 1, #oleada de enemigos actual
        "Nivel": 1 #nivel actual donde el jugador dejó la partida (único de momento)
    }
}

Archivo DB: 
 id: N
 jugador: Player1
 oleada: 1
 puntos: 0
 datetime: KKDLKDLKDL


# Documentación general de todo lo llevado hasta la actualidad:


## 1. Arquitectura de Clases (¿Cómo mierda construi esto sin que colapsara?)

En lugar de lanzar 2,000 líneas de código en un solo archivo main.py y rezarle a diosito, me recomendaron mejor una Arquitectura Limpia y Programación Orientada a Objetos (POO), así que dividí el "reino" en clases especializadas donde cada una sabe exactamente qué hacer, teniendo ss funciones especificadas y claras para poder entender QUE DEBE DE CUMPLIR

### A. El Motor Principal 

* **Game (main.py)**: Es el cerebro supremo. Hereda la responsabilidad de inicializar Pygame, crear la ventana, instanciar todos los *Managers* (SpriteManager, SoundManager, SaveManager) y gestionar la máquina de estados. Posee el bucle principal (run()) que calcula el dt (Delta Time) para que el juego corra fluido tanto en una PC gamer como en una tostadora con pantalla, tipo DOOM xxd
* **BaseState (src/states/base_state.py)**: La clase madre abstracta. Todos los estados heredan de ella (por eso actualize pausestate jajajajsjaj, odio mi vida). Garantiza que cualquier pantalla del juego implemente obligatoriamente la "Santa Trinidad" de funciones:
  * handle_events(events): Procesa las teclas y clics.
  * update(dt): Modifica la lógica, posiciones y variables.
  * draw(screen): Pinta las imágenes en pantalla.
* **Estados Concretos (MenuState, GameState, PauseState, GameOverState)**: Cada uno es un mundo aislado. Al cambiar de estado con game.change_state("GAME"), el motor pausa el renderizado del menú y pasa a controlar la lógica de combate de la partida sin dejar basurita en memoria.

### B. Los Administradores Logísticos (Managers)

* *SpriteManager (src/core/sprite_manager.py)**: Nuestro repartidor de sprites de confianza. Para no reventar el disco duro leyendo archivos PNG 60 veces por segundo, esta clase implementa un caché (*Dictionary*). La primera vez que le pides duende.png, lo lee del disco, lo guarda en RAM y te lo entrega. Las siguientes 10,000 veces, te devuelve la copia almacenada en milisegundos y lo carga en la superficie
* **SoundManager (src/core/sound_manager.py)**: Separa las pistas MP3 de la música de fondo en bucle de los efectos de sonido WAV (sables, explosiones, clics de botones). Incluye gestión de volumen y manejo de excepciones por si a Pygame le da un ataque de pánico con los drivers de audio.
* **SaveManager (src/core/save_manager.py)**: Encargado de la serialización y deserialización en formato JSON. Se encarga de convertir objetos de Python a texto ejecutable en database/savegame.json de forma silenciosa, usando bloques try/excep` para que si falla la lectura del disco, el juego no sufra un crasheo instantáneo, sino que pueda escribir y guardar en json y en db.

### C. La Interfaz Dinámica (src/ui/interfaz.py)

* La interfaz del juego, en este punto, tenemos dos funciones principales (menu_compra y menu_juego), en estas funciones, cada uno dibuja su menu y las opciones para el jugador.

* *Menu_Juego*: Menu de juego para el usuario para poder ingresar a su partida
* *Menu_Compra*: Menu de compra para poder mejorar las torres, se necesita guardar el archivo previamente

## 2. Diario de Pruebas (Test 1 al Test 8)

Para no morir en el intento, aplicamos la técnica ancestral de "Divide y Vencerás". No se escribió una sola línea del juego final hasta que cada mecanismo fue probado en un laboratorio aislado (*script de test*).

* **Test 1 - prueba inicial de pygame(test1.py)**:
  * *Objetivo:* Lograr que Pygame abra una ventana negra sin que la terminal mediga "Esta aplicación no responde".
  * *Resultado:* Éxito rotundo. Se validó la captura del evento QUIT (la tachita de cerrar) y la tecla ESC.
* **Test 2 - enemigos en Consola 1D (test2.py)**:
  * *Objetivo:* Implementación rápida de enemigos
  * *Resultado:*  Valió la pena
* **Test 3 - Carga de Texturas y Ruidos (test3.py)**:
  * *Objetivo:* Probar que SpriteManager y SoundManager no rompieran las rutas de archivos (assets/images/ y assets/sounds/).
  * *Resultado:* Primera vez que vimos un sprite renderizado y escuchamos un .wav sin que saltara el famoso FileNotFoundError.
* **Test 4 - Prueba de Estados (test4.py)**:
  * *Objetivo:* Probar la máquina de estados alternando de Menú a Partida con una tecla.
  * *Resultado:* Un éxito. La arquitectura POO funcionó como reloj suizo: los estados cambiaban limpiamente sin congelar la pantalla.
* **Test 5 -  Colisiones 1D (test5.py)**:
  * *Objetivo:* Validar la fórmula de distancia absoluta
  * *Resultado:* El duende detuvo su marcha al llegar a la coordenada exacta de la torre y empezó a aplicar daño por temporizador (*cooldown* de ataque).
* **Test 6 - Colisiones a Color (test6.py)**:
  * *Objetivo:* Pasar la lógica del Test 5 a la pantalla de Pygame con cuadraditos de colores y barras de vida verdes/rojas.
  * *Resultado:* Visualmente hermoso. Los bloques cambiaban a color rojo al entrar en combate y la barra de vida se reducía en tiempo real.
* **Test 7 - La Gran Fusión (Mapa + Sprites + Save JSON) (test7.py)**:
  * *Objetivo:* Juntar el fondo del mapa, los sprites reales del duende y la torre, la colisión 1D y el guardado silencioso al presionar la tecla S.
  * *Resultado:* El prototipo cobró vida. Presionar `S escribía el archivo savegame.json sin un solo micro-estallido de lag, aunque nunca me lo guardaba por culpa de una superficie de mierda
* **Test 8 - Economía, UI e Interfaz Interactiva (test8.py)**:
  * *Objetivo:* Probar las funciones de interfaz.py inyectando el diccionario del jugador, descontando oro al presionar las teclas 1, 2 o 3 y bloqueando las compras si no hay dinero suficiente.
  * *Resultado:* Sistema de tienda funcional. El menú interactivo y la barra superior respondieron de inmediato con la simulación completa de eventos.
* **Test 9 -  Gestionar Oleadas y Game Over definitivo**:
  * *Objetivo*: Probar la gestión de oleadas, implementar y llevar los avances del juego a una mini prueba, gestionar el gameoverstate y los diferentes estados
  * *Resultado*: Problemas al principio con la gestión de oledas, resueltos debido a una estúpidez que olvidé borrar JAJAJ
* **Test 10 -  Integración Final**:
  * *Objetivo*; IMPLEMENTACIÓN COMPLETA, NO IMPORTA QUE HAYA O NO, COMPLETA
  * *Resultado*: GANAMOS SSOKSPOSPSPOSPSOPSOPSOSPOSP o(≧∀≦)o


# Arquitectura Completa del Proyecto:

- assets /
         -- sounds/ # *carpeta de sonidos a utilizar*
         -- images/ # *carpeta de imagenes a utilizar*

- database / # *carpeta principal de manejo de base de datos*

- src /
      -- core / # *carpeta para manejar sonidos y sprites*
      -- entities/ # *carpeta de entidades*
      -- scenes/ # *escenas de juego y mapa*
      -- ui/ *interfaz del juego*

- tests /
        captures/ # *capturas de lo llevado a lo actual en el juego*
        pygame/ # *capturas, código, animaciones de un mini juego*

- docs / *documentación base de lo que llevo hasta hoy*

- states / *estados base del juego*

- main.py *archivo principal de juego*

- requirements.txt *requerimientos necesarios*

- .gitignore *archivo que le indica a git lo que ignorará*

- README.md *archivo de lectura principal*

- ACTUALIZACIONES.md *archivo principal de documentación y actualizaciones*

- j4yz.md *archivo de documentación personal*

- savegame.json *archivo principal de prueba de guardado*

**SUBCARPETAS** 

* *sounds* 
  - Gameover
  - Pausa
  - Click
  - Confirmar Click
  - Sonido de la transcurrencia del juego
  - Llegada de oleada
  - Jefe
  - Menu
  - Caida de Torre
* *images*
  - Defensores
  - Torres
  - Menú y Mapa
  - Enemigos
  - Armas

* *core*
  - Directores: SpriteManager y SoundManager
  - Rutas: config.py
* *entities*
  - Enemigo
  - Defensor
  - Torre
  - Proyectil
  - Hechizo
* *scenes*
  - Mapa (la misma durante todo el juego)
  - Escenas del juego (a ún futuro será mejor aprovechado)
* *ui*
  - Interfaz del juego

* *captures*
  capturas almacenadas durante la fase beta y las pruebas
* *pygame*
    *captures_2*
      capturas almacenadas del segundo juego
    *font*
      fondo de texto xd
    *graphics*
      sprites a usar
    *audio*
      musica de prueba

# Archivos y carpetas principales:

-- main.py
-- states/
-- src/ core 
-- src/ ui
-- src / entities
-- database/
-- assets/ images
-- assets/sounds
-- docs/
-- savegame.json
-- README.md

# ¿Qué problema resuelve este proyecto?:

-- Un "cliente" (no existe por cierto) pide una aplicación o un software utilizando pygame de entretenimiento (en este caso un videojuego) con géstion de datos, persistencia, y uso de habilidades aprendidas durante el curso de Coderhub Academy


# Datos del Proyecto

-- Flujo MVP: 

 *Flujo N1. Interfaz y Menú "DECENTE"*: El punto aquí es crear un menu principal de juego interactivo (no al nivel de PvZ pero al menos que el usuario entienda), con audio en bucle, navegación con "sonidos de efecto" dignos de Video Brinquedo y estados de pausas y game over para que se sienta como un juego y no como si fueras un ojeador virtual de cosas sin sentido xd 
 *Flujo N2. Combate y Oleadas*: El más arrecho arrechito , es un bucle de combate y oleadas de enemigos. además de una gestión de vida / combate necesarios para lo que verdaderamente ES EL PUNTO LÓGICO del juego
 *Flujo N3. Persistencia:* Es solo guardado y lectura de datos (como oro, puntuación, vida de la torre), de prueba previa en formato JSON, para ser en formato DB

-- Desarrollador: J4zyln2

-- Fecha de Entrega: Sabado 15 de agosto de 2026

-- Grupo/Institución/Academia: Coderhub Academy

-- Coderhub Curso Básico 003 :3


# Proyectos personales con pygame:

1) Juego de la culebrita (Snake)

2) Ping - Pong

3) Plataformero sencillo, aunque con 100 indicaciones :v

4) Tetris

5) Este proyecto JAJA

