
import pygame

pygame.init()
caption = pygame.display.set_caption('Python App')
screen = pygame.display.set_mode([320, 200])  # 窗口大小为640*480

img = pygame.transform.scale(pygame.image.load("test.png"), (90, 100))
rect = img.get_rect().move((115, 30))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen, [255, 0, 0], [300, 0, 20, 40], 1)
    pygame.draw.circle(screen, [0, 0, 0], [20, 20], 20, 1)
    screen.blit(img, rect)

    pygame.display.update()
    screen.fill([255, 255, 255])  # 用白色填充窗口
