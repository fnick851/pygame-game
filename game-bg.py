import pygame

background = '2d-land.jpg'

pygame.init()
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("pygame game")

bg = pygame.image.load(background).convert()

y_move = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        screen.blit(bg, (0, y_move))
        y_move -= 1
        pygame.display.update()
        screen.fill([0, 0, 0])
