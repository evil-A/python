class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool):
        if not isinstance(first_name, str):
            print("ERROR: name is not a string")
            return None
        if not isinstance(is_alive, bool):
            print("ERROR: alive: true or false")
            return None
        try:
            self.first_name = str(first_name)
            self.is_alive = bool(True)
        except:
            raise TypeError

class Greyjoy(GotCharacter):
    """A class representing the Greyjoy family. Or when rulers of the sea fall into badlands."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name = first_name, is_alive = is_alive)
        self.family_name = "Greyjoy"
        self.house_words = "We do not sow"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self): 
        self.is_alive = False
