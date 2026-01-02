def increase(a):
    return a+1;

def Demo(Task, Values):
    for no in Values:
        print(Task(no));

Data = [13,17,10,14,11];

Demo(increase, Data);