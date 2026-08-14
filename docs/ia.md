Hey, que tal :3, esto no lo quiero tener que subir al repositorio, pero es casi OBLIGATORIO cojones

Este es mi uso de IA (kimi k3) para poder principalmente identificar errores sin pedir código, determine usted mismo que mensaje puedo mejorar, ya que principalmente me tuve que documentar en pygame cómo por 8° vez

-- Función: Ruta y plan:
PROMPT 1: Actúa como mentor, profesor, o desarrollador de videojuegos indie

Condiciones obligatorias:
- 1: POO (aunque solo sería la creación de un Director de Sonidos y Sprites, los demás enemigos y entidades las tengo ideadas)
- 2: Dos relaciones entre clases (por ejemplo, Colisión: Enemigo - Defensor, o Enemigo - Torre)
- 3: Interfaz visual (Principalmente el fondo de pantalla en la ventana)
- 4: Validaciones y manejo de errores 
- 5: MVP con tres flujos principales 

Hazme preguntas de mi nivel actual (ya sea en desarrollo de videojuegos (que es realizar aplicaciones allegro en dev C++), o en programación), y posteriormente, lo ideal sería crear (sin hacer vibecoding o coding inexistente) estos siguientes pasos:

1) MSCW (MUST, SHOULD, COULD, WON'T)
2) Tareas pequeñas a resolver antes de empezar el proyecto 
3) Riesgos, planes de contingencia:
4) Actualizaciones diarias/semanales en estas 2 semanas ()

*pd: no uses nombres de desarrolladores indies de conocidos para que la IA se base, solo dale su rol y sus funciones y vuelvele a dar contexto en caso de una mala explicación previa, al final hablas con algo que no entiende tu proyecto hasta que lo indicas xd*

*pd 2: por la cara un MVP en un videojuego indie, nada que ver, si parece más un proyecto hecho en scratch XD*

-- Función: Encontrar razones para trabajar con eje unidimensional
PROMPT 2: ¿Qué ventajas trae con si crear un juego con una dimensión en pygame en comparación a juegos 2D hechos en motores como, supongamos, Unity, GDevelop, GameMaker, que si o si son juegos hechos en 2 o 3 dimensiones (x, y, z). Pero, a su vez, cuales son las desventajas que trae consigo el tener que "adaptarse" a este formato, debido a obviamente ser más feo visualmente, y mucho más complejo visualmente para un jugador promedio?

*pd: nunca trabaje con 3D, yo personalmente uso GameMaker o Gdevelop para hacer juegos relativamente pequeños ya que suelo hacer mucho uso del pixelart, y al no poder hacer diferentes tipos de spritesheets para cada personaje debido a las dimensiones, quise encontrar motivos del porque es mejor usar propuestas 1D*

-- Función: PLAN DE PRUEBAS MANUAL
PROMPT 3: Actúa como desarrollador/arquitecto de software/videojuegos. Mi proyecto es un juego de "Kingdom Defense" (básicamente, defender torres al puro estilo de Plantas vs Zombies) usando Pygame

Hazme primero las preguntas necesarias para comprender flujos y relaciones, recordando que al trabajar con diferentes entidades, cada una toma un rol diferente, como por ejemplo, duendes y ogros, que son los enemigos del castillo, en comparación de hechiceros y espadachines, que son los encargados de salvaguardar el castillo como si estuvieras defendiendo un voto judicial (al más estilo god of war). Ya poseo una estructura de pruebas y tests específicos: desde tests sencillos, pruebas de imagenes, enemigos, hasta pruebas de sonido, pero una ronda incluso muy sencilla de preguntas me ayudaría a complementar todo.

*pd: esto me fue efectivo para poder desarrollar diferentes pruebas, implementar cambios, etc, es muy probable que tenga que actualizar todo de forma diaria*

-- Función: Error "desconocido": AttributeError: partially initialized module 'pygame' has no attribute 'init' (most likely due to a circular import) -- aquí si admito que me pasé de flojo pq me lo encontré a los 15 minutos en reddit
PROMPT 4: Sé que para toda importación de pygame tengo que implementar pygame.init(), pero, ¿Solamente, de confirmación, si llamo a un mismo pygame.py, ejecuto un pygame.init() previo al resto de código, y me sale ese error, es por qué en caso de llamar pygame a un archivo e importar el mismo nombre, es porque en sí, no importa el módulo/librería, sino que intenta importar el archivp??

*pd: no, no es un error desconocido, verdaderamente tenía dudas de este error, fue de lo que no ví a documentarme xddddd (pd: eso aparece casi que entrando a pygame, me dió flojera ver XD) esto me saltó a la hora de hacer el primer test en main.py, que se llamaba realmente pygame.py. Osea sí, soy un tonto, pero con clase (╬▔皿▔)╯*


-- Función: Lógica de colisiones sencilla

PROMPT 5: "Actúa como un arquitecto de videojuegos indie. Explícame de una forma un poco más conceptual, más basado en como funciona una colisión, o en teoría, acerca de como funciona o funcionaría la detección de colisiones en un juego unidimensional entre un enemigo en movimiento y el jugador en velocidad 0, un cuerpo estático. ¿Qué variables lógicas se necesitan para que no se sobrepongan en un frame en específico del ciclo de juego y así no se vea tan sobresaturado de enemigos o entidades dentro del mapa?. Supongamos que existe Mario 1D, Goomba y Mario pueden participar en el mismo punto en el eje Y, pero, omo es el juego, al confirmarse que si hay más enemigos, ¿Cómo funcionaría para que no se vea sobresaturado un juego que tiene más de, por lo menos, 20 enemigos? Podrías incluso mostrarlo en código, pseudocódigo, o una estrategia útil que pueda entender hasta un niño"

*pd: esto me sirvió para otras pruebas, de todos modos tuve que buscar en YT como funcionaba*

-- Función: Solución de error

PROMPT 6: "Actúa como un arquitecto o desarrollador de software de videojuegos experimentado en Pygame, una librería de Python diseñada para videojuegos 2D. Bueno, el punto es que en Pygame tengo un error, al llamar al método save_game() dentro de GameState (en una de sus funciones de manejo de eventos), Python me devuelve un error indicando que falta un argumento que no tiene relación con la función, de tipo Surface o que esperaba una superficie. Yo tengo una carpeta de diferentes estados, cada uno tiene su función, pero normalmente solo necesita una superficie a dibujarse en un def draw, como por ejemplo, para un SaveState. En dado caso, necesito que me ayudes a revisar la lógica de estos dos métodos, y me expliques una solución factible, como si fuera a un niño, para identificar en qué parte del código el programa no se entiende con la función save_state, o incluso, en lugar de reservarla para draw(), que hace en específico*

*pd: El único de los 1000 errores de pygame al cual no logré encontrarle documentación, quería subir directamente los cambios, y ni ganas tenía de seguir buscando sin encontrar nada, en dado coso, use kimi k3 para que me pudiera explicar y corregir el error, el resultado fue un cambio en la función de save_game(). El principal problema es que añadí una superficie que no era, y, al borrarla, pensaba que en lugar de guardar el estado de la superficie, la iba a borrar, cuando estaba de extra*

-- Función: Preparación a cambios y mejoras futuras

PROMPT 7: "Actúa como un desarrollador de videojuegos, experimentado en Pygame, pero incluso en librerías como SFML, paquetes como Allegro, y experiencia de videojuegos en C, C++, etc :3¿Que cambios o mejoras podrían ser el anillo al dedo para un juego de Tower Defense (basado en juegos Flash de defender tu torre, o incluso PvZ) de 1D, con estados de menu, game_over, pausa, juego, guardado, con director de sprites y sonidos, para poder implementar y terminar de llevar este juego desde un cambio o proyecto pequeño a un proyecto más completo (además de obviamente "indicaciones" o "movimientos" para cada sprites, nuevos dibujos, spritesheets, animaciones y mejoras en el sistema de guardado, añadiendo más archivos de guardado) y así llevar este juego a algo más desarrollado. Puedes tomar referencias y plantearme un mapa simple de desarrollo de videojuegos?"

*pd: último prompt de forma definitiva, este prompt solamente fue para estructurarme un plan sencillo de cara a cambios futuros :3*


-- Función: Resolver fallos criticos de guardado en la base de datos SQlite por enviar estructuras SIN SOPORTE (dbbrowser, tu eres gei?)

PROMPT 8: "Durante la integración para guardar daos en main.py la consola arrojó un error de Error binding parameter: type 'dict' is not supported. Si, tengo entendido que esta función nes para cuando arrastro (entre 8003 comillas) un objeto en Python a SQLITE3, Pero ¿Cual es la causa raíz en el flujo de un juego como Pygame al guardar los datos, ya que yo tengo una tabla de estado_partida que recibe un inventario donde tengo 4 entidades (caballero, defensor, espadachin, soldado), cómo debo ajustarlo para que en la tabla pueda guardarlo? Es por el tipo de dato colocado, y si es ¿Que solución sería la más ideal para corregirlo?, porque en esa tabla guardaré lo que esté en el inventario"

*pd: Opté por remover la columa inventario de la tabla estado_partida, solamente delegué el almacenamiento de tropas compradas a la tabla de inventario_compras*

Prompts desde: 01/08/2026 - 13/08/2026 

# Prompts que yo recomendaría (Tomando de inspiración a D.M):

* *EXTRA: La idea 1 es el prompt base, el 2 y el 3 es para documentación y depuración*

*IDEA 1*: 

-- Actúa como desarrollador de videojuegos, profesor, o desarollador de software para un principiante. Quiero definir un proyecto (individual o en grupo, depende de como trabajes). Para una ruta sencilla, tengo un dominio relativamente corto pero útil en (implementas lo que manejas xd). Lo propuesto para un avance actual es (tu ideita), pero, antes de proponer una solución, puedes hacer una estrategia de evaluación y documentación claves para mantenerme al margen del conocimiento necesario. Podríamos definir las siguientes variables obligatorias para el proyecto:

(tus variables)

Con todo lo mencionado, el punto aquí no es escribir código, ya que, la idea central de un programador/ingeniero/estudiante es resolver problemas específico, sean básicos, intermedio o avanzado. Imaginate un contexto (puedes tomar una referencia necesaria para el proyecto, como guía), entregandome una ficha para documentación y de proyecto, definiciones de activos como el/los MVP y el flujo lógico, y uun formato MSCW (Must, Should, Could, Wont)

*IDEA 2*: 

-- Suponte que estás documentado totalmente en [tecnología], Investiguemos un problema relacionado con[tema/temasproyecto] en específico, ayudame a entender como surge este problema, cual es el punto de este problema y una solución. 

Context: [contexto]

Entre algunas referencias a tomar, distingamos puntos como:

1. Hechos similares
2. Recomendaciones
3. Tipos de Soluciones
4. Problemas similares
5. Inferencias

Antes de pensar en código, imaginate una solución paso a paso, como si fueramos a resolver un diagrama de flujo, puedes comparar diferentes soluciones, como si estuvieras solucionando un problema de paso a paso con diferentes rutas, para incluir fuentes sin pegar o copiar una solución ya existente, sino, encontrar una solución óptima para este inconveniente.

*IDEA 3*: 

Actúa como desarollador/ arquitecto de software / videojuego. Puedes revisar este problema de mi proyecto como si fueras un mentor o un profesor.

Lo esperable : {esperable}
Lo actual: {actual}
Error: {errorespecifico}
Falla que yo considero: {fallaconsiderada}
Ptuebas que ya hice: {prueban}
Código relacionado: {codigo}
Solución que yo espero: {soluciónesperada}

No pensemos ni actuemos con código, el punto es que identifiques cada parametro en específico para poder tener por lo menos 4 ideas o hipotesis, proponiendo pruebas rápidas para confirmar o tirar a la basura, con una explicación del por que ocurrió, correcciones y soluciones (sin código) de paso a paso, sin proponer una ya existente.

# Conclusiones de uso de IA:

Verdaderamente, dependiendo de tu estilo de proyecto, la I.A si puede ser una herramienta bastante buena o que aumente tu productividad o tu rango o lo que tu consideres relatviamente importante, pero, a veces si es muy probable que quedes todo hueco y menso pq nunca supiste usarla y te termino dando una estructura completa con archivos ya hechos y quedaste así (._?) pq solamente querías que te explicara un error. El punto es idetnficiarle un rol a cumplir y el contexto necesario, al ser una IA generativa y estar entrenada con 1029209 busquedas previas, verdaderamente no te generará un resultado único, sino es una combinación para lo que estuvo verdaderamente entrenado, así que tendrás que identificar todo de manera clara y concisa.

pd: dale apoyo a este proyecto, andale ( •̀ ω •́ )✧

