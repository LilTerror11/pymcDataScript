from stateBlock import stateBlock


class nbtBlock(stateBlock):
    def __init__(self, name: str, states: dict, nbt: dict):
        super().__init__(name, states)
        self.nbt: dict = nbt