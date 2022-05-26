from enum import Enum
from entities.entity import Entity
from positions.directions import Direction


def absolute_teleport(entity: Entity, x_square: int, y_square: int):
    # Remove entity from current square
    current_region: Region = global_map.get_val(entity.x_region, entity.y_region)
    current_square: Square = current_region.get_val(entity.x_square, entity.y_square)
    current_square.entities.remove(entity)

    # Update variables
    entity.x_square = x_square
    entity.y_square = y_square

    # Add entity to new square
    new_region: Region = global_map.get_val(entity.x_region, entity.y_region)
    new_square: Square = new_region.get_val(entity.x_square, entity.y_square)
    new_square.entities.add(entity)


def relative_teleport(entity: Entity, direction: Enum, num_squares):
    match direction:
        case Direction.NORTH:
            absolute_teleport(entity, entity.x_square, entity.y_square + num_squares)
        case Direction.EAST:
            absolute_teleport(entity, entity.x_square + num_squares, entity.y_square)
        case Direction.WEST:
            absolute_teleport(entity, entity.x_square - num_squares, entity.y_square)
        case Direction.SOUTH:
            absolute_teleport(entity, entity.x_square, entity.y_square - num_squares)
        case Direction.NORTHEAST:
            relative_teleport(entity, Direction.NORTH, num_squares)
            relative_teleport(entity, Direction.EAST, num_squares)
        case Direction.SOUTHEAST:
            relative_teleport(entity, Direction.SOUTH, num_squares)
            relative_teleport(entity, Direction.EAST, num_squares)
        case Direction.NORTHWEST:
            relative_teleport(entity, Direction.NORTH, num_squares)
            relative_teleport(entity, Direction.WEST, num_squares)
        case Direction.SOUTHWEST:
            relative_teleport(entity, Direction.SOUTH, num_squares)
            relative_teleport(entity, Direction.WEST, num_squares)

