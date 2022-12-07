class Point:
    def __init__(self, x_coord=0.0, y_coord=0.0, z_coord=0.0):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

    def __str__(self):
        return f"({self.x_coord}, {self.y_coord}, {self.z_coord})"

    def __sub__(self, other):
        return Point(self.x_coord - other.x_coord,
                     self.y_coord - other.y_coord,
                     self.z_coord - other.z_coord)


def main():
    point_a = Point(-2, -3, 0)

    print(point_a.x_coord)
    print(point_a.y_coord)
    print(point_a.z_coord)

    print(point_a)

    point_a = Point(3.0, -0.67, -6)
    point_b = Point(34.0, -5.67, -6.06)
    print(point_b - point_a)


if __name__ == '__main__':
    main()
