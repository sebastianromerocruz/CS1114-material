"""
Author: Sebastián Romero Cruz
CS-UY 1114
Fall 2022
"""
encoded_message = input("Enter an encoded string: ")
key = int(input("Enter a key: "))

decoded_message = ""

start = len(encoded_message) - 1  # we're going backwards, so we start at the last index
end = -1                          # we end at 0, but we subtract 1 because the end is non-inclusive
step = -1 * (key + 1)             # in order to skip key-number of characters, we add 1 to the key

for index in range(start, end, step):
    character = encoded_message[index]

    # we also ignore digits
    if not character.isdigit():
        decoded_message += character

print(f"Your message is '{decoded_message}'")