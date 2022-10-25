import math

SPHERE_VOL_CONSTANT = math.pi * 4 / 3


def print_volume_of_sphere(radius):
    volume = SPHERE_VOL_CONSTANT * radius ** 3
    print("The volume of this spherical object is {}.".format(volume))


earth_radius = 6378  # in km; approx.
print_volume_of_sphere(earth_radius)

polaris_radius = 37.5  # in in Solar radii; approx.
print_volume_of_sphere(polaris_radius)
