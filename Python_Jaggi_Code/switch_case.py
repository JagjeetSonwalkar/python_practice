# def day_of_weak(day):
#     if day == 1:
#         return "sunday"
#     elif day == 2:
#         return "monday"
#     elif day == 3:
#         return "tuesday"
#     elif day == 4:
#         return "wednesday"
#     elif day == 5:
#         return "thursday"
#     elif day == 6:
#         return "friday"
#     elif day == 7:
#         return "saturday"
#     else:
#         return "Not a valid day!"
from unittest import case


def day_of_weak(day):
    match day:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "tuesday"
        case 4:
            return "wednesday"
        case 5:
            return "thursday"
        case 6:
            return "friday"
        case 7:
            return "saturday"
        case _:
            return "Not a valid day!"

def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return True
        case _:
            return False

def main():
    print(day_of_weak(2))
    print(day_of_weak(3))

    print(is_weekend("sunday"))

if __name__ == "__main__":
    main()