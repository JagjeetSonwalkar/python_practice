#  Polymorphism: Same Method Name Different Classes

class Animal:
    def dog(self):
        return "bhu bhu"

    def cat(self):
        return "meow meow"

class Pet(Animal):
    def dog(self):
        return "bhu bhu"

    def fat(self):
        return "No no"

def main():
    ret = 0

    dog_sound = Animal()
    ret = dog_sound.fat()
    print(ret)

if __name__ == "__main__":
    main()