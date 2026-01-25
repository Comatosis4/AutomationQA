class Rhombus:
    angle_b: int

    def __init__(self, side:int, angle_a: int):
        self.side = side
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side' and value <= 0:
            raise AttributeError(f'Side must be > 0')

        elif key == 'angle_a':
             if not 0 < value < 180:
                raise AttributeError(f'Angle is not in the range')
             super().__setattr__(key,value)
             super().__setattr__('angle_b', 180 - value)

        else:
            super().__setattr__(key,value)

bob = Rhombus(side = 13, angle_a = 12)
print(bob.angle_a)
print(bob.angle_b)
print(bob.side)


