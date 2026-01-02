PI = 3.14

def calculateRadius(rad):
    result = PI * rad * rad
    return result

def main():
    print("Enter radius of circle: ")
    radius = float(input())

    Area = calculateRadius(radius)

    print("Area of circle: ",Area)

if __name__ == "__main__":
    main()