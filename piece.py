import random
from constants import COLORS, SHAPES, COLUMNS, ROWS, BG_COLOR

class Piece:
    def __init__(self, shape=None):
        self.shape = shape if shape else random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self, grid):
        rotated = list(zip(*self.shape[::-1]))
        if not self.collides(grid, 0, 0, rotated):
            self.shape = rotated

    def collides(self, grid, dx=0, dy=0, shape=None):
        shape = shape or self.shape
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.x + j + dx, self.y + i + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or (new_y >= 0 and grid[new_y][new_x] != BG_COLOR):
                        return True
        return False

    def move(self, grid, dx, dy):
        if not self.collides(grid, dx, dy):
            self.x += dx
            self.y += dy
            return True
        return False
