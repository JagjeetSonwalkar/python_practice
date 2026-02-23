# Abstraction: Abstract Class with Abstract Method

from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is started...")

def main():
    bugatti = Car()
    bugatti.start()

if __name__ == "__main__":
    main()