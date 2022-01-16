from directions import Direction
from player import Player
from region import Region


player = Player(0, 0, 0, 0)

while True:
    print("Which direction do you want to move?")
    action = input().upper()
    direction = None
    match action:
        case "N":
            direction = Direction.NORTH
        case "S":
            direction = Direction.SOUTH
        case "E":
            direction = Direction.EAST
        case "W":
            direction = Direction.WEST
        case "NE":
            direction = Direction.NORTHEAST
        case "NW":
            direction = Direction.NORTHWEST
        case "SE":
            direction = Direction.SOUTHEAST
        case "SW":
            direction = Direction.SOUTHWEST
        case _:
            print("Not a valid direction:")
    player.move_squares(direction, 1)
    print(f"X:{player.x_square} Y:{player.y_square}")

