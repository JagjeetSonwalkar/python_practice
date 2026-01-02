# create the constant varibale

class Const:

    @property
    def PI(self):
        return 3.14

def main():
    # PI_value = 3.16
    # PI_value += 1     # it work, means PI is not a constant varible
    # print(PI_value)

    PI_value = float()

    constant_object = Const()
    PI_value = constant_object.PI

    print(PI_value)

if __name__ == "__main__":
    main()