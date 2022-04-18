def extract_data(filepath):
    games_list = []

    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return games_list

    file.readline()  # to get rid of header

    for line in file:
        line = line.strip().replace('"', '').split(',')
        name = line[1]
        platform = line[2]
        year = line[3]
        genre = line[4]
        publisher = line[5]
        developer = line[15]

        datum = [name, platform, year, genre, publisher, developer]
        games_list.append(datum)

    file.close()
    return games_list

