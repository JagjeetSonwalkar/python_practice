#  Find Key with Maximum Value in Nested Dictionary
# Input 1 → {'a':{'x':10,'y':5}} → Output 1 → 'x'
# Input 2 → {'b':{'p':3,'q':7}} → Output 2 → 'q'


def tarvel(data):
    new_dict = {}

    for key, value in data.items():
        if isinstance(value, dict):
            nestedDict = tarvel(value)
            if nestedDict is not None:
                for nested_key, nested_value in nestedDict.items():
                    new_dict.update({nested_key:nested_value})
        else:
            new_dict.update({key:value})
    return new_dict

def find_max(data_dict_x):
    data_dict = tarvel(data_dict_x)

    max = list(data_dict.values())[0]
    max_keys = []

    for value in data_dict.values():
        if value != None:
            if value > max:
                max = value
    for k, v in data_dict.items():
        if v == max:
            max_keys.append(k)
    return max_keys
    
def main():
    ## variables
    Ret = None
    date_dict = {}
    ##########################

    date_dict = {
        "current_year": 2025,
        "dates":
        {
            "DOB":
            {
                "date":25,
                "month":10,
                "year":2003
                
            },
            "marrage":None,
            "break_up": 0
        },
        "up_comming_year" : 2026,
        "next_month" : 12
    }

    Ret = find_max(date_dict)
    print(Ret)
    

if __name__ == "__main__":
    main()