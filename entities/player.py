from entities.being import Being
from positions.directions import Direction
from gameplay.action import GameAction, GameActionType
import gameplay.actions.move_actions as move_actions


class Player(Being):

    def print_menu(self):
        print(f"""
            It's your turn.
            You are at ({self.x_square}, {self.y_square}).
            What do you do?
            1. Move
            2. Interact
            3. Use ability
            4. Attack
            5. Pass
            6. Exit            """)

    def get_move_action(self):
        direction: Direction = Direction.abbreviation_to_enum(
        input("Which direction do you want to move? ")
        )
        while direction == Direction.INVALID:
            print("Invalid direction")
            direction = Direction.abbreviation_to_enum(
                input("Which direction do you want to move?")
            )
        return GameAction(GameActionType.MOVE, 2, lambda: move_actions.relative_teleport(self, direction, 1))

    def tick(self):
        self.print_menu()
        action_choice: int = int(input())
        match action_choice:
            case 1:
                self.current_action = self.get_move_action()
        super().tick()