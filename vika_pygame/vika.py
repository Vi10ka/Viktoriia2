import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

x, y = 200, 150
speed = 3

# Кольори
background_color = (163, 157, 245)
rect_color = (216, 58, 106)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, (x, y, 50, 50))
    pygame.display.flip()



    clock.tick(60)

pygame.quit()   
