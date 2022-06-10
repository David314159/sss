import pygame

sprites = pygame.sprite.Group()
"""Every sprite in the game."""


class PlayerSprite(pygame.sprite.Sprite):
    """A sprite representing a player. Only handles graphics stuff."""
    def __init__(self):
        """Constructs the sprite, loads the image, sets its position, and adds self to the sprites group"""
        super().__init__()
        self.image = pygame.image.load("resources/images/sprites/captain_alex.png").convert()
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        sprites.add(self)

    def update_pos(self, x, y):
        """Updates the sprite's position on the screen."""
        self.rect.x = x
        self.rect.y = y


def init_sprites():
    """Constructs the sprites that should be in the game."""
    player = PlayerSprite()
