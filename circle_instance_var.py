import math

class Circle:
    def __init__(self, name, radius, PI):
        self.name = name
        self.radius = radius
        self.PI = PI



    def area(self):
        return self.PI * self.radius**2

    def __del__(self):
        pass

c1 = Circle('원', 10, math.pi)
#c1.area()
print('c1의 면적은', c1.area())

print(c1.__dict__)


