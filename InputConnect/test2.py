import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Create the Pygame window
window = pygame.display.set_mode((window_width, window_height))

# Run the game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # Quit Pygame

    # Game logic and rendering
    window.fill((255, 255, 255))  # Fill the window with white color
    pygame.display.update()

# Reopen the window with the same code
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # Quit Pygame

    # Game logic and rendering
    window.fill((255, 255, 255))  # Fill the window with white color
    pygame.display.update()