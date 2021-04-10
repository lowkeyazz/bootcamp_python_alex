import sys


class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        if type(first_name) != str or first_name == "":
            sys.exit("ERROR Type str required for first name")
        self.first_name = first_name
        if type(is_alive) != bool:
            sys.exit("ERROR Type bool required for is_alive")
        self.is_alive = is_alive


'''Class house Stark Ps John Snow is not a stark or a bastard'''


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        return self.house_words

    def die(self):
        if self.is_alive == False:
            print('Already dead')
        self.is_alive = False


'''Class house Targaryen Ps John Snow is a targaryen'''


class Targaryen(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and blood"

    def print_house_words(self):
        return self.house_words

    def die(self):
        if self.is_alive == False:
            print('Already dead')
        self.is_alive = False
