# LOAN APPROVAL

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def get_df(data):
    df = pd.DataFrame(data)
    return df

def data_clean(df):
    num_col = ["Income","CreditScore","LoanAmount"]
    df[num_col] = df[num_col].fillna(df[num_col].median())

    df["EmploymentStatus"].fillna(df['EmploymentStatus'].mode()[0], inplace=True)

    for col in ["Income", "LoanAmount"]:
        upper_limit = df[col].quantile(0.95)
        df[col] = np.where(df[col] > upper_limit, upper_limit, df[col])

    # Encode Categorical Data
    df = pd.get_dummies(df, columns=["EmploymentStatus"], drop_first=True)

    # Encode Target Variable
    df["Approved"] = df["Approved"].map({"Yes":1, "No":0})

    return df

def main():
    raw_data = {
    'Income': [25000, 40000, None, 30000, 80000, 50000, 20000, 900000, 45000, None],
    'CreditScore': [650, None, 750, 600, 800, 720, 580, 820, None, 770],
    'LoanAmount': [200000, 250000, 300000, None, 350000, 270000, 150000, 4000000, 230000, 320000],
    'EmploymentStatus': ['Employed', 'Employed', 'Self-Employed', 'Unemployed','Employed', None, 'Unemployed', 
                            'Employed', 'Employed', 'Self-Employed'],
    'Approved': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }

    df = get_df(raw_data)
    print(df)

    df = data_clean(df)
    print(df)

    # feature - label
    x = df.drop("Approved", axis=1)
    y = df["Approved"]

    # train & test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Feature Scaling
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Train Logistic Regression Model
    model = LogisticRegression(max_iter = 1000)
    model.fit(x_train_scaled, y_train)

    # model evaluation
    y_pred = model.predict(x_test_scaled)

    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))

    new_applicant = np.array([[55000, 710, 260000, 1, 0]])
    new_applicant_scaled = scaler.transform(new_applicant)

    prediction = model.predict(new_applicant_scaled)
    probability = model.predict_proba(new_applicant_scaled)

    print("Loan Approved:", "YES" if prediction[0] == 1 else "NO")
    print("Approval Probability:", probability[0][1])

if __name__ == "__main__":
    main()