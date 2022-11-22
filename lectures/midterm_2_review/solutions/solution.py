CAST_SAMPLE = [{"id": 11111, "name": "Léa Seydoux"}, {"id": 11112, "name": "Adrien Brody"}]
MOVIES = {
    "The French Dispatch": {
        "genre": "Anthology / Comedy", 
        "cast": ["Owen Wilson", "Benicio del Toro", "Léa Seydoux", "Adrien Brody", "Frances McDormand", "Timothée Chalamet", "Lyna Khoudri", "Jeffrey Wright", "Stephen Park", "Bill Murray"] 
    },
    "The Grand Budapest Hotel": {
        "genre": "Comedy / Drama",
        "cast": ["Ralph Fiennes", "Tony Revolori", "Adrien Brody", "Willem Dafoe", "Saoirse Ronan", "Léa Seydoux"]
    },
    'Moonrise Kingdom': {
        "genre": "Coming of Age / Comedy / Drama",
        "cast": ["Jared Gilman", "Kara Hayward", "Bruce Willis", "Edward Norton", "Bill Murray"]
    },
    "The Royal Tenenbaums": {
        "genre": "Comedy / Drama",
        "cast": ["Gene Hackman", "Anjelica Huston", "Danny Glover", "Ben Stiller", "Luke Wilson", "Gwyneth Paltrow", "Bill Murray"]
    }
}


def get_costarred(cast_sample, movies):
	# STEP 1: Since the problem is asking us to return a list of movie titles, let's initialise an empty list
    costarred_movies = []

	# STEP 2: Iterate through all the movies using the items() view
    for movie_info in movies.keys():

		# STEP 3: Isolate the movie title and the info dictionary
        movie_title, info = movie_info

        is_costarred = True

		# STEP 4: Iterate through the cast sample
        for cast_member in cast_sample:

			# STEP 4: We want to keep a movie title if all cast members in the sample were in it
            if cast_member['name'] not in info['cast']:
                is_costarred = False

        if is_costarred:
            costarred_movies.append(movie_title)
    
    return costarred_movies


def main():
    print(get_costarred(CAST_SAMPLE, MOVIES))


main()
