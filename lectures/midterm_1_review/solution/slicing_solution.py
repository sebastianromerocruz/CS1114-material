"""
Author: Sebastián Romero Cruz
CS-UY 1114
Fall 2022
"""
encoded_message = input("Enter an encoded string: ")
key = int(input("Enter a key: "))

decoded_message = ""

for char in encoded_message:
    if not char.isdigit():
        decoded_message += char

start = -1              # the negative-first index is the last index of a sequence
step = -1 * (key + 1)   # this step is the same

decoded_message = decoded_message[start::step]

print(f"Your message is '{decoded_message}'")