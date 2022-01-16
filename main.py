from directions import Direction
from player import Player
from region import Region

player = Player(3, 4, 7, 8)
print(player.x_square)
print(player.y_square)
player.move_squares(Direction.NORTH, 3)
print(player.x_square)
print(player.y_square)