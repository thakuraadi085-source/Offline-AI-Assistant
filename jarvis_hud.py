import pygame
import math
import threading
import time
import psutil
import datetime

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS AI HOLOGRAM")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------

BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 150, 255)
WHITE = (220, 255, 255)

# ---------------- STATE ----------------

running = True
pulse = 0
rotation = 0

status_text = "WAITING FOR WAKE WORD : JARVIS"

wave = [0] * 100

# ---------------- BACKGROUND THREAD ----------------

def animation_thread():
    global pulse

    while running:
        pulse += 0.08
        time.sleep(0.02)


threading.Thread(
    target=animation_thread,
    daemon=True
).start()

# ---------------- FONT ----------------

title_font = pygame.font.SysFont("consolas", 28, bold=True)
hud_font = pygame.font.SysFont("consolas", 18)
small_font = pygame.font.SysFont("consolas", 15)

# ---------------- LOOP ----------------

while running:

    screen.fill(BLACK)

    center_x = WIDTH // 2
    center_y = HEIGHT // 2 - 40

    rotation += 1

    # ==================================================
    # OUTER RINGS
    # ==================================================

    for radius in [90, 130, 170, 210]:

        pygame.draw.circle(
            screen,
            CYAN,
            (center_x, center_y),
            radius,
            1
        )

    # ==================================================
    # ROTATING NODES
    # ==================================================

    for i in range(24):

        angle = math.radians(rotation + i * 15)

        x = center_x + math.cos(angle) * 210
        y = center_y + math.sin(angle) * 210

        pygame.draw.circle(
            screen,
            BLUE,
            (int(x), int(y)),
            4
        )

    # ==================================================
    # CORE
    # ==================================================

    core_radius = 45 + int(math.sin(pulse) * 10)

    pygame.draw.circle(
        screen,
        CYAN,
        (center_x, center_y),
        core_radius
    )

    pygame.draw.circle(
        screen,
        BLUE,
        (center_x, center_y),
        core_radius + 15,
        3
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (center_x, center_y),
        10
    )

    # ==================================================
    # WAVEFORM
    # ==================================================

    for i in range(len(wave)):
        wave[i] = math.sin(pulse + i * 0.25) * 30

    base_y = HEIGHT - 120

    for i in range(len(wave) - 1):

        x1 = 50 + i * 9
        y1 = base_y + wave[i]

        x2 = 50 + (i + 1) * 9
        y2 = base_y + wave[i + 1]

        pygame.draw.line(
            screen,
            CYAN,
            (x1, y1),
            (x2, y2),
            2
        )

    # ==================================================
    # TITLE
    # ==================================================

    title = title_font.render(
        "JARVIS AI CORE",
        True,
        CYAN
    )

    screen.blit(title, (20, 20))

    # ==================================================
    # STATUS
    # ==================================================

    status = hud_font.render(
        status_text,
        True,
        WHITE
    )

    screen.blit(status, (20, 65))

    # ==================================================
    # SYSTEM INFO
    # ==================================================

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    if battery:
        battery_text = f"{battery.percent}%"
    else:
        battery_text = "N/A"

    current_time = datetime.datetime.now().strftime(
        "%d-%m-%Y  %I:%M:%S %p"
    )

    info_lines = [
        f"CPU : {cpu} %",
        f"RAM : {ram} %",
        f"BATTERY : {battery_text}",
        f"TIME : {current_time}"
    ]

    y = 110

    for line in info_lines:

        txt = small_font.render(
            line,
            True,
            CYAN
        )

        screen.blit(txt, (20, y))

        y += 25

    # ==================================================
    # CORNER SCAN LINES
    # ==================================================

    for i in range(0, WIDTH, 30):

        pygame.draw.line(
            screen,
            (0, 40, 40),
            (i, 0),
            (i + 20, HEIGHT),
            1
        )

    # ==================================================
    # EVENTS
    # ==================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()