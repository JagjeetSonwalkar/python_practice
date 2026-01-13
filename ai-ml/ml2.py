from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Sample labeled data: (features, price)
# Features could be [square_footage, number_of_bedrooms]
data = [
    ([1500, 3], 300000),
    ([2000, 4], 450000),
    ([1200, 2], 250000),
    ([1800, 3], 380000),
    ([2500, 5], 550000),
]

# Separate features and target variable
X = np.array([item[0] for item in data]) # Features (e.g., square footage, bedrooms)
y = np.array([item[1] for item in data]) # Target (price)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Example of predicting a new house price
new_house_features = [[1600, 3]] # 1600 sq ft, 3 bedrooms
predicted_price = model.predict(new_house_features)
print(f"Predicted price for a {new_house_features[0][0]} sq ft, {new_house_features[0][1]} bedroom house: ${predicted_price[0]:,.2f}")

'''
In this snippet:
X represents the features of houses (square footage, number of bedrooms), and y is the corresponding price.
LinearRegression is a common algorithm for regression tasks.
model.fit() trains the model to find the best-fitting line (or hyperplane in higher dimensions).
model.predict() estimates the price for new house features.
mean_squared_error and r2_score are common metrics to evaluate regression models.
'''