import sys
import pygame

pygame.init()

screencita = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Prueba 5 xd")
clock = pygame.time.Clock()


duende_x, duende_ran, vel_duende = 50, 20, 90
torre_x, torre_vida = 650, 100
last_attack, cooldown = 0, 100

while True:
    dt = clock.tick(60) / 1000
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sys.exit()

    collis = abs(duende_x - torre_x) <= duende_ran

    if not collis:
        duende_x += vel_duende * dt #el punto es que la posición x del duende se actualice cada frame
        # pene
    else:
        if time - last_attack >= cooldown and torre_vida > 0: 
            torre_vida = max(0, torre_vida - 10) #le restamos 10 puntos al hp de la torre
            last_attack = time # y cada aauq ese actualizará con el tiempo establecido

    screencita.fill((25, 30, 40))
    pygame.draw.line(screencita, (100, 100, 100), (0, 300), (800, 300), 4)

    pygame.draw.rect(screencita, (200, 50, 50) if collis else (50, 200, 50), (int(duende_x), 270, 30, 30),)
    pygame.draw.rect(screencita, (70, 130, 240), (int(torre_x), 215, 50, 90))

    font = pygame.font.SysFont("Courier New", 16) #si, lo busque en google XDDDDD
    text = font.render(f"Distancia: {abs(duende_x - torre_x):.2f}; Torre HP: {torre_vida}", True, (255, 255, 255))

    screencita.blit(text, (20, 20))


    pygame.display.flip()

pygame.quit()
sys.exit()