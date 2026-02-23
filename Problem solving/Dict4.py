#  Sort Dictionary by Keys
# Input 1 → {'b':2,'a':1} → Output 1 → {'a':1,'b':2}
# Input 2 → {2:'x',1:'y'} → Output 2 → {1:'y',2:'x'}

# Sort Dictionary by Values
# Input 1 → {'a':2,'b':1} → Output 1 → {'b':1,'a':2}
# Input 2 → {1:'z',2:'x'} → Output 2 → {2:'x',1:'z'}

#  Nested Dictionary Access
# Input 1 → {'a':{'x':10}}, access a->x → Output 1 → 10
# Input 2 → {1:{'y':5}}, access 1->y → Output 2 → 5

# Flatten Nested Dictionary
# Input 1 → {'a':{'x':10}} → Output 1 → {'a.x':10}
# Input 2 → {1:{'y':5}} → Output 2 → {1.y':5}

# Remove Keys with None Values
# Input 1 → {'a':None,'b':2} → Output 1 → {'b':2}
# Input 2 → {1:None,2:3} → Output 2 → {2:3}

def sortByKeys(dictx):
    keySortList = list(dictx.keys())
    keySortList.sort()
    resultDict = {}

    for i in keySortList:
        resultDict.update({i:dictx[i]})
    return resultDict

def sortByvalue(dictx):
    sort_items = sorted(dictx.items(), key=lambda item: item[1])
    sort_dict = dict(sort_items)

    return sort_dict
        
def nestedDict(dictt):
    for key, value in dictt.items():
        if isinstance(value, dict):
            print(f"nested key --> {key}")
            nestedDict(value)
        else:
            print(f"{key} : {value}")

def nested_dict_access(dict_x, match_key):
    result = None

    for k, v in dict_x.items():
        if k == match_key and k is not isinstance(v, dict):
            return v
        
        if isinstance(v, dict):
            result = nested_dict_access(v, match_key)
            if result is not None:
                return result
                
def get_flattem_dict(dict_x):
    result_dict = {}

    for key, value in dict_x.items():
        if isinstance(value, dict):
            result = {}
            result = get_flattem_dict(value)

            if result is not None:
                for n_key, n_value in result.items():
                    newKey = key + '.' + n_key 
                    result_dict.update({newKey : n_value})
        else:
            result_dict.update({key : value})
    
    return result_dict

def remove_none_value(dict_x):
    result_dict = {}
    
    for key, value in dict_x.items():
        if isinstance(value, dict):
            cleaned = remove_none_value(value)
            if cleaned:
                result_dict[key] = cleaned
        elif value is not None:     
            result_dict[key] = value
    return result_dict

def main():
    Ret = None
    value = None
    dict = {'b':2,'f':9, 'a':1, 'e':9, 'c':3, 'd':1}

    # Ret = sortByKeys(dict)
    # print(f"The orginal dict {dict} & sorted dict by keys {Ret}")

    # Ret = sortByvalue(dict)
    # print(f"The orginal dict {dict} & sorted dict by values {Ret}")

    informartiondict = {
        "name": "Virat",
        "info":
        {
            "eduction":
            {
                "degree":"B.Tech",
                "year":2025,
                "active_back_log":None
            },
            "city":"Pune",
            "skills":["python", "java", "mysql"]
        },
        "active" : True,
        "marriage" : None
    }
    
    # nestedDict(informartiondict)

    # print("Enter the netsed key's to access the value: ")
    # value = input()
    # Ret = nested_dict_access(informartiondict, value)
    # print(f"{value} : {Ret}")

    # Ret = get_flattem_dict(informartiondict)
    # print(Ret)

    Ret = remove_none_value(informartiondict)
    print(Ret)


if __name__ == "__main__":
    main()