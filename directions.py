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
    INVALID = auto()

    @staticmethod
    # quotes around the "Direction" typehint because python is being cringe
    # see https://www.python.org/dev/peps/pep-0484/#forward-references
    def abbreviation_to_enum(abrv: str) -> 'Direction':
        match abrv.upper():
            case "N":
                return Direction.NORTH
            case "S":
                return Direction.SOUTH
            case "E":
                return Direction.EAST
            case "W":
                return Direction.WEST
            case "NE":
                return Direction.NORTHEAST
            case "SE":
                return Direction.SOUTHEAST
            case "NW":
                return Direction.NORTHWEST
            case "SW":
                return Direction.SOUTHWEST
            case _:
                return Direction.INVALID
