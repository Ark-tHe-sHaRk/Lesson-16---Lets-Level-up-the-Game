import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Custom event for changing sprite colors
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Color Changer")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Sprite class
class ColorChangingSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        new_color = random.choice(COLORS)
        self.image.fill(new_color)

# Create two sprites
sprite1 = ColorChangingSprite((255, 0, 0), 100, 100, 200, 250)
sprite2 = ColorChangingSprite((0, 0, 255), 100, 100, 500, 250)

# Group to manage sprites
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Set a timer for the custom event
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger every 2 seconds

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()