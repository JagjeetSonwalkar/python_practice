from abc import ABC, abstractmethod

# Basic abstract class
class Game(ABC):
    @abstractmethod
    def play(self):
        pass

# Abstract class with concrete method
class Vechicle(ABC):

    @abstractmethod
    def car(self):
        pass

    def sound(self):
        print("Bhum Bhum")

class BGMI(Game):
    def time(self):
        print("1111")

    def play(self):
        print("play bgmi")

def main():
    obj = BGMI()

    obj.play()


if __name__ == "__main__":
    main()