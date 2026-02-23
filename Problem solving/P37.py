# 	Sort dict by keys.
# 	Sort dict by values

if __name__ == "__main__":
    mydict = {1:"Rohit",2:"Virat",4:45,5:18,0:666}
    print("Orignal dict:",mydict)

    sortedKeys = dict(sorted(mydict.items()))
    print("sort dict by keys: ",sortedKeys)
