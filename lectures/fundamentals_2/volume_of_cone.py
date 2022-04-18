'''
Lecture fundamentals_2
S. Romero Cruz
CS 1114
Spring 2022
'''

# Defining our variables for volume of a cone
pi = 3.1456
base_radius = 7
height = 4.5

# Not really necessary here, but splitting an expression into parts often helps
# us debug easier
constants = pi / 3
print("Constants:")
print(constants)

radius_component = base_radius * base_radius
print("Radius Component:")
print(radius_component)

height_component = height
print("Height Component:")
print(height_component)

# Calculation
volume = constants * radius_component * height_component

# Output
print(volume)