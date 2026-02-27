class Song:
    note = "A class type to represent a Song"
    version = 1.0

    def __init__(self, name="", artist="", album="", released_year=2000):
        self.name = name
        self.artist = artist
        self.album = album
        self.released_year = released_year

    def info(self):
        print(f"Song: {self.name} by {self.artist}")
        print(f"Album: {self.album}")
        print(f"Released Year: {self.released_year}")


songs = [
    Song(
        name="The Ytse Jam",
        artist="Dream Theater",
        album="When Dream and Day Unite",
        released_year=2004
    ),
    Song(
        name="Always with Me, Always with You",
        artist="Joe Satriani",
        album="Surfing with the Alien",
        released_year=1987
    ),
]

print(f"Class: Song, version: {Song.version}, note: {Song.note}")

print(f"type of songs: {type(songs).__name__}")

for s in songs:
    s.info()
    print()
