from gameplay.signal import Signal



class Entity:
    def __init__(self, name: str, current_action = None):
        self.current_action = current_action

        self.name = name

    def tick(self):
        if self.current_action is not None:
            if self.current_action.is_finished():
                self.current_action = None
            else:
                self.current_action.tick()

    def handle_signal(self, signal: Signal):
        print("I am handling signal", signal)
