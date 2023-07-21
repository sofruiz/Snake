import pygame
import random

pygame.init()

Ven_W = 600
Ven_H = 400
Ventana = pygame.display.set_mode((Ven_W, Ven_H))
pygame.display.set_caption("Juego de Snake")

SnakeT = 10
SnakeC = (0, 255, 0)
SnakeX = Ven_W / 2
SnakeY = Ven_H / 2
SnakeV = 10
SnakeB = [(SnakeX, SnakeY)]

ComidaT = 10
ComidaC = (255, 0, 0)
ComidaX = random.randint(0, Ven_W - ComidaT)
ComidaY = random.randint(0, Ven_H - ComidaT)

score = 0
score_font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Movimiento con teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        SnakeY -= SnakeV
    if keys[pygame.K_DOWN]:
        SnakeY += SnakeV
    if keys[pygame.K_LEFT]:
        SnakeX -= SnakeV
    if keys[pygame.K_RIGHT]:
        SnakeX += SnakeV

    # Actualiza la serpiente cuando come
    SnakeB.insert(0, (SnakeX, SnakeY))
    if len(SnakeB) > score + 1:
        SnakeB.pop()

    # Revisa la colision con la comida
    if SnakeX < ComidaX + ComidaT and SnakeX + SnakeT > ComidaX and SnakeY < ComidaY + ComidaT and SnakeY + SnakeT > ComidaY:
        ComidaX = random.randint(0, Ven_W - ComidaT)
        ComidaY = random.randint(0, Ven_H - ComidaT)
        score += 1

    # Colision con las paredes
    if SnakeX < 0 or SnakeX + SnakeT > Ven_W or SnakeY < 0 or SnakeY + SnakeT > Ven_H:
        pygame.quit()
        quit()

    # Crea la serpiente y comida
    Ventana.fill((255, 255, 255))
    for i in range(len(SnakeB)):
        pygame.draw.rect(Ventana, SnakeC, [SnakeB[i][0], SnakeB[i][1], SnakeT, SnakeT])
    pygame.draw.rect(Ventana, ComidaC, [ComidaX, ComidaY, ComidaT, ComidaT])

    # Score
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    Ventana.blit(score_text, (10, 10))

    # Actualiza la pantalla
    pygame.display.update()

    clock.tick(20)
