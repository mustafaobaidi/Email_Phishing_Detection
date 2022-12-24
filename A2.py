import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import tree
from sklearn import metrics


def evaluate_F1score(prediction, labels):
    return metrics.f1_score(labels,prediction)

def evaluate_Recall(prediction, labels):
    return metrics.recall_score(labels,prediction)

def evaluate_Precision(prediction, labels):
    return metrics.precision_score(labels,prediction)

def SVC_model(data,test_size):
    #split the data
    train_data, test_data = train_test_split(data, test_size = test_size, random_state=99)
    #assign the train x and y

    train_Y = train_data['Phishing'].values
    train_X = train_data.drop('Phishing', axis=1)

    #assign the test x and y
    test_Y = test_data['Phishing'].values
    test_X = test_data.drop('Phishing', axis=1)

    model = svm.SVC()
    model.fit(train_X,train_Y)
    prediction = model.predict(test_X)
    print('SVM')
    print("Precision:", evaluate_Precision(test_Y, prediction))
    print("F1-Score:", evaluate_F1score(test_Y, prediction))
    print("Recall:", evaluate_Recall(test_Y, prediction))
    print('*************************************************')

def Logistic_Regression_model(data, test_size):
    #split the data
    train_data, test_data = train_test_split(data, test_size = test_size, random_state=99)
    #assign the train x and y

    train_Y = train_data['Phishing'].values
    train_X = train_data.drop('Phishing', axis=1)

    #assign the test x and y
    test_Y = test_data['Phishing'].values
    test_X = test_data.drop('Phishing', axis=1)
    clf = LogisticRegression(random_state=0).fit(train_X, train_Y)
    # print("Logistic Regression Accuracy: {}".format(clf.score(test_X,test_Y)))
    prediction = clf.predict(test_X)
    print('Logistic Regression')
    print("Precision:", evaluate_Precision(test_Y, prediction))
    print("F1-Score:", evaluate_F1score(test_Y, prediction))
    print("Recall:", evaluate_Recall(test_Y, prediction))
    print('*************************************************')

def Decision_Tree_model(data,test_size):
    #split the data
    train_data, test_data = train_test_split(data, test_size = test_size, random_state=99)
    #assign the train x and y

    train_Y = train_data['Phishing'].values
    train_X = train_data.drop('Phishing', axis=1)

    #assign the test x and y
    test_Y = test_data['Phishing'].values
    test_X = test_data.drop('Phishing', axis=1)
    clf2 = tree.DecisionTreeClassifier(random_state=0, max_depth=2)
    clf2 = clf2.fit(train_X, train_Y)
    # print("Decision Tree Accuracy: {}".format(clf2.score(test_X,test_Y)))
    prediction = clf2.predict(test_X)
    print('Decision Tree')
    print("Precision:", evaluate_Precision(test_Y, prediction))
    print("F1-Score:", evaluate_F1score(test_Y, prediction))
    print("Recall:", evaluate_Recall(test_Y, prediction))
    print('*************************************************')

def main():

    # read the csv
    df2 = pd.read_csv('../dataset/dataset_T2.csv') 
    df3 = df2.sample(frac=1).reset_index(drop=True)

    test_size = 0.10

    for i in range(3):
        print('__________________________________________________________________________________')
        print('testing the models with a test size of: ' + "{:.2f}".format(test_size*100) +'%')
        print('__________________________________________________________________________________')
        SVC_model(df3,test_size)
        Decision_Tree_model(df3,test_size)
        Logistic_Regression_model(df3,test_size)
        test_size = test_size + 0.10

if __name__ == "__main__":
    main()