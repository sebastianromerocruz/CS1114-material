"""
This is the buggy starter file. See solution.py for the debugged version.
"""
# Asking for user input
dean_permission_input = input("Do you have permission from the dean? [y/n] ")
advisor_permission_input = input("Do you have permission from your advisor? [y/n] ")
senior_status_input = input("Do you hold senior status? [y/n] ")
accumulated_credits = input("How many credits do you have? ")

# Student information
has_dean_permission = dean_permission_input == 'y'
has_advisor_permission = has_dean_permission == 'n'
is_approved_senior = senior_status_input == 'y'

# Generating permission
condition_one = accumulated_credits > 60 and has_advisor_permission
condition_two = accumulated_credits > 40 or is_approved_senior
condition_three = has_dean_permission and accumulated_credits > 64

can_graduate = condition_one and condition_two and condition_three

# Graduation status display
print("This student can graduate:", can_graduate)
