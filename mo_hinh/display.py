import pygame

pygame.init()

WIDTH = 420
LENGTH = 600
colors = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (142, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 193, 33)}

window = pygame.display.set_mode((WIDTH, LENGTH), pygame.RESIZABLE)
window.fill((255, 255, 255))
surface = pygame.Surface((420, 420))
surface.fill((175, 175, 175))
# set logo
image = pygame.image.load("C:\\Users\phamh\PycharmProjects\Game2048Test\images\\2048logo.png")
pygame.display.set_icon(image)
clock = pygame.time.Clock()
fps = 60


def draw_text(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            font = pygame.font.SysFont(None, 60 - 5 * len(str(value)))
            if value > 0:
                document = font.render("{}".format(value), True, (119, 110, 101))
                center = document.get_rect(center=(100 * j + 60, 100 * i + 60))
                window.blit(document, center)


def draw_block(board):
    for i in range(4):
        for j in range(4):
            value = board[j][i]
            rect = pygame.rect.Rect(100 * i + 20, 100 * j + 20, 80, 80)
            if value < 4098:
                pygame.draw.rect(window, colors[value], rect, 0, 5)
            else:
                pygame.draw.rect(window, (0, 0, 0), rect, 0, 5)
            if value > 0:
                pygame.draw.rect(window, (0, 0, 0), rect, 1, 5)


def draw_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("SCORE: {}".format(score), True, (119, 110, 101))
    window.blit(text, (10, 450))
