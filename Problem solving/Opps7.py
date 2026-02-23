# Override Method in Subclass

class Vehicle:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour 
    
    def vehicle_sound(self):
        return "Genric vehicle sound"

class Car(Vehicle):
    def __init__(self, vehicle_type, model, colour):
        super().__init__(model, colour)
        self.vehicle_type = vehicle_type

    def vehicle_sound(self):
        return "Vroom vroom"


def main():
    vehicle_sound = ""

    v1 = Vehicle("350 GT", "yellow")
    v2 = Vehicle("Benz Patent-Motorwagen", "white")
    v3 = Vehicle("Type 10", "white-black")

    lambo = Car("car", "350 GT", "yellow")

    vehicle_sound = v2.vehicle_sound()
    print(f"vehicle sound '{vehicle_sound}'")

    vehicle_sound = lambo.vehicle_sound()
    print(f"lambo car sound '{vehicle_sound}'")

    



if __name__ == "__main__":
    main()