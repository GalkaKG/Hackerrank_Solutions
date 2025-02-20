import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split())

train_data = [list(map(float, input().split())) for _ in range(N)]
X_train = np.array([row[:-1] for row in train_data])  
y_train = np.array([row[-1] for row in train_data])   

T = int(input())
X_test = np.array([list(map(float, input().split())) for _ in range(T)])

poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)

for price in y_pred:
    print(round(price, 2))  
