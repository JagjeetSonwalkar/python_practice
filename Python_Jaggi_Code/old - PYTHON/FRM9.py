CheckEven = lambda No : (No%2 == 0)
Increase = lambda No: No+1
Sum = lambda A,B : A+B

from JaggiFRM import filterX, MapX, ReduceX

def main():
    # Data = [7,10,15,12,4,6,9,8,12,16]
    # print("Input data : ",Data)
    Data = [];
    
    print("Enter the size of list: ");
    size = int(input());

    print("Enter the data in numberic format: ");
    for i in range(size):
        value = int(input());
        Data.append(value);

    Fdata = list(filterX(CheckEven, Data));
    print("Filter data: ",Fdata);

    Mdata = list(MapX(Increase, Fdata));
    print("Map data: ",Mdata);

    Rdata = ReduceX(Sum, Mdata);
    print("Reduce data: ",Rdata);

if __name__ == "__main__":
    main();