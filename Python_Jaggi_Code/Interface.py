from abc import ABC, abstractmethod

# Interface method
class Game(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def winner(self):
        pass


def main():
    obj = BGMI()

    obj.play()


if __name__ == "__main__":
    main()