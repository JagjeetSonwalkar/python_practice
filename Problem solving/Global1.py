
X_VALUE = 10

def main():
    x = 100

    global X_VALUE 

    X_VALUE += 1
    x += 1

    print("Global -->",X_VALUE)
    print("Local-->",x)

if __name__ == "__main__":
    main()