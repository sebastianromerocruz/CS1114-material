import arpeggiator

# Don't worry about about how any of this works—just treat it as any other module
ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

# WRITE YOUR CODE BELOW...
END_CODE = "DONE"
MIN_PLAY_TIMES = 0

# STEP 1: Asking the user for notes
user_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

while user_note != END_CODE:
    ARPEGGIATOR.add_note(user_note)
    user_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

print(ARPEGGIATOR)

# STEP 2: Asking the user for arpeg. direction
user_direction = input("\nEnter an arpeggiator direction [U/D] ")

while user_direction != 'U' and user_direction != 'D':
    user_direction = input("Enter an arpeggiator direction [U/D] ")

# STEP 3: Asking the user for how many times arpeg. will be played
user_play_times = int(input("\nHow many times do you want your arpeggiator to play? "))

while user_play_times <= MIN_PLAY_TIMES:
    user_play_times = int(input("How many times do you want your arpeggiator to play? (Must be positive amount) "))

# STEP 5: Playing the arpeggiator
print()  # for nice formatting
for time in range(user_play_times):
    if user_direction == 'U':
        ARPEGGIATOR.play(UP)
    else:
        ARPEGGIATOR.play(DOWN)
