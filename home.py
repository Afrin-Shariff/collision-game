import pygame
import random

def displayLevel():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("level: " + str(level), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (440, 40)
    screen.blit(text, textRect)

def displayHealth():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("health: " + str(health), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (415, 15)
    screen.blit(text, textRect)

def drawLives():
    if health > 0:
        screen.blit(heart,(470, 10))

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

# Initialize positions and directions for obstacles
obstacle_positions = [random.randint(-100, 500) for _ in range(8)]
obstacle_directions = [random.choice([-1, 1]) for _ in range(8)]

def drawObstacle():

    planetY = 0 + down
    planetY = planetY % 500
    screen.blit(planet,(planetY,150))

    planetY2 = 0 + down
    planetY2 = planetY2 % 500
    screen.blit(planet,(planetY2,600))

    planetY3 = 0 + down
    planetY3 = planetY3 % 500
    screen.blit(planet,(520, planetY3))

    planetY4 = 0 + down
    planetY4 = planetY4 % 500
    screen.blit(planet,(-50, planetY4))
    
    for i in range(2):
            global obstacle_positions

            for i in range(len(obstacle_positions)):
                # Move obstacle up or down based on its direction
                obstacle_positions[i] += obstacle_directions[i] * 2 # Speed of movement

                # If an obstacle goes out of bounds, reverse its direction
                if obstacle_positions[i] <= 0 or obstacle_positions[i] >= 800:
                    obstacle_directions[i] *= -1
                   
                screen.blit(planet, (25 + i * 100, obstacle_positions[i]))  # Adjust X position based on the index

    pass

obstacle_positions = [random.randint(-100, 500) for _ in range(8)]
obstacle_directions = [random.choice([-1, 1]) for _ in range(8)]

def drawGood():
    
        for i in range(2):
            global obstacle_positions

            for i in range(len(obstacle_positions)):
                # Move obstacle up or down based on its direction
                obstacle_positions[i] += obstacle_directions[i] * 2 # Speed of movement

                # If an obstacle goes out of bounds, reverse its direction
                if obstacle_positions[i] <= 0 or obstacle_positions[i] >= 800:
                    obstacle_directions[i] *= -1
                   
def drawCharacter():
    x,y = getPos()
   
    PINK = (247, 163, 163)
    YELLOW = (237, 232, 126)
    PINK2 = (245, 105, 105)

    pygame.draw.rect(screen, PINK, pygame.Rect(x-15,y-30, 120, 60))
    pygame.draw.circle(screen, PINK2, [x+15,y+0], 25, 0)
    pygame.draw.polygon(screen, PINK2, points=[(x-75,y+00), (x-15,y-30), (x-15,y+30)])
    pygame.draw.polygon(screen, PINK2, points=[(x-75,y+00), (x-15,y-30), (x-15,y+30)])

def drawBrokenCharacter():
    x,y = getPos()
   
    RED = (255, 000, 000)

    pygame.draw.rect(screen, RED, pygame.Rect(x-15,y-30, 120, 60))
    pygame.draw.circle(screen, RED, [x+15,y+0], 25, 0)
    pygame.draw.polygon(screen, RED, points=[(x-75,y+00), (x-15,y-30), (x-15,y+30)])
    pygame.draw.polygon(screen, RED, points=[(x-75,y+00), (x-15,y-30), (x-15,y+30)])

def draw():

    global health
    
    safeColour = (0, 0, 0) # add the safe background colour 
    screen.fill(safeColour)
    
    drawGood()
    drawObstacle() # draw obstacles
    x,y = getPos() #get the position of the mouse
    collide = screen.get_at((x, y))[:3]
    if collide == (0, 0, 0):
        drawCharacter()
    else:
        print(collide)
        drawBrokenCharacter()
        health = health - 5
    displayLevel()
    displayHealth()
    drawLives()
########################################################
# main code
pygame.init()

screen = pygame.display.set_mode([800, 800])

heart = pygame.image.load("heart.webp").convert_alpha()
heart = pygame.transform.scale(heart,(70,40))
running = True
frameCount = 1
level = 0
health = 500
planet = pygame.image.load("planet4.webp").convert_alpha()
pygame.mixer.init()
sound = pygame.mixer.Sound("spirals.wav")
sound.play()
down = 1
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw to the screen
    down = down + 1
    draw()
    frameCount = frameCount + 1
    level = frameCount//250
    
    # Flip the display
    pygame.display.flip()
    pygame.time.wait(10-level)

    if health == 0:
        pygame.quit()
    
# Done! Time to quit.
pygame.quit()