# Multiple Inheritance Example

class Engine:
    def __init__(self, engine_model_name):
        self.engine_model_name = engine_model_name
    
    def engine_sound(self):
        return " Growl..."

class Number_plate:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

class Vehicle(Engine, Number_plate):
    def __init__(self, top_speed, vehicle_colour, vehicle_type, engine_model_name, vehicle_number):
        Engine.__init__(self, engine_model_name)
        Number_plate.__init__(self, vehicle_number)

        self.vehicle_type = vehicle_type
        self.vehicle_colour = vehicle_colour
        self.top_speed = top_speed

    def display(self):
        print(f"Vechical type: {self.vehicle_type}")
        print(f"Engine: {self.engine_model_name}")
        print(f"number plate: {self.vehicle_number}")
        print(f"colour: {self.vehicle_colour}")
        print(f"topspeed: {self.top_speed}")
        print("-" * 40)

def main():
    lamboo_vehicle = Vehicle(450, "red", "car", "Miura", 1)
    bugatti_vehicle = Vehicle(444, "white", "car", "The 8.0L Quad-Turbocharged W16", 111)

    lamboo_vehicle.display()
    bugatti_vehicle.display()
    
if __name__ == "__main__":
    main()