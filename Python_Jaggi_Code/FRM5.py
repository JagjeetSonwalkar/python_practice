def increase(a):
    return a+1;

def Demo(Task, Values):
    newList = [];

    for no in Values:
        # print(Task(no));
        lData = Task(no);
        newList.append(lData);
    return newList

Data = [13,17,10,14,11];

new_dataList = list(Demo(increase, Data));

print(new_dataList);