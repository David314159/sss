from enum import Enum, auto


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    WEST = auto()
    SOUTH = auto()
    NORTHEAST = auto()
    SOUTHEAST = auto()
    NORTHWEST = auto()
    SOUTHWEST = auto()

    @staticmethod
    # quotes around the "Direction" typehint because python is being cringe
    # see https://www.python.org/dev/peps/pep-0484/#forward-references
    def str_to_direction(string: str) -> 'Direction':
        str_to_direction_dict = {
            'N': Direction.NORTH,
            'NE': Direction.NORTHEAST,
            'E': Direction.EAST,
            'SE': Direction.SOUTHWEST,
            'S': Direction.SOUTH,
            'SW': Direction.SOUTHWEST,
            'W': Direction.WEST,
            'NW': Direction.NORTHWEST,
        }
        return str_to_direction_dict[string.upper()]
