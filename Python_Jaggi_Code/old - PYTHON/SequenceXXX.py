def calculateRadius(rad , PI = 3.14):
    result = PI * rad * rad
    return result

def main():
    print("Enter radius of circle: ")
    radius = float(input())

    Area = calculateRadius(radius)

    print("Area of circle: ",Area)

if __name__ == "__main__":
    main()