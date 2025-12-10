**<h1>House Price Prediction using Linear Regression</h1>**
<br>
A Machine Learning project to predict house prices based on features such as size (sqft) and number of bedrooms.
<br><br>
<h2>Overview</h2>
<br>
This project builds a simple yet effective Linear Regression model to predict housing prices.<br>
Dataset berisi 100 data rumah dengan pola harga yang realistis dan sedikit noise agar mendekati kondisi data dunia nyata.
<br><br>
Model ini menunjukkan:<br>
- Hubungan positif antara size & price<br>
- Hubungan positif antara bedrooms & price<br>
- Error (MSE) yang sangat rendah karena data bersih dan well-structured<br><br>

<h2>Project Structure</h2>
house-price-prediction/<br>
│── data.csv<br>
│── house_price_prediction.ipynb<br>
│── main.py<br>
│── README.md<br>
│── requirements.txt<br><br>

<h2>Model Used</h2>
Linear Regression dari scikit-learn:<br>
- Mudah diinterpretasikan<br>
- Cocok untuk hubungan linear<br>
- Akurat untuk dataset bersih<br><br>

<h2>Performance</h2>
Model menghasilkan nilai error:<br>
- MSE : 696484870.6547278 <br>
- RMSE: 26390.999803999995 <br><br>
Semakin kecil nilai MSE, semakin akurat prediksi model dibanding data asli.

<h2>Contoh Prediksi</h2>
Prediksi harga rumah 2500 sqft, 4 kamar: 478101.2769438156
