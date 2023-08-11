from math import sqrt, pi


class Line:
    coor1: tuple[int, int]
    coor2: tuple[int, int]

    def __init__(self, coor1: tuple[int, int], coor2: tuple[int, int]):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self) -> float:
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self) -> float:
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
distance = li.distance()
print(f"distance: {distance}")


slope = li.slope()
print(f"slope: {slope}")


class Cylinder:
    height: int
    radius: int

    def __init__(self, height: int = 1, radius: int = 1):
        self.height = height
        self.radius = radius

    def volume(self) -> float:
        return pi * self.radius**2 * self.height

    def surface_area(self) -> float:
        return 2 * pi * self.radius * self.height + 2 * pi * self.radius**2


c = Cylinder(2, 3)
volume = c.volume()
print(f"volume: {volume}")
surface_area = c.surface_area()
print(f"surface_area: {surface_area}")
