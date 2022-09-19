'''
input_number_systems
S. Romero Cruz
CS 1114
Spring 2022
'''

# Most basic user input and output
user_input = input()
print(user_input)

# User input and output with a prompt and more details
user_input = input("What is this class's course number? ")
print(user_input)

# What I would ideally do
user_input = input("What is this class's course number? ")
course_number = int(user_input)
print("The user entered course number " + str(course_number))
