import sys
import pygame
from src.core.config import screen_height, screen_width, fps, game_title

def pruebapene():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"{game_title}: prueba 6, colisiones de mi polla")
    reloj = pygame.time.Clock()

    duende_x = 50.0 #la posición x del duende 
    duende_vel = 100.0 #la velocidad del duende, baja para ser un rpg, pero si fuese el fifa yo abandonase el juego
    duende_ancho = 40 #el ancho del duende, o el rango x del duende
    duende_rango = 30 #el rango o nivel del duende

    torre_x = 650.0 #la posición x de la torre
    torre_vida_max = 100 # la vida maxima de la torre
    torre_vida = 100 # su vida actual

    cooldown_ataque = 0.8  #tiempo de espera de ataque de 0.8 segundos
    tiempo_acumulado = 0.0

    executing = True
    while executing:
        dt = reloj.tick(fps) / 1000.0 #60 fps por loop frame 

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                executing = False

        distance = abs((duende_x + duende_ancho) - torre_x) #distancia creador
        collidir = distance <= duende_rango #en ese caso, la distancia siempre es menor o igual al rango del duende

        if not collidir: #en el caso de que no exista, hay que buscar la forma para poder igualarlo en su eje x y que la variable collidir pueda ser tomada por el programa
            duende_x += duende_vel * dt
        else:
            tiempo_acumulado += dt #en ese caso, le suamamos al tiempo acumulado lo que tenemos en la variable dt
            if tiempo_acumulado >= cooldown_ataque and torre_vida > 0: #si el tiempo acumulado, la torre de vida recibirá daño
                torre_vida = max(0, torre_vida - 15)
                tiempo_acumulado = 0.0

        pantalla.fill((30, 35, 45)) # renderizamos la pantalla

        pygame.draw.line(pantalla, (100, 100, 100), (0, 300), (800, 300), 4) #dibujamos la linea del suelo


        duende_color = (220, 50, 50) if collidir else (50, 200, 50) # coloreamos al duende
        pygame.draw.rect(
            pantalla, duende_color, (int(duende_x), 260, duende_ancho, 40)
        )
        pygame.draw.rect(
            pantalla, (70, 130, 240), (int(torre_x), 200, 60, 100)
        )

        ancho_barra = int((torre_vida / torre_vida_max) * 60)
        pygame.draw.rect(pantalla, (200, 0, 0), (int(torre_x), 185, 60, 8))
        pygame.draw.rect(
            pantalla, (0, 220, 0), (int(torre_x), 185, ancho_barra, 8)
        )

        fuente = pygame.font.SysFont("Arial", 16)
        statement = (
            "IN A FIGHT" if collidir else "Marching..."
        )
        txt = fuente.render(
            f"Estado: {statement} | Vida Torre: {torre_vida}%",
            True,
            (255, 255, 255),
        )
        pantalla.blit(txt, (20, 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pruebapene()