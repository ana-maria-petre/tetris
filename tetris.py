import pygame
from piece import Piece
from constants import WIDTH, HEIGHT, PANEL_WIDTH, BLOCK_SIZE, BG_COLOR, GRID_COLOR

class Tetris:
    def __init__(self):
        self.grid = [[BG_COLOR for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]
        self.piece = Piece()
        self.next_piece = Piece()
        self.score = 0
        self.game_over = False
        self.drop_time = pygame.time.get_ticks()

    def lock_piece(self):
        for i, row in enumerate(self.piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.piece.y + i][self.piece.x + j] = self.piece.color
        self.check_lines()
        self.piece = self.next_piece
        self.next_piece = Piece()
        if self.piece.collides(self.grid):
            self.game_over = True

    def check_lines(self):
        full_rows = [i for i, row in enumerate(self.grid) if all(cell != BG_COLOR for cell in row)]
        for row in full_rows:
            del self.grid[row]
            self.grid.insert(0, [BG_COLOR for _ in range(WIDTH // BLOCK_SIZE)])
        self.score += len(full_rows) * 100

    def restart(self):
        self.__init__()

    def hard_drop(self):
        while self.piece.move(self.grid, 0, 1):
            pass
        self.lock_piece()

    def update(self, SPEED):
        current_time = pygame.time.get_ticks()
        if current_time - self.drop_time > SPEED:
            if not self.piece.move(self.grid, 0, 1):
                self.lock_piece()
            self.drop_time = current_time

    def draw(self, screen):
        screen.fill(BG_COLOR)
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRID_COLOR, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for i, row in enumerate(self.piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.piece.color, ((self.piece.x + j) * BLOCK_SIZE, (self.piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        self.draw_side_panel(screen)

    def draw_side_panel(self, screen):
        pygame.draw.rect(screen, (230, 230, 230), (WIDTH, 0, PANEL_WIDTH, HEIGHT))
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (50, 50, 50))
        screen.blit(score_text, (WIDTH + 20, 50))
        pygame.draw.rect(screen, (200, 200, 200), (WIDTH + 20, HEIGHT - 70, 110, 40))
        restart_text = font.render("Restart", True, (50, 50, 50))
        screen.blit(restart_text, (WIDTH + 40, HEIGHT - 60))
        for i, row in enumerate(self.next_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.next_piece.color, (WIDTH + 50 + j * BLOCK_SIZE, 150 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
