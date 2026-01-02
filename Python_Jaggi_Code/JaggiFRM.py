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