import pygame

from graphics.sprite import entity_sprites, effect_sprites, resource_bars, dead_resource_bars, visible_entity_sprites
from graphics.window import screen, background_color

def tick_group(group: pygame.sprite.Group):
    """Helper function that can tick an entire group of sprites"""
    for sprite in group:
        sprite.tick()


def tick_graphics():
    """Updates all the graphics based on the current game state"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    entity_sprites.update()
    tick_group(entity_sprites)

    effect_sprites.update()
    tick_group(effect_sprites)


    visible_entity_sprites.draw(screen)
    effect_sprites.draw(screen)


    for bar in resource_bars:
        bar.tick()

    for bar in dead_resource_bars:
        resource_bars.remove(bar)
    dead_resource_bars.clear()

    pygame.display.update()
    screen.fill(background_color)

