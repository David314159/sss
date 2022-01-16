from directions import Direction
from player import Player


player = Player(0, 0, 0, 0)

while True:
    direction = Direction.abbreviation_to_enum(
        input("Which direction do you want to move? ")
    )
    player.move_squares(direction, 1)
    print(f"X:{player.x_square} Y:{player.y_square}")

