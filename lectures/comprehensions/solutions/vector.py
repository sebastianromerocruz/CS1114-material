from point import Point
from math import sqrt
from random import randrange

PLUS_SIGN, MINUS_SIGN = '+', '-'

class Vector:
    def __init__(self, origin=Point(), end_point=Point()):
        self.vector = end_point - origin

    def get_magnitude(self):
        return sqrt(self.vector.x_coord ** 2 + self.vector.y_coord ** 2 + self.vector.z_coord ** 2)

    def __mul__(self, other):
        return Vector(Point(), Point(self.vector.x_coord * other.vector.x_coord,
                                     self.vector.y_coord * other.vector.y_coord,
                                     self.vector.z_coord * other.vector.z_coord,))

    def __str__(self):
        x_component = self.vector.x_coord        
        y_component = self.vector.y_coord if self.vector.y_coord >= 0 else abs(self.vector.y_coord)
        z_component = self.vector.z_coord if self.vector.z_coord >= 0 else abs(self.vector.z_coord)

        first_sign  = PLUS_SIGN if self.vector.y_coord >= 0 else MINUS_SIGN
        second_sign = PLUS_SIGN if self.vector.z_coord >= 0 else MINUS_SIGN

        return f"{x_component}x {first_sign} {y_component}y {second_sign} {z_component}z"


def main():
    point_a  = Point(randrange(-10, 10), randrange(-10, 10), randrange(-10, 10))
    point_b  = Point(randrange(-10, 10), randrange(-10, 10), randrange(-10, 10))
    vector_a = Vector(point_b, point_a)

    point_c  = Point(randrange(-10, 10), randrange(-10, 10), randrange(-10, 10))
    point_d  = Point(randrange(-10, 10), randrange(-10, 10), randrange(-10, 10))
    vector_b = Vector(point_d, point_c)

    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")

    dot_product = vector_a * vector_b

    print("A · B = {}".format(dot_product))
    print("|A · B| = {}".format(dot_product.get_magnitude()))


main()
