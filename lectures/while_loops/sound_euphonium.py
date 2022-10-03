user_input = int(input("Please enter any integer: "))

if user_input % 3 == 0:
    print("Sound!")
elif user_input % 5 == 0:
    print("Euphonium")
elif user_input % 3 == 0 and user_input % 5 == 0:
    print("Sound! Euphonium")