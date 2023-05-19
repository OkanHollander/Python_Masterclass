class Song:
    """Class to represent a song
    Attributes:
        title (str): title of the song
        artist (Artist): artist of the song
        duration (int): duration of the song
    """

    def __init__(self, title, artist, duration=0):
        """Initializes a song object
        Args:
            title (str): title of the song
            artist (Artist): artist of the song
            duration (int): duration of the song
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using it's track list
    Attributes:
        name (str): name of the album
        year (int): year of the album
        artist (Artist): artist of the album
            If not specified, the artist will default to an artist with the name "Various artist
        tracks (list[Song]): list of songs in the album
    Methods:
        add_song: adds a song to the album"""

    def __init__(self, name, year, artist=None):
        """Initializes an album object
        Args:
            name (str): name of the album
            year (int): year of the album
            artist (Artist): artist of the album
                If not specified, the artist will default to an artist with the name "Various artist
        """
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the album
        Args:
            song (Song): song to add
            position (int): position to add the song
            If not specified, the song will be added to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Class to represent an artist
    Attributes:
        name (str): name of the artist
        albums (list[Album]): list of albums of the artist

    Methods:
        add_album: adds an album to the artist"""

    def __init__(self, name):
        """Initializes an artist object
        Args:
            name (str): name of the artist
        """
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Adds an album to the artist
        Args:
            album (Album): album to add
                if album is present it will not be added
        """
        if album not in self.albums:
            self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, albums_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)
            print(f"{artist_field} : {albums_field} : {year_field} : {song_field}")

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(albums_field, year_field, new_artist)
            elif new_album.name != albums_field:
                # we've just read details for a new album
                new_artist.add_album(new_album)
                new_album = Album(albums_field, year_field, new_artist)

            # create a new song object and add it to the current albums's collection
            new_song = Song(song_field, new_artist, year_field)
            new_album.add_song(new_song)
        # After reading the last line of the text file, we have an artist and album that havn't been store,
        # process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


def create_checkfile(artist_list):
    """Creates a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    checkfile.write(
                        f"{artist.name}\t{album.name}\t{album.year}\t{song.title}\n"
                    )


if __name__ == "__main__":
    artist = load_data()
    print(f"There are {len(artist)} artists")
    create_checkfile(artist)
