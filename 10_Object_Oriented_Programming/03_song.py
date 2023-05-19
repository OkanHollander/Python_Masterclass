class Song():
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


