import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

# Load assets
planet = pygame.image.load("planet4.webp").convert_alpha()
heart = pygame.image.load("heart.webp").convert_alpha()
heart = pygame.transform.scale(heart, (70, 40))
sound = pygame.mixer.Sound("spirals.wav")
sound.play()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (247, 163, 163)
PINK2 = (245, 105, 105)
RED = (255, 0, 0)

# Game variables
health = 500
level = 0
frameCount = 0
down = 1
clock = pygame.time.Clock()

# Obstacles
obstacle_positions = [random.randint(-100, 500) for _ in range(8)]
obstacle_directions = [random.choice([-1, 1]) for _ in range(8)]

# Helper functions
def get_mouse_pos():
    return pygame.mouse.get_pos()

def display_text(text, pos, size=20):
    font = pygame.font.Font("freesansbold.ttf", size)
    rendered = font.render(text, True, WHITE, BLACK)
    rect = rendered.get_rect(center=pos)
    screen.blit(rendered, rect)

def draw_lives():
    if health > 0:
        screen.blit(heart, (470, 10))

def draw_character(broken=False):
    x, y = get_mouse_pos()
    color = RED if broken else PINK
    accent = RED if broken else PINK2
    pygame.draw.rect(screen, color, pygame.Rect(x - 15, y - 30, 120, 60))
    pygame.draw.circle(screen, accent, [x + 15, y], 25)
    pygame.draw.polygon(screen, accent, [(x - 75, y), (x - 15, y - 30), (x - 15, y + 30)])

def draw_obstacles():
    global obstacle_positions, obstacle_directions, down
    planetY = down % HEIGHT
    screen.blit(planet, (planetY, 150))
    screen.blit(planet, (planetY, 600))
    screen.blit(planet, (520, planetY))
    screen.blit(planet, (-50, planetY))

    for i in range(len(obstacle_positions)):
        obstacle_positions[i] += obstacle_directions