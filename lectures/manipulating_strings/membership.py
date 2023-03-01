# METHOD 1
# USING FOR-LOOP SEQUENCING
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

for letter in second_string:
    if letter in first_string:
        print(letter)


# METHOD 2
# USING FOR-LOOP INDEXING
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)

for index in range(second_string_length):
    letter = second_string[index]
    if letter in first_string:
        print(letter)


# METHOD 3
# USING WHILE-LOOP INDEXING
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)
index = 0

while index < second_string_length:
    letter = second_string[index]
    if letter in first_string:
        print(letter)

    index += 1
