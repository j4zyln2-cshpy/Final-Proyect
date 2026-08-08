# Ventajas de un Enfoque 1D:

- Lógica y Matemática mas Simple: A veces, para detectar colisiones, podrías tardar más de 2029209209202902902920 siglos, bueno, en este caso, calcular disparos, intercepciones, o ataques extra, solo se necesitaría comparar si |X1 - X2| <= distancia, en lugar de trabajar con ánuglos o sprites de rotación, teniendo que volver a hacer el jugador en cada uno de los ejes o hacer sprites de animaciones de más (por experiencia)

- No Pathfiding: En un mapa 2D, en Gdevelop por ejemplo, los enemigos SIEMPRE necesitan algoritmos (como A*) para esquivar obstáculos o seguir caminos. En 1D solo se mueven en una dirección (arriba/abajo)

- Un balance más relajao papi: Si papi, calculando el tiempo que tarde un enemigo en atacar es literalmente la fórmula más fácil (t = d/v). Por ejemplo, a mi me facilita esto para ajustar oleadas, o costo de mejoras

- Desarrollo Visual y Sprites Rápido: No debería de animar para 4 / 8 DIMENSIONES EL MISMO PERSONAJE DE PUTA MIERDA NOJODA ME CAE MAL ANIMAR ESA MIEDA EN 8 DIRECCIONES EN ASESPRITE COÑO. Ya calmandome, solo necesito el perfil lateral xd

# Desventajas de trabajar con 1D:

-- Limitaciones: Aquí estás jodido porque el posicionamiento siempre es lineal y con menos opciones, en 2D tu puedes elegir estratégicamente dónde ubicar tus torres en una cuadrícula para optimizar el área de cobertura.

-- Visual Depth (o suerposición de sprites): Al estar TODOS en la misma coordenada Y, si coinciden 939209309309303903 duendes y 4 caballeros, todos estarán amontonados exactamente en el mismo punto a menos que que use un offset o manejo de capas.

-- Menos Variedad en Mapas: Obviamente, los mapas en 1D se reducen a líneas rectas o carriles únicos, limitando la posibilidad de crear atajos, caminos bifurcados o laberintos, o lo que deseas implementar.

# Que tiene de bueno/malo pygame para desarrollo de juegos (principalmente juegos que no sean de 3D):

1) (En mi opinión, la más favorable para este tipo de mierdas) Control Total del Game Loop: En GameMaker o GDevelop. Pygame me da todo el control para que yo elija cuando procesar estados, actualizar estados de objetos, limpiar o redibujar, etc

2) Por lo que tengo entendido, como no carga con librerías de física 3D o motores de renderizado, ni tipo de layouts especializados.  Si solo necesitas mover rectángulos, sprites y verificar distancias en un eje, o solamente quieres hacer cosas bidimensionales con mapas más planos que tu novia, como lo es esto de ej. , la ejecución en Python con Pygame es casi instantánea.

3) Tiene un Manejo Ligero de Superficies (Surface). Dibujar gráficos 2D pixel-art es extremadamente rápido y eficiente, lo único es que es tedioso, hablando desde experiencia propia, si vas a hacer juegos donde existan muchos personajes y estos interactúen, agarrarías la misma plantilla UNA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA Y OTRA VEEEEEEEEZ, para poder dibujar sus direcciones, arriba, abajo, izquierda, derecha, salto, caminar, correr, agacharse, etc, y para eso necesitas BASTANTE PRACTICA, sobre todo para animar. Bueno, pygame permite manipular directamente matrices de píxeles, aplicar transparencias (alpha) y escalar superficies con muy poco consumo de CPU/GPU, ahorrandote todo el proceso.

4) Utilizando clases de python te rsuelve más de la cuenta tu vida con el hecho de que en lugar de tener que volver a repetir procesos tediosos para patrones como Component, Object Pooling, State Machine, python no impone restricciones, los trabaja de forma transparentes utilizando clases estándar de python