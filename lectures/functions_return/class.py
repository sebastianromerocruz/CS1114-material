import math


def get_cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    print(volume)


number = 5
sine = math.sin(number)


volume_of_can = get_cylinder_volume(2, 4)
print(volume_of_can)
