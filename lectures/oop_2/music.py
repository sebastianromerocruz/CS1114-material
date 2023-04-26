class Song:
    def __init__(self, song_title, artist, album, genre, length_in_seconds):
        self.song_title = song_title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length_in_seconds = length_in_seconds
        self.play_count = 0

    def play(self, rotations=1):
        self.play_count += rotations



if __name__ == '__main__':
    title = "Purple"
    artist = "Lil Wayne"
    album = "Jeff"
    genre = "Hip-hop"
    length = 123

    new_song = Song(title, artist, album, genre, length)

    print(new_song.song_title)
    print(new_song.artist)
    print(new_song.album)
    print(new_song.genre)
    print(new_song.length_in_seconds)
    print(new_song.play_count)

    # num_of_plays = 10
    # for time in range(num_of_plays):
    #     new_song.play(10)
    #
    # print(new_song.play_count)

    new_song.play()
    print(new_song.play_count)