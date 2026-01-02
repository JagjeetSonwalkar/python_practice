from turtle import Shape


class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} & {"filled" if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"The circle has a radius of {self.radius} cm")
        super().describe()
def main():
    circle_obj = Circle("red", True, 3.5)

    circle_obj.describe()

if __name__ == '__main__':
    main()