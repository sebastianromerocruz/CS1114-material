VALUE_LIMIT = 5000
END_CODE = "-1"
NON_ALPHA_CHAR = ' '

word_input = input("Enter a word to measure, or " + END_CODE + " to stop: ")
value = 0

while value <= VALUE_LIMIT and word_input != END_CODE:
    word_value = 0

    for character in word_input:
        if character != NON_ALPHA_CHAR:
            word_value += ord(character)

    value += word_value
    print("The value of the word(s) '" + word_input + "' is " + str(word_value) + ".")
    print("Current total value:", value)

    word_input = input("\nEnter a word or words to measure, or " + END_CODE + " to stop: ")

print("\nThe final value is", value)