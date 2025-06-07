import pygame
import sys

# --- Secure Input Validation for Paddle Speed ---
MIN_PADDLE_SPEED = 1
MAX_PADDLE_SPEED = 20
DEFAULT_PADDLE_SPEED = 5

def get_valid_paddle_speed():
    try:
        # Check if argument is provided
        if len(sys.argv) > 1:
            user_input = sys.argv[1]
            paddle_speed = int(user_input)
            if MIN_PADDLE_SPEED <= paddle_speed <= MAX_PADDLE_SPEED:
                return paddle_speed
            else:
                print(f"Input paddle_speed {paddle_speed} out of bounds ({MIN_PADDLE_SPEED}-{MAX_PADDLE_SPEED}). Using default.")
        else:
            print("No paddle_speed argument provided. Using default.")
    except ValueError:
        print("Invalid paddle_speed input. Must be an integer. Using default.")
    return DEFAULT_PADDLE_SPEED

paddle_speed = get_valid_paddle_speed()

# --- Pygame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Secure Ping Pong")

# Game Elements
ball = pygame.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle.bottom < height:
        paddle.y += paddle_speed

    # Ball Movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] *= -1
    if ball.colliderect(paddle):
        ball_speed[0] *= -1

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
