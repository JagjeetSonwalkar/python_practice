# Clear all elements from a list.

def clearX(getList):
    lastRange = len(getList)

    for i in range(lastRange):
        getList.pop()


def main():
    myList = [10, 2 ,9,7, 2, 1, 10, 4, 100, 5, 1, 7, 7]

    print(myList)
    clearX(myList)
    print(myList)


if __name__ == "__main__":
    main()