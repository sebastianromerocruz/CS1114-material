import turtle

side_length = 100
gap_constant = 3
inner_angle = 90

# Draw a third of the first side
turtle.forward(side_length / gap_constant)

# Skip over the second third
turtle.penup()
turtle.forward(side_length / gap_constant)

# Draw the last third of the side, and turn left 90 degrees
turtle.pendown()
turtle.forward(side_length / gap_constant)
turtle.left(inner_angle)

# Draw the next three sides in the same fashion, turning 90 degrees at each edge
turtle.forward(side_length / gap_constant)
turtle.penup()
turtle.forward(side_length / gap_constant)
turtle.pendown()
turtle.forward(side_length / gap_constant)
turtle.left(inner_angle)

turtle.forward(side_length / gap_constant)
turtle.penup()
turtle.forward(side_length / gap_constant)
turtle.pendown()
turtle.forward(side_length / gap_constant)
turtle.left(inner_angle)

turtle.forward(side_length / gap_constant)
turtle.penup()
turtle.forward(side_length / gap_constant)
turtle.pendown()
turtle.forward(side_length / gap_constant)
turtle.left(inner_angle)
