from math import pi

def get_cylinder_volume(radius=0.0, height=0.0, data_filepath=None):
    if data_filepath:
        # Open your file
        file = open(data_filepath, 'r')

        # header
        file.readline()
        
        # radius
        radius = file.readline()
        radius = radius.strip()
        comma_loc = radius.find(',')
        radius = float(radius[comma_loc + 1:])  

        # height
        height = file.readline()
        height = height.strip()
        comma_loc = height.find(',')
        height = float(height[comma_loc + 1:])  

        file.close()

        area_of_base = pi * radius ** 2
        volume = area_of_base * height

        return volume
    else:
        area_of_base = pi * radius ** 2
        volume = area_of_base * height

        return volume


def main():
    volume = get_cylinder_volume(radius=3, height=4)
    print(volume)

    volume = get_cylinder_volume(4, 1)
    print(volume)

    volume = get_cylinder_volume(data_filepath="data.csv")
    print(volume)


main()
