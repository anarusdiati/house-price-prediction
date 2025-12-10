**<h1>House Price Prediction using Linear Regression</h1>**
<br>
A Machine Learning project to predict house prices based on features such as size (sqft) and number of bedrooms.
<br><br>
<h2>Overview</h2>
<br>
This project builds a simple yet effective Linear Regression model to predict housing prices.<br>
The dataset contains 100 housing records with realistic price patterns and added noise to better simulate real-world conditions.
<br><br>
This model demonstrates:<br>
- A positive relationship between size and price<br>
- A positive relationship between bedrooms and price<br>
- Very low error (MSE) due to a clean and well-structured dataset<br><br>

<h2>Project Structure</h2>
house-price-prediction/<br>
│── data.csv<br>
│── house_price_prediction.ipynb<br>
│── main.py<br>
│── README.md<br>
│── requirements.txt<br><br>

<h2>Model Used</h2>
Linear Regression from scikit-learn:<br>
- Easy to interpret<br>
- Suitable for linear relationships<br>
- Accurate when used with clean datasets<br><br>

<h2>Performance</h2>
The model produces an error value:<br>
- MSE : 696484870.6547278 <br>
- RMSE: 26390.999803999995 <br><br>
The smaller the MSE, the more accurate the model’s predictions are compared to the actual data.

<h2>Example Prediction</h2>
Predicted price for a 2,500 sqft house with 4 bedrooms: 478101.2769438156
