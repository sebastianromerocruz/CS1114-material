# Constants
LOWER_CREDIT_LIMIT = 40
UPPER_CREDIT_LIMIT = 64

dean_permission_input = input("Do you have permission from the dean? [y/n] ")

if dean_permission_input == 'y':
    print("This student can graduate because they have the dean's permissions.")
else:
    advisor_permission_input = input("Do you have permission from your advisor? [y/n] ")
    senior_status_input = input("Do you hold senior status? [y/n] ")
    accumulated_credits = float(input("How many credits do you have? "))

    if accumulated_credits >= LOWER_CREDIT_LIMIT and advisor_permission_input == 'y':
        print("This student can graduate because they have their advisor's permission and have the necessary credits.")
    elif accumulated_credits >= UPPER_CREDIT_LIMIT and senior_status_input == 'y':
        print("This student can graduate because they are an approved senior and have the necessary credits.")
    else:
        print("This student cannot graduate.")