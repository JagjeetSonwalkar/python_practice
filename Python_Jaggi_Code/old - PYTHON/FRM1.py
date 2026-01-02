from functools import reduce

def checkEven(no):
    return (no%2 == 0);

def increase(no):
    return (no+1);

def sum(A, B):
    return (A+B);


Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16];

print("Input Data: ",Data);

Fdata = list(filter(checkEven, Data));
print("Filter data: ",Fdata);

Mdata = list(map(increase, Fdata));
print("Map data: ",Mdata);

Rdata = reduce(sum, Mdata);
print("Reduce data: ",Rdata);