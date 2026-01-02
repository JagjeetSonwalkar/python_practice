
from sklearn import tree

def main():
    # rough = 0, smooth = 1
    ball_feature = [[35,0], [47,0], [90,1], [48, 0], [90, 1], [35, 0], [92, 1], [35, 0], [35, 0], [35, 0]]

    # tennis = 1, cricket = 2
    ball_name = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    obj = tree.DecisionTreeClassifier()

    #--------------------------------
    # fit method is used for training
    #--------------------------------
    obj.fit(ball_feature, ball_name)

    #------------------------------------------
    #  predict method is used to test the model
    #------------------------------------------
    # print(obj.predict([93, "smooth"]))
    print(obj.predict([[93, 1]]))
    print(obj.predict([[93, 1], [95, 1], [42, 0], [42, 0]]))

if __name__ == '__main__':
    main()