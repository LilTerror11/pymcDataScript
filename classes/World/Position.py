from typing import Any


class PositionSetupError(Exception):
    def __init__(self, value=None):
        if value is None:
            value = "1 or more position object in somehtin ghave not been setpu"
        self.value = value


class position:
    set = False
    x = None
    y = None
    z = None

    def __init__(self, x: int | float = None, y: int | float = None, z: int | float = None,
                 pos: tuple[int | float, int | float, int | float] = None,
                 none: Any = 0):
        has_pos = False
        has_cord = False
        if pos is not None:
            passed = 0
            for part in pos:
                if [int, float].__contains__(type(part)):
                    passed += 1
            if passed >= 3:
                has_pos = True
            pass
        elif (x, y, z) != (None, None, None):
            if (x, y, z).__contains__(None) and False:
                pass
            else:
                passed = False
                positions = [x, y, z]
                pos2 = []
                for part in positions:
                    if [int, float].__contains__(type(part)):
                        passed += 1
                    else:
                        if part is None:
                            passed += 1
                            part = none
                    pos2.append(part)
                if passed >= 3:
                    x, y, z = pos2
                    has_cord = True
        if has_cord:
            self.x = x
            self.y = y
            self.z = z
            self.set = True
        elif has_pos:
            self.x = pos[0]
            self.y = pos[1]
            self.z = pos[2]
            self.set = True

    def check_set(self):
        pos = [self.x, self.y, self.z]
        for part in pos:
            if not [int, float].__contains__(type(part)):
                self.set = False

    def __add__(self, other):
        self.check_set()
        if not [int, float].__contains__(type(other)):
            if not isinstance(other, type(self)):
                raise TypeError(f"Type {type(other)} Cannot be added with Type {type(self)}")
            other: position
            other.check_set()
            if not other.set:
                raise PositionSetupError(f"position {other} has not been setup (The second position object)")
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup (The first position object)")
            return position(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup")
            return position(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        self.check_set()
        if not [int, float].__contains__(type(other)):
            if not isinstance(other, type(self)):
                raise TypeError(f"Type {type(other)} Cannot be subtracted with Type {type(self)}")
            other: position
            other.check_set()
            if not other.set:
                raise PositionSetupError(f"position {other} has not been setup (The second position object)")
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup (The first position object)")
            return position(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup")
            return position(self.x - other, self.y - other, self.z - other)

    def __repr__(self):
        if not self.set:
            return "<Unset position object>"
        else:
            return f"<position object (x: {self.x}, y: {self.y}, z: {self.z})>"

    def __bool__(self):
        return self.set

    def __mul__(self, other):
        if not [int, float].__contains__(type(other)):
            if not isinstance(other, type(self)):
                raise TypeError(f"Type {type(other)} Cannot be multiplied with Type {type(self)}")
            other: position
            if not other.set:
                raise PositionSetupError(f"position {other} has not been setup (The second position object)")
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup (The first position object)")
            return position(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            if not self.set:
                raise PositionSetupError(f"position {self} has not been setup")
            return position(self.x * other, self.y * other, self.z * other)

