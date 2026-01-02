
from sklearn import tree

def main():
    # rough = 0, smooth = 1
    ball_feature = [[35,0], [47,0], [90,1], [48, 0], [90, 1], [35, 0], [92, 1], [35, 0], [35, 0], [35, 0]]

    ball_name = ["tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket",  "tennis", "tennis", "tennis"]

    obj = tree.DecisionTreeClassifier()

    #--------------------------------
    # fit method is used for training
    #--------------------------------
    obj.fit(ball_feature, ball_name)

    #------------------------------------------
    #  predict method is used to test the model
    #------------------------------------------
    # print(obj.predict([93, "smooth"]))
    print(obj.predict([93, 1]))

if __name__ == '__main__':
    main()