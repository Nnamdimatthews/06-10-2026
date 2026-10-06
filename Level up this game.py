import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

background = pygame.image.load("Sunset hill.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

pygame.mixer.music.load("10 Sunset Hill Map.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()