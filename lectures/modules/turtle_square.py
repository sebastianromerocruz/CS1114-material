import random
import turtle

# Generating a random side-length using the random module
inner_angle = 90
lower_limit = 25
upper_limit = 100
random_side_length = random.randrange(lower_limit, upper_limit)

# Draw the first side and turn 90 degrees
turtle.forward(random_side_length)
turtle.left(inner_angle)

# Draw the next three sides, turning 90 degrees at each edge
turtle.forward(random_side_length)
turtle.left(inner_angle)

turtle.forward(random_side_length)
turtle.left(inner_angle)

turtle.forward(random_side_length)
turtle.left(inner_angle)
