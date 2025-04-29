import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_size = 10

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Paddle class
def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))

# Ball class
def draw_ball(x, y):
    pygame.draw.rect(screen, white, (x, y, ball_size, ball_size))

# Main game loop
def game_loop():
    # Paddle positions
    paddle1_y = screen_height // 2 - paddle_height // 2
    paddle2_y = screen_height // 2 - paddle_height // 2

    # Ball position and speed
    ball_x = screen_width // 2 - ball_size // 2
    ball_y = screen_height // 2 - ball_size // 2
    ball_speed_x = 3 * random.choice((1, -1))
    ball_speed_y = 3 * random.choice((1, -1))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with top and bottom
        if ball_y <= 0 or ball_y >= screen_height - ball_size:
            ball_speed_y *= -1

        # Ball collision with paddles
        if (ball_x <= paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \
           (ball_x >= screen_width - paddle_width - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
            ball_speed_x *= -1

        # Ball out of bounds
        if ball_x < 0 or ball_x > screen_width:
            ball_x = screen_width // 2 - ball_size // 2
            ball_y = screen_height // 2 - ball_size // 2
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))

        # Fill the screen with black
        screen.fill(black)

        # Draw paddles and ball
        draw_paddle(0, paddle1_y)
        draw_paddle(screen_width - paddle_width, paddle2_y)
        draw_ball(ball_x, ball_y)

        # Update the display
        pygame.display.flip()

        # Frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == '__main__':
    game_loop()