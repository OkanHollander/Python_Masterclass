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
        album_name (str): name of the album
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
        self.album_name = name
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
