import pygame


pygame.init()


WIDTH = 800
HEIGHT = 600


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Ping Pong")
clock = pygame.time.Clock()


paddle_width = 10
paddle_height = 100
ball_size = 15

player_1_pos = [(HEIGHT // 2) - paddle_height // 2]
player_2_pos = [(HEIGHT // 2) - paddle_height // 2]

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

def draw_paddles():
   
    pygame.draw.rect(screen, WHITE, (10, player_1_pos[0], paddle_width, paddle_height))
    
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, player_2_pos[0], paddle_width, paddle_height))

def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    if ball_x <= 0:
        game_over("Игрок 2 победил!")
    elif ball_x >= WIDTH:
        game_over("Игрок 1 победил!")

    check_collisions()

def check_collisions():
    global ball_speed_x

    if (
        ball_x < paddle_width + 10 and
        player_1_pos[0] < ball_y < player_1_pos[0] + paddle_height
    ):
        ball_speed_x *= -1

    if (
        ball_x > WIDTH - paddle_width - ball_size - 10 and
        player_2_pos[0] < ball_y < player_2_pos[0] + paddle_height
    ):
        ball_speed_x *= -1

def game_over(winner):
    font = pygame.font.Font(None, 36)
    text = font.render(f"{winner}", True, RED)
    screen.blit(text, ((WIDTH // 2) - 100, (HEIGHT // 2)))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_w]:  
        player_1_pos[0] -= 5
    if keys[pygame.K_s]:  
        player_1_pos[0] += 5


    if keys[pygame.K_UP]:  
        player_2_pos[0] -= 5
    if keys[pygame.K_DOWN]:  
        player_2_pos[0] += 5

    
    player_1_pos[0] = max(0, min(HEIGHT - paddle_height, player_1_pos[0]))
    player_2_pos[0] = max(0, min(HEIGHT - paddle_height, player_2_pos[0]))

    screen.fill(BLUE)
    draw_paddles()
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_size)
    move_ball()

    pygame.display.update()
    clock.tick(60)

pygame.quit()