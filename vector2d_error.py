

#unsupported operand type(s) for +: 'Vector2d' and 'Vector2d'
#생성자만 만든다고해서 계산을 할수있는것은 아님

class Vector2d:
    def __init__(self, x, y):

        self.x = x
        self.y = y


v1 = Vector2d(1,2)
v2 = Vector2d(3,4)


v3 = v1 + v2

