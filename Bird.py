from abc import ABC

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    #abstractmethod
    def eat(self):
        pass

    extinct = False           
