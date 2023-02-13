AGE_LIMIT = 17

movie_rating = input("What is this movie's rating? ")
user_age = int(input("How old are you? "))


if user_age >= AGE_LIMIT:
    # If the user is old enough to watch any movie, then the program just ends here
    print("ALLOWED.")
else:
    # If the user isn't old enough to watch R-rated movies, then we only really care if the movie IS R-rated
    if movie_rating == 'r' or movie_rating == 'R':
        # Check if the user is chaperoned
        has_chaperone = input("Are you accompanied by someone? [y/n] ")

        if has_chaperone != 'y' and has_chaperone != 'Y':
            # If they are not, they are automatically not allowed
            print("NOT ALLOWED.")
        else:
            # If they are, check for the chaperone's age
            chaperone_age = int(input("How old is your chaperone? [y/n] "))
            
            if chaperone_age >= AGE_LIMIT:
                print("ALLOWED.")
            else:
                print("NOT ALLOWED.")
    else:
        # If the movie isn't even R-rated, we're done right away
        print("ALLOWED.")