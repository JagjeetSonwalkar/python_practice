
from sklearn import tree

def main():
    ball_feature = [[35,"rough"], [47,"rough"], [90,"smooth"], [48, "rough"], [90, "smooth"], [35, "rough"], [92, "smooth"], [35, "rough"], [35, "rough"], [35, "rough"]]

    ball_name = ["tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket",  "tennis", "tennis", "tennis"]

    obj = tree.DecisionTreeClassifier()

    #--------------------------------
    # fit method is used for training
    #--------------------------------
    obj.fit(ball_feature, ball_name)

    #------------------------------------------
    #  predict method is used to test the model
    #------------------------------------------
    print(obj.predict([93, "smooth"]))

if __name__ == '__main__':
    main()