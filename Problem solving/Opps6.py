# Implement Simple Inheritance

class Vehicle:
    all_vechicle = []

    def __init__(self, model, colour):
        self.model = model
        self.colour = colour 

        Vehicle.all_vechicle.append(self)

    def display(self):
        print(f"model: {self.model} & colour: {self.colour}")

    @classmethod
    def display_all(cls):
        for vehicle_name in cls.all_vechicle:
            vehicle_name.display()


class Car(Vehicle):
    def __init__(self, vehicle_type, model, colour):
        super().__init__(model, colour)
        self.vehicle_type = vehicle_type

    def display(self):
        print(f"Vechicle type: {self.vehicle_type}, model: {self.model} ,colour: {self.colour}")

def main():
    v1 = Vehicle("350 GT", "yellow")
    v2 = Vehicle("Benz Patent-Motorwagen", "white")
    v3 = Vehicle("Type 10", "white-black")

    lambo = Car("car", "350 GT", "yellow")
    lambo.display()

    Vehicle.display_all()

    



if __name__ == "__main__":
    main()