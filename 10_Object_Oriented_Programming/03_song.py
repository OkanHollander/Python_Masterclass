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
        if self.artist is not None:
            self.artist = artist
        else:
            self.artist = Artist("Various artist")
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
            print(artist_field, albums_field, year_field, song_field)

if __name__ == "__main__":
    load_data()