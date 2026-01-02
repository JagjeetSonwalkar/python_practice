from functools import reduce

Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16];

print("Input Data: ",Data);

FData = list(filter(lambda x : (x%2 == 0), Data));
print("Filter data: ",FData);

MData = list(map(lambda x : (x+1), FData));
print("Map data: ",MData);

RData = reduce(lambda a,b : (a+b), MData);
print("Reduce data: ",RData);