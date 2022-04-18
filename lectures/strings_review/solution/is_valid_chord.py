ROOTS = "A B C D E F G"
TYPES = "♮ ♭ ♯"  # Natural, flat, and sharp
COLOURS = "maj m 7 m7 6 m6 dim sus4 dim 7♭13 ♯9 7♭9"
INVALID_NOTES = "B♯ C♭ F♭ E♯"
SPACE_CHAR = ' '
END_CODE = "DONE"

is_user_not_done = True

while is_user_not_done:
    user_chord = input("Enter a chord: [ROOT TYPE COLOUR] ")

    if user_chord == END_CODE:
        is_user_not_done = False  # this is another way of ending your loop.
        continue  # continue will basically skip to the next loop iteration, ignoring the rest of the code in the loop

    first_space_index = user_chord.find(SPACE_CHAR)
    second_space_index = user_chord.find(SPACE_CHAR, first_space_index + 1)

    root = user_chord[:first_space_index]
    chord_type = user_chord[first_space_index + 1:second_space_index]
    colour = user_chord[second_space_index + 1:]

    is_valid_root = root in ROOTS
    is_valid_type = chord_type in TYPES
    is_valid_colour = colour in COLOURS
    is_valid_note = root + chord_type not in INVALID_NOTES

    if is_valid_root and is_valid_type and is_valid_colour and is_valid_note:
        print("{}{}{} is a valid chord!".format(root, chord_type, colour))
    else:
        print("{}{}{} is not a valid chord!".format(root, chord_type, colour))
