

class position:
    set = None
    x = None
    y = None
    z = None
    pos = None
    def __init__(self, x: int | float=None, y: int | float=None, z: int | float=None, pos: tuple[int | float, int | float, int | float]=None):
        has_pos = False
        has_cord = False
        if type(pos) is tuple[int, int, int]:
            print(pos)
            pass
        elif (x, y, z) != (None, None, None):
            if (x, y, z).__contains__(None):
                pass
        self.pos = pos


test = position(pos=(0, 0, 0))

print(type(test.pos))

print(type((int, int, int)))
