import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Read the first line: F (number of features) and N (number of training samples)
F, N = map(int, input().split())

# Read the training data (features + price per square foot)
train_data = [list(map(float, input().split())) for _ in range(N)]
X_train = np.array([row[:-1] for row in train_data])  # Extract feature columns
y_train = np.array([row[-1] for row in train_data])   # Extract price column

# Read the number of test cases
T = int(input())

# Read the test data (only features, price is missing)
X_test = np.array([list(map(float, input().split())) for _ in range(T)])

# Create polynomial features (degree 3, since the polynomial order is < 4)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)  # Transform training data
X_test_poly = poly.transform(X_test)        # Transform test data

# Train a linear regression model on the polynomial features
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict the missing prices
y_pred = model.predict(X_test_poly)

# Print the predicted prices (rounded to 2 decimal places)
for price in y_pred:
    print(round(price, 2))
