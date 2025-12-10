import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Pisahkan fitur & label
X = data[["size", "bedrooms"]]
y = data["price"]

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)

# 6. Evaluasi
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print("MSE :", mse)
print("RMSE:", rmse)

# 7. Visualisasi hasil
plt.figure(figsize=(8, 5))
plt.scatter(data["size"], data["price"], label="Data Points")
plt.plot(data["size"], model.predict(data[["size", "bedrooms"]]), label="Model Prediction")
plt.xlabel("Size")
plt.ylabel("Price")
plt.title("House Price Prediction")
plt.legend()
plt.grid(True)
plt.show()

example = model.predict([[2500, 4]])
print("\nPrediksi harga rumah 2500 sqft, 4 kamar:", example[0])