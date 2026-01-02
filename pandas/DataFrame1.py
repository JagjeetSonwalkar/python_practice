# Data Frame

import pandas as pd

def main():
    data = {
        "name" : ["rohit", "virat", "hardik"],
        "age" : [45, 18, 44]
    }

    data_frame = pd.DataFrame(data, index = ["player 1", "player 2", "player 3"])

    print("Data Frame: ")
    print(data_frame)

    # display rohit
    print("\n",data_frame.iloc[0])

    # add new coloum
    data_frame["pos"] = [1, 3, 5]

    print("\nData frame after adding new cloumn: ")
    print(data_frame)

    # add new row
    # new_row = pd.DataFrame([{"name":"Bumhra", "age":32, "pos":8}])

    print("\nAdd new row: ")
    new_row = pd.DataFrame([{"name":"Bumhra", "age":32, "pos":8}], index=["player 4"])
    data_frame = pd.concat([data_frame, new_row])

    print(data_frame)

    # add multipal rows
    print("\nAdding 2 new rows")

    new_rows = pd.DataFrame([{"name":"sky", "age":35, "pos":3},
                            {"name":"ROKO", "age":50, "pos":12}],
                            index = ["player 5", "player 6"])
    data_frame = pd.concat([data_frame, new_rows])
    print(data_frame)
    # --------------- end of main ----------------------#
if __name__ == "__main__":
    main()