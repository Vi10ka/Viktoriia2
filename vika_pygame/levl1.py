import pygame
import random

pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Гравець — коло (велике поле)")

player_x = 2500  # початкова позиція гравця посеред великого поля
player_y = 2500
player_radius = 15
player_color = (183, 176, 245)
speed = 5
max_radius = 300

clock = pygame.time.Clock()

# Велике поле гри
map_width = 5000
map_height = 5000

font = pygame.font.SysFont(None, 30)

class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, map_width)
        self.y = random.randint(0, map_height)
        self.radius = 10
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, self.color, (self.x + offset_x, self.y + offset_y), self.radius)

# Багато їжі по всьому великому полі
foods = [Food() for _ in range(1000)]

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < map_width:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < map_height:
        player_y += speed

    # Зсув карти відносно гравця
    offset_x = -player_x + screen_width // 2
    offset_y = -player_y + screen_height // 2

    # Перевірка зіткнення з їжею
    for food in foods:
        distance = ((player_x - food.x)**2 + (player_y - food.y)**2)**0.5
        if distance < player_radius + food.radius:
            if player_radius < max_radius:
                player_radius += 2
            food.spawn()

    screen.fill((173, 216, 230))
    for food in foods:
        food.draw(screen, offset_x, offset_y)
    pygame.draw.circle(screen, player_color, (screen_width // 2, screen_height // 2), player_radius)

    # Індикатор прогресу
    progress_width = 300
    progress_height = 20
    progress_x = 10
    progress_y = 10
    pygame.draw.rect(screen, (100, 100, 100), (progress_x, progress_y, progress_width, progress_height))
    progress_ratio = player_radius / max_radius
    pygame.draw.rect(screen, (0, 255, 0), (progress_x, progress_y, int(progress_width * progress_ratio), progress_height))
    text = font.render(f"Розмір: {player_radius}/{max_radius}", True, (0, 0, 0))
    screen.blit(text, (progress_x, progress_y + progress_height + 5))

    pygame.display.flip()

pygame.quit()
