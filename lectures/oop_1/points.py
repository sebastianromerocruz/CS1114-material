import math

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_distance_from(self, another_point):
        return math.dist([self.x, self.y], [another_point.x, another_point.y])


if __name__ == '__main__':
    point1 = Coordinates(45, 46)
    point2 = Coordinates(35.67, 23.00000009)

    distance = point1.get_distance_from(point2)

    print(distance)