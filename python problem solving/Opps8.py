# Use super() to Call Parent Method
class Vehicle:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour 
    
    def v_car_sound(self):
        return "Vroom-vroom"

    def v_bike_sound(self):
        return " boom-boom"

class Car(Vehicle):
    def __init__(self, vehicle_type, model, colour):
        super().__init__(model, colour)
        self.vehicle_type = vehicle_type

    def car_sound(self):
        sound = super().v_car_sound()
        return "car sound:"+sound

def main():
    vehicle_sound = ""

    v1 = Vehicle("350 GT", "yellow")
    v2 = Vehicle("Benz Patent-Motorwagen", "white")
    v3 = Vehicle("Type 10", "white-black")

    lambo = Car("car", "350 GT", "yellow")

    vehicle_sound = lambo.car_sound()
    print(vehicle_sound)

if __name__ == "__main__":
    main()