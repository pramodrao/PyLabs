""" Object creation test """


class PartyAnimal:
    """ Party Animal class """
    parties_hosted = 0
    name = ""

    def __init__(self, name):
        """ Constructor """
        print("Constructor Called")
        self.name = name

    def party(self):
        """ Host a party """
        self.parties_hosted = self.parties_hosted + 1
        print("So far", self.name, "has hosted", self.parties_hosted, "parties")

    def __del__(self):
        """ Destructor """
        print("No more parties for", self.name)


class FootballFan(PartyAnimal):
    """ FootballFan """
    games_played = 0

    def play_next_game(self):
        self.games_played = self.games_played + 1
        print("Total games played by", self.name, "is", self.games_played)


def main():
    """ Main class """
    jake = PartyAnimal("Jake")
    jake.party()
    nancy = FootballFan("Nancy")
    jake.party()
    nancy.play_next_game()
    nancy.party()
    jake.party()


main()
