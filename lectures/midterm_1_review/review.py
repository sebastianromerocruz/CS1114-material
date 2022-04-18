import arpeggiator

# Don't worry about about how any of this works—just treat it as any other module
ARPEGGIATOR = arpeggiator.Arpeggiator()
# ARPEGGIATOR.play() and .add_note() are already defined
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

# WRITE YOUR CODE BELOW
# STEP 1: Ask for notes
user_note = input("Enter a note: ")

while user_note != "DONE":
    ARPEGGIATOR.add_note(user_note)
    user_note = input("Enter a note: ")

# STEP 2: Direction
user_direction = input("Up or down? [U/D] ")

while user_direction != 'U' and user_direction != 'D':
    user_direction = input("Up or down? [U/D] ")

# STEP 3: Times
user_times = int(input("How many times? "))

while user_times <= 0:
    user_times = int(input("How many times? "))

# STEP 4: Play
for time in range(user_times):
    if user_direction == 'U':
        ARPEGGIATOR.play(UP)
    else:
        ARPEGGIATOR.play(DOWN)

