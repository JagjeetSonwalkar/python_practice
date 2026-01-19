'''
Problem: Predict student marks
Features: Study hours, attendance
Label: Final marks
Algorithm: Linear Regression
Metric: MSE
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def main():
    # <-- collect the data -->
    raw_data = {
    'StudyHours': [1, 2, 3, 4, 5, None, 7, 8, 9, 10],
    'Attendance': [60, 65, 70, None, 80, 85, 90, 92, 95, 98],
    'Marks': [35, 40, 45, 50, None, 65, 70, 75, 85, 90]
    }

    df = pd.DataFrame(raw_data)
    print(df)

    # <-- clean & preprocess Data -->
    df.fillna(df.mean(), inplace = True)
    print(df)

    # <-- Separate Features and Label -->
    x = df[['StudyHours', 'Attendance']]
    y = df['Marks']

    # <-- Feature Scaling -->
    scaler = StandardScaler()
    x_scaler = scaler.fit_transform(x)

    # <-- Choose an Algorithm --> Output is numeric → Regression & Simple relationship → Linear Regression
    model = LinearRegression()

    # <-- Split Data -->
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaler, y, test_size=0.3, random_state=42
    )

    # <-- Model Training -->
    model.fit(x_train, y_train)

    # <-- Evaluate Performance -->
    # Make Predictions
    y_pred = model.predict(x_test)

    # Calculate MSE
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean_squard_error: {mse}")

    # Tune Parameters
    model_tuned = LinearRegression(fit_intercept=True)
    model_tuned.fit(x_train, y_train)

    y_pred_tuned = model_tuned.predict(x_test)
    mse_tuned = mean_squared_error(y_test, y_pred_tuned)

    print("Tuned Model MSE:", mse_tuned)

    # Deploy the Model: Model is ready to predict on new, unseen data
    new_student = np.array([[6, 88]])  # 6 hours study, 88% attendance
    new_student_scaled = scaler.transform(new_student)

    predicted_marks = model.predict(new_student_scaled)
    print("Predicted Marks:", predicted_marks[0])


if __name__ == "__main__":
    main()