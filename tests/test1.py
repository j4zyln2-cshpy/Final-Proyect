import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            running = False

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()

