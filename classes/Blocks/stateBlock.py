from block import block


class stateBlock(block):
    def __init__(self, name: str, states: dict):
        super().__init__(name)
        self.states: dict = states