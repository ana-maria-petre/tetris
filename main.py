import pygame
from tetris import Tetris
from constants import WIDTH, HEIGHT, PANEL_WIDTH, SPEED

pygame.init()
screen = pygame.display.set_mode((WIDTH + PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
game = Tetris()

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.piece.move(game.grid, -1, 0)
            elif event.key == pygame.K_RIGHT:
                game.piece.move(game.grid, 1, 0)
            elif event.key == pygame.K_DOWN:
                game.piece.move(game.grid, 0, 1)
            elif event.key == pygame.K_UP:
                game.piece.rotate(game.grid)
            elif event.key == pygame.K_SPACE:
                game.hard_drop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if WIDTH + 20 <= x <= WIDTH + 130 and HEIGHT - 70 <= y <= HEIGHT - 30:
                game.restart()

    game.update(SPEED)
    game.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
