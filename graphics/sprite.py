import pygame

sprites = pygame.sprite.Group()


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/images/sprites/captain_alex.png").convert()
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        sprites.add(self)

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


def init_sprites():
    player = PlayerSprite()
