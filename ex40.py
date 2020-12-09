
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy bday to you", "I do not want to get sued", "So i will stop right here"])
bulls_parade = Song(["Happy bday to you", "I do not want to get sued", "So i will stop right here"])

happy_bday.sing_me_a_song()
bulls_parade.sing_me_a_song()
