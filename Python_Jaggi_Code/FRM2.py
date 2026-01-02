from functools import reduce

checkEven = lambda x : x%2 == 0;

increase = lambda x : x+1 ;

add = lambda a, b : a+b ;

Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16];

print("Input Data: ",Data);

FData = list(filter(checkEven, Data));
print("Filter data: ",FData);

MData = list(map(increase, FData));
print("Map data: ",MData);

RData = reduce(add, MData);
print("Reduce data: ",RData);