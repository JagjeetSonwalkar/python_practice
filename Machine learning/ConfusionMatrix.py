from sklearn.metrics import confusion_matrix

def main():
    actual = [1,0,1,1,0,1,0,1,1,0]
    predicted = [1,0,1,0,0,1,1,1,1,1]

    con_mat = confusion_matrix(actual, predicted)

    print("Confusion Matrix is: ")
    print(con_mat)

'''
TN      FP
FN      TP

[2 2]
[1 5]

Accuracy = (TN + TP) / (TN + FP + FN + TP)
'''
# -------------- end of main ------------ #

if __name__ == '__main__':
    main()