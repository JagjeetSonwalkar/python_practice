CheckEven = lambda No : (No%2 == 0)
Increase = lambda No: No+1
Sum = lambda A,B : A+B

def filterX(Task, getValue):
    Result = [];

    for no in getValue:
        Ret = Task(no);
        if(Ret == True):
            Result.append(no);
    return Result;

def MapX(Task, getValue):
    Result = [];

    for no in getValue:
        Ret = Task(no);
        Result.append(Ret);
    return Result;

def ReduceX(Task, getValue):
    Result = 0;

    for no in getValue:
        Result = Task(Result, no);
    return Result;


Data = [7,10,15,12,4,6,9,8,12,16]
print("Input data : ",Data)

Fdata = list(filterX(CheckEven, Data));
print("Filter data: ",Fdata);

Mdata = list(MapX(Increase, Fdata));
print("Map data: ",Mdata);

Rdata = ReduceX(Sum, Mdata);
print("Reduce data: ",Rdata);