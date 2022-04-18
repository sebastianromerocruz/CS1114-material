# Constants
lower_credit_limit = 40
upper_credit_limit = 64

# Asking for user input
dean_permission_input = input("Do you have permission from the dean? [y/n] ")
advisor_permission_input = input("Do you have permission from your advisor? [y/n] ")
senior_status_input = input("Do you hold senior status? [y/n] ")
accumulated_credits = float(input("How many credits do you have? "))

# Student information
has_dean_permission = dean_permission_input == 'y'
has_advisor_permission = has_dean_permission == 'y'
is_approved_senior = senior_status_input == 'y'

# Generating permission
condition_one = accumulated_credits >= upper_credit_limit and is_approved_senior
condition_two = accumulated_credits >= lower_credit_limit and has_advisor_permission

can_graduate = has_dean_permission or condition_one or condition_two

# Graduation status display
print("This student can graduate:", can_graduate)