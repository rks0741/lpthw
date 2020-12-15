
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy bday to you", "I do not want to get sued", "So i will stop right here"])
bulls_parade = Song(["They rally around tha family", "With pockets full of shells"])

katusha = Song(["Vihodila na bereg katusha", "Na visokii beereg na krutoi", "Tam h3 chto dalshe"])
katusha_lyrics = ["Vihodila na bereg katusha2", "Na visokii beereg na krutoi2", "Tam h3 chto dalshe2"]


happy_bday.sing_me_a_song()
bulls_parade.sing_me_a_song()

katusha.sing_me_a_song()

katusha_l = Song(katusha_lyrics)

katusha_l.sing_me_a_song()
