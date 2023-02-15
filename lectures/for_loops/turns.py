turns = int(input("How many times do you want the for-loop to execute? "))

"""
For every value that our loop variable current_turn takes from a range of numbers of 0 to turns, execute the line 
print("Turn number", current_turn).
"""
for current_turn in range(turns):
    print("Turn number", current_turn)


"""
The while-loop equivalent to the for-loop above would be:
"""
# turns = int(input("How many times do you want the while-loop to execute? "))
#
# current_turn = 1
#
# while current_turn <= turns:
#     print("Turn number", current_turn)
#     current_turn += 1
