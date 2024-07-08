class Human():
    def __init__(self, age, weight, height, race, address):
        self._age = age
        self.weight = weight
        self.height = height
        self.race = race
        self.address = address

def information_me(self):
        return "Name: " + self.name + " Family: " + self.family + " My Address: " + self.address + " My Age: " + str(
            self.age)