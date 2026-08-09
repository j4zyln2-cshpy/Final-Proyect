# Proyecto final Coderhub: Presentado por José Petit / J4zyln2-chspy

* Title: Last Standing Defense / Kingdom Defense 1D*

* Usuario Objetivo: Al inicio será para jugadores casuales, o gente que le guste esta clase de juegos, con el paso de las actualizaciones intentaré implementar nuevas estrategias para atraer jugadores diarios, con sistemas de niveles mejorados, nuevas mejoras, etc

* Funciones Principales (M.V.P):

-- *Flujo N1. Interfaz y Menú "DECENTE"*: El punto aquí es crear un menu principal de juego interactivo (no al nivel de PvZ pero al menos que el usuario entienda), con audio en bucle, navegación con "sonidos de efecto" dignos de Video Brinquedo y estados de pausas y game over para que se sienta como un juego y no como si fueras un ojeador virtual de cosas sin sentido xd 
-- *Flujo N2. Combate y Oleadas*: El más arrecho arrechito , es un bucle de combate y oleadas de enemigos. además de una gestión de vida / combate necesarios para lo que verdaderamente ES EL PUNTO LÓGICO del juego
-- *Flujo N3. Persistencia:* Es solo guardado y lectura de datos (como oro, puntuación, vida de la torre), de prueba previa en formato JSON, para ser en formato DB

* Tecnologías:

-- *Lenguaje*: Python (3.13)
-- *Librería*: Pygame
-- *Data y Persiencia de Datitos*: JSON / SQLITE
-- *Repositorio de mier... DIGO, CONTROL*: GH (github para los conocedores) y Git 

pd: si tienes un desorden de carpetas, identifica en que repositorio estás para no confundirte en caso de tener un orden que ni tu entiendes, con git remote -v 

* Instalaciones:

1) Clona mi repositorio "público": podrías hacerlo directo desde git clone o desde el comando

-- *Git Clone*: Está disponible apenas abres visual studio code: copias el repo, guardas la carpeta y empiezas a editar

-- *Comando*: bash: git clone [link (https...j4zyln2//git...j4zyln2/)] cd [nombrecarpeta (n)]

Recomendación: Utiliza git clone xd

2) Instala las dependencias necesarias

pip install requirements.txt

3) (En caso de no querer instalar lo necesario en requirements.txt), más por flojera:

-- *pip install pygame*

Recomendación personal: busca documentación de pygame lol xdddddd

# Crear y activar un etorno virtual:

python -m venv insertnombredenetornovirtual.mp4

-- en windows: name\Scripts\activate (pd: yo no tengo, está de extra, lo activé pensando que lo iba a usar XD)

# Instalar las depedencias que necesitas o la librería:

ya lo mencioné, pero ejecuta este comando: pip install -r requirements. txt

# Uso:

El punto de este apartado es para que puedas ejecutar el juego más incompleto posible con la máquina de estadoa principal

python main.py

-- Puedes usar estos controles de prueba cuando lo ejecutas, quizás los cambie:

ESC: Salir del juego (le cambiaré el control)

p : Pausar el juego (aún no impelementado)

SPACE: Ejecutar efectos de sonido (SFX)

S: Guardar estado actual de la partida

# Estructura xd

nodiretitulo /
- assets /
         -- sounds/ # *carpeta de sonidos a utilizar*
         -- images/ # *carpeta de imagenes a utilizar*

- database /

- src /
      -- core /
      -- entities/
      -- scenes/

- tests /
        captures/
        pygame/

- docs /

- states /

- main.py

- requirements.txt

- .gitignore

- README.md

# Entidades / Clases Principales:

-- Entidades Principales:

1) Defensor:
   1.1) Hechicero
   1.2) Espadachin
   1.3) Arquero/Soldado
   1.4) Caballero
2) Torre:
   2.1) Torre Rey
   2.2) Torre Mágica
   2.3) Torre Base
3) Enemigo:
   3.1) Duende
   3.2) Ogros
   3.3) Verdugo
   3.4) Jefe/Monstruo (Ogro principalmente)
4) Proyectiles y Armas:
   4.1) Flecha
   4.2) Bombas
   4.3) Foso
   4.4) Mundíbulo
5) Monedas de Oro

-- Estados:

1) SaveState
2) BaseState
3) GameOverState
4) GameState
5) PauseState
6) MenuState

-- Relaciones de Interacción (lo implementado actualmente):

1) Herencia: MenuState, GameState, PauState y GameOverState heredan de la clase padre BaseState, la cual está "vacía"

2) Interacción sencilla: La clase GameState procesa la colisión, al ser un eje, ejecutas una fórmula tan sencilla como si estuvieras en bachillerato viendo química orgánica: Xenemigo - Xdefensor, calculando solamente la distancia entre enemigos y las estructuras y defensores de nuestra Torre Madre o Padre (una torre tiene género?)

# Pruebas Realizadas:

-- Test 1: Realizado (02/08/2026)
*Descripción:* Implementación de eventos para poder saber que teclas usar, prueba relativamente corta

-- Test 2: Realizado (03/08/2026)
*Descripción:* Implementación de entidades como Enemigo y TorreRey

-- Test 3: Realizado (05/08/2026)
*Descripción:* Prueba básica de clases como SpriteManager y SoundManager

-- Test 4: Realizado (07/08/2026)
*Descripción:* Impelementación final de Sprites y música como prueba, usando SpriteManager y SoundManager

-- Test 5: Realizado (08/08/2026)
*Descripción:* Detección de Colisiones entre Enemigos, 

-- Test 6: Realizado (09/08/2026)
*Descripción:* Prueba de Interacciones entre Enemigos, Torre y Defensores

-- Test 7: Pendiente ()
*Descripción:* Integración completa de Sprites de Mapa 2D / 1D

-- Test 8: Pendiente ()
*Descripción:* Implementación de Moneditas de Oro, Interfaz, Unidades

-- Test 9: Pendiente ()
*Descripción:* Gestionar Oleadas y Game Over definnitivo (aunque en main.py ya está)

-- Test 10: Pendiente ()
*Descripción:* Integración Final, Juego Completo en versión mini

# IA y Registro de Apoyo:

-- Diseñar estructura de carpeta y separar responsabilidades (Puede verse en el 1° prompt)
-- Planificar las etapas del proyecto bajo la metodología MSCW (3° prompt)
-- Documentación de errores y contenido necesario para poder tener estrategias claras del juego (2° prompt y 4° prompt)

# Mejoras Futuras:

-- Agregar verdaderos sprites y música producida por mí, no hechos en paint u obtenidos de khinsider
-- Agregar animaciones de múltiples frames (spritesheets) para animaciones de caminar, atacar, apariciones, etc
-- Incluir hechizos de area con temporizadores (cooldown)

# Autor:

-- Estudiante: J4zyln2 / José Petit
-- "RUTA": Software Developer - Nivel 1 (un momento, esto es una ruta? XD?)
-- Fecha: Agosto de 2026
-- Donde encontrarme: no lo hagas, solo buscame en Yt como Giuspy, de vez en cuando subiré videos xd

# Estado emocional actual:

git add bugs.py
git commit -m "more bugs lol"

![alt text](image.png) XDDDDDDDDD

# Constancia de Actualizaciones:

-- luego de la culminación del proyecto xd, esto no es para llevar los cambios actuales, para eso tendrás subido otro archivo markdown apenas se culmine este proyecto, más bien, es para llevar constancia de actualizaciones futuras posterior a su entrega (ya que es un trabajo, no un proyecto real)