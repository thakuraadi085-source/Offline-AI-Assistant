import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS HUD")

clock = pygame.time.Clock()

CYAN = (0, 255, 255)
BLUE = (0, 180, 255)
WHITE = (220, 255, 255)
BLACK = (0, 0, 0)

angle = 0

font_small = pygame.font.SysFont("Arial", 14)
font_big = pygame.font.SysFont("Arial", 24)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    cx = WIDTH // 2
    cy = HEIGHT // 2

    angle += 1

    # Glow Center
    for r in range(80, 0, -10):
        pygame.draw.circle(screen, (0, 80 + r, 255), (cx, cy), r)

    # Main Reactor Ring
    pygame.draw.circle(screen, CYAN, (cx, cy), 180, 4)

    # Rotating Ring 1
    for i in range(0, 360, 20):
        a = math.radians(i + angle)
        x = cx + math.cos(a) * 220
        y = cy + math.sin(a) * 220
        pygame.draw.circle(screen, CYAN, (int(x), int(y)), 4)

    # Rotating Ring 2
    for i in range(0, 360, 10):
        a = math.radians(i - angle)
        x = cx + math.cos(a) * 270
        y = cy + math.sin(a) * 270

        pygame.draw.line(
            screen,
            BLUE,
            (cx + math.cos(a) * 250,
             cy + math.sin(a) * 250),
            (x, y),
            2
        )

    # Wave Ring
    for i in range(360):
        a = math.radians(i)
        wave = 300 + math.sin(math.radians(i * 4 + angle * 3)) * 10

        x = cx + math.cos(a) * wave
        y = cy + math.sin(a) * wave

        pygame.draw.circle(screen, CYAN, (int(x), int(y)), 1)

    # Outer Ring
    pygame.draw.circle(screen, BLUE, (cx, cy), 320, 2)

    # HUD Crosshair
    pygame.draw.line(screen, CYAN, (cx - 350, cy), (cx + 350, cy), 1)
    pygame.draw.line(screen, CYAN, (cx, cy - 350), (cx, cy + 350), 1)

    # Side Panels
    pygame.draw.rect(screen, CYAN, (40, 120, 260, 650), 2)
    pygame.draw.rect(screen, CYAN, (1300, 120, 260, 650), 2)

    # Top Line
    pygame.draw.line(screen, CYAN, (0, 50), (WIDTH, 50), 2)

    for i in range(1, 31):
        txt = font_small.render(str(i).zfill(2), True, CYAN)
        screen.blit(txt, (i * 50, 15))

    # JARVIS Title
    title = font_big.render("JARVIS AI SYSTEM", True, WHITE)
    screen.blit(title, (WIDTH//2 - 120, 40))

    # Invented By
    credit = font_small.render(
        "Invented by Aditya Singh Rajput",
        True,
        CYAN
    )

    screen.blit(
        credit,
        (WIDTH - 220, HEIGHT - 20)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()