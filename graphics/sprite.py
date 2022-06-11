import pygame

sprites = pygame.sprite.Group()
"""Every sprite in the game."""

class SSSSprite(pygame.sprite.Sprite):
    def __init__(self, img_path: str, scale: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load(f"resources/images/sprites/{img_path}").convert()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        sprites.add(self)

    def update_pos(self, x, y):
        """Updates the sprite's position on the screen."""
        self.rect.x = x
        self.rect.y = y
