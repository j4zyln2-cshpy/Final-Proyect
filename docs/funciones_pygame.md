# Documentación rescatable de Pygame:

Hola, que tal, soy j4zyln2, un estudiante de ingieniería de sistemas, que apenas está empezando en desarrollar videojuegos pequeños en GDevelop y GameMaker, además de proyectos individuales utilizando paquetes de C++ como allegro y librerías como SFML, amante de los videojuegos, pixelart, y me gusta la tecnología, no soy un amante, pero si me gusta comentar cualquier cosa

Mi canal en youtube es: gz. Actualmente está vacio, pero dentro de poco subiré videos hablando de tecnología, videojuegos, etc :3

A por cierto, toy en plena pa NO NO

1) Manejo de Pantalla y Ventana: 

Entiendo qye Pygame dibuja todo sobre objeto, pero ¿Cómo se llaman? surface, que son imagenes en memoria, todo lo que vemos es una superficie (surface lol), la ventana principal es la superficie principal a dibujar y sobre la cual se va a dibujar, porno

Algunas funciones a incluir son:

* *pygame.init()*: inicializa todos los módulos internos. SIEMPRE DEBE IR AL INICIO
* *pygame.display.set_mode((ancho,alto))*: Crea la ventana del juego y devuelve la superficie a renderizar
* *pygame.display_set_caption("NOmbre)*: Cambia el titulo de la ventana
* *pygame.display.update()*: Actualiza el contenido de la pantalla, muestra todo lo dibujado en el frame actual xd

¿Cómo se ve en código?

import pygame

pygame.init()
variable_pantalla_lol = pygame.display.setmode((200,400))
pygame.display.set_caption("Título de mierda")

2) Game Loop y Control de Tiempo:

Llegamos a pygame.time, que, a diferencia de motores como GameMaker, GDevelop, que, por ejemplo son las que yo utilizo y de hecho gestionan el ciclo ellas mismas, aquí controlamos nosotros mismos el bucle principal de forma manual, es decir, te toca manejar todo el ciclo de juego TÚ SOLO (o tu equipo). Para evitar que el juego corra a velocidades infinitas, podemos usar y mencionar:

**pygame.time.Clock**

* *clock = pygame.time.Clock*: En este amiguito creamos el objeto reloj
* *dt = clock.tick(60) / 1000.0*: este limita el juego a 60fps (frame per second), devolviendo el tiempo transcurrio desde el último frame en segundos, en otro caso, si hicieras (dt = clock.tick(50)/1000.0), lo limitaría a 50fps, pero aquí lo haré a 60

**¿Por qué deberías de usar dt?**: En mi caso, como solamente voy a usar un eje, solamente tendría que multiplicarlo por la velocidad para enemigos (como duendes), sin importar los FPS (tendría que comprobar después)

**¿Qúe es un frame?**: En palabras sencillas, es cada instante o imagen que procesa la consola o PC en un segundo. Es cada una de las imágenes fijas que forman un vídeo o juego en pantalla. A 60 fotogramas por segundo, un solo frame dura cerca de 16 ms.

-- Extra: ¿Qué es un frame perfect?: Es una acción en un videojuego (como por ejemplo Super Mario Bros de 1985) que exige pulsar un botón o hacer un movimiento exactamente en un fotograma (frame) específico, siendo abusadisimo en speedruns, al igual que el pixel perfect

¿Cómo se ve en código?:

reloj = pygame.time.clock() #creamos el objeto real
executing = True #y creamos una variable executing que tomará un valor booleano

while executing:
dt = reloj.tick(60) / 1000.0 delta time en #segundos

3) Eventos e Inputs:

Volví a eventos, bueno, para hacertelo en formato pene, pygame solo necesita que TÚ hagas un clic, presionas una tecla, o hagas una acción, todo eso lo guarda como en una cola de eventos (event queue)

*¿Qué es una cola de eventos?*: Una cola de eventos es una lista ordenada de EVENTOS, tareas o mensajes que esperan su turno para ser procesados
*¿qué es un event queue?*: Una event queue es una fila ordenada donde se guardan tareas o acciones (como un clic, una tecla presionada o datos que llegan de internet) para que el programa las atienda una por una, en estricto orden de llegada, sin que nada se pierda ni se atasque.

* *pygame.event.get()*: Vacía la cola y devuelve una lista de los eventos ocurridos desde el último frame.
* *event.type == pygame.QUIT*: Se dispara cuando el jugador presiona la "X" de la ventana.
* *event.type == pygame.KEYDOWN*: Se dispara únicamente en el frame en que se presiona una tecla.
* *pygame.mouse,get_pos() / pygame.mouse,get_pressed()*: Esto devuelve una tupla de tres valores booleanos (clic_izquierdo, clic_medio, clic_derecho) que indican si cada botón está presionado o no (true/false) en el momento exacto de la "llamada".

¿Cómo se ve en código?

ejecutando = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        ejecutando = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            print("bienvenido a la torre tipo 1 :3")

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # este es el clic izquierdo
            pos_x, pos_y = pygame.mouse.get_pos()

4) Sprites, Imágenes y Superficies

Para por ejemplo, mostrar mis duendes, o las bombas de mi Bomberman, o un castillo, cargo imagenes desde mi disco, se dibuja, etc

* *pygame.image.load("ruta/imagen.png").convert_alpha()*: Carga una imagen. con convert_alpha() mantienes una transferencia PNG

* *pygame.transform.scale(superficie, (ancho, alto))*: Escala una imagen al tamaño deseado.

* *superficie_destino.blit(superficie_origen, (x, y))*: "Pega" una imagen/superficie sobre otra en las coordenadas (X, Y)

¿Cómo se ve en código?

sprite_bomba = pygame.image.load("assets/bomba.png").convert_alpha()
sprite_bomba = pygame.transform.scale(sprite_bomba, (32, 32))

pantalla.blit(sprite_bomba, (pos_x_bomba, pos_y_bomba))

5) Colisiones y Formas Básicas

Incluso si mi lógica ssolo es de 1D, pygame lo gestiona gracias al objeto pygame.Rect

* *rect* = pygame.Rect(x, y, ancho, alto): Crea una caja delimitadora.

* *rect1.colliderect(rect2)*: Devuelve True si dos rectángulos se superponen (por ejemplo, si el proyectil impacta al duende).

* *rect.collidepoint((x, y))*: Revisa si un punto (como el clic del mouse) está dentro del rectángulo (útil para seleccionar casillas de torres).

¿Cómo se ve en código?

rect_bomba = pygame.Rect(bomba_x, 300, 32, 32)
rect_duende = pygame.Rect(duende_x, 300, 40, 50)

if rect_bomba.colliderect(rect_duende):
    print("¡QUIERO PE... DIGO, LANZAMIENTO DE BOMBA *se muere*!")

6) Texto y UI Básica: 

Para mostrar el dinero acumulado, puntos, vida, oleadas, o lo necesario, porfin usaremos pygame.font

* *font = pygame.font.SysFont("Arial", 24)*: Define la tipografía o las fuentes
* *txt_surface = font.render(f"Oro:{gold}", True, (255,255,255))*: Genera una superficie con el texto dibujado
* *window.blit(txt_surface,(x,y))*: Pega ese texto en la pantalla

7) Control de Sonido y Música:
* *pygame.mixer.init()*: esto inicia el sistema de audio de pygame
* *pygame.mixer.sound.set:volumen(n)*: Reproduce la música, peroooo, ajsta el volumen a n, por ejemplo, supongamoos que fuese 0.5, ajusta el volumen a 50% 
* *pygame.mixer.sound.load("musiquitagud.wav/mp3)*: carga un sonido en especifico
* *pygame.mixer.music.play(-1)*: Reproduce la música de fondo en un loop infinito DKLFKKFJFKJFKFJKFKFJFKJFKFJKFJKFJKFJFKJFKJFKFJKFJKFJFKJFK

8) Transformación de Gráficos:
* *pygame.transform.flip(superficie, flip_x, flip_y)*: Invierte la imagen de forma horizontal o vertical
* *pygame.transform.rotate(surface,angle)*: Rota la imagen a los grados que pusiste ahí

9) Entrada, eventos:

* *pygame.key.get_pressed()*: Devuelve una lista con el estado de TODAS las teclas
* *pygame.KEYDOWN*:  es un tipo de evento que se activa exactamente en el momento en que el usuario presiona una tecla hacia abajo en el teclado.
* *pygame.mouse.get_visible()*: Oculta el puntero para dibujar una mira o un cursor en pixel-art xd

-- posteriormente añadiré para hacer colisiones, más funciones de añadir eventos, etc :D

# ¿Cómo instalarlo?

Ejecuta los siguientes comandos en orden: Ctrl + J -> Terminal -> pip install pygame 

puedes ver si se instaló con: pip list

# ¿Para qué sirve?

Pygame es una biblioteca de Python, la cual es principalmente para crear videojuegos en dos dimensiones (2D), además de programas multimedia interactivos. Es perfecto para manejar gráficos (OSTIA QUE BUENOS LOS GRÁFICOS, QUE BUENOOOOOOS, QUE BUENOS SON LOS GRÁFICOS, SIII, SII 🗣️❗), reproducir soniditos y músiquita, controlar la entrada de teclas y ratón, y gestionar la animación

- Permite desarrollar jueguitos de plataformas, puzzles, arcades, o estrategia

- Facilita el cargar y mostrar imágenes, sprites, fondos y la reproducción de música o efectos de sonido.

- Captura acciones como clics, pulsar teclas, mover el ratón, etc.

- Es útil para probar ideas de juegos, como lo es esta, pa pasarlo a otros motores, de hecho, alguien en YT lo hizo (busquenlo xd)

# ¿Por qué usarlo?

-- Según mucha gente, es fácil de aprender, y la verdad si, relativamente lo es, su sintaxis es simple para gente pendeja como yo que empezó en el mundo del videogame development o la programación en general

-- Todo obviamente basado en python, aprovecha todo de este lenguaje sin requerir uno extra, como C++, C, Assembly, etc

-- Cuenta con documentación, tutotiales, proyectos de apoyo (de hecho de este me base en uno disponible de internet, solo que obviamente haciendolo a mi forma), etc

-- Me hizo mejorar en Gdevelop o GameMaker, e incluso Unity, ya que me ayudó a entender bucles de juego, conceptos lógicos, interacción de componentes de software, etc

-- Es sencillo de manejar y arroja resultados verdaderamamente buenos, proceso básico, resultado efectivo, 100% de efectividad.

# ¿Cómo fue mi experiencia con esta librería?

La verdad, un poco rara, no diré traumatica, ni nada de ese estilo, a y por cierto, os dejo una imagen final :3

![alt text](animations.gif)

-- oa: J4ZYLN2 

me acabo de dar cuenta que no subí nada, pero llevo desde el 2-3 de agosto con el repositorio vacío, hoy 5 o mañana 6 de agosto subo aunque sea algo nwbn, pq ese repositorio hace ya 2 días que lo debería de tener actualizado, no me jodas njkdjkdjdkjdkjdkjdkjdkjdkjdkjdkdjkdkdj (odio mi vida)