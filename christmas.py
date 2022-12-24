import pygame
import random

 
pygame.init()
window_size = (900, 600)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Christmas Greeting")
screen.fill((255, 0, 0))
font_color = (255, 255, 255)
font = pygame.font.SysFont("comicsansms", 56)

text = font.render("Merry Christmas!", True, font_color)
text_size = text.get_size()
text_x = (window_size[0] - text_size[0]) // 2
text_y = (window_size[1] - text_size[1]) // 2
 
snowflakes = []
num_snowflakes = 100
snowflake_size = 5
snowflake_speed = 1

for i in range(num_snowflakes):
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])

    dx = random.uniform(-snowflake_speed, snowflake_speed)
    dy = random.uniform(snowflake_speed,  3 * snowflake_speed)

    snowflake = (x, y, dx, dy)
    snowflakes.append(snowflake)
 
running = True
while running:
    screen.fill((255, 0, 0))
    screen.blit(text, (text_x, text_y))
    for snowflake in snowflakes:
        x, y, dx, dy = snowflake
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), snowflake_size)
    for i in range(num_snowflakes):
        x, y, dx, dy = snowflakes[i]
        x += dx
        y += dy
        if x < 0 or x > window_size[0]:
            dx = -dx
        if y > window_size[1]:
            y = 0
        snowflakes[i] = (x, y, dx, dy)

    pygame.display.flip()

   


