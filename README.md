

# 🚲 Bike Sharing Demand Prediction

This project predicts the **bike rental count** based on historical data and various features such as season, weather, temperature, humidity, and more. It uses **machine learning models** to provide accurate predictions for both **daily** and **hourly** datasets.

---

## 📌 **Project Overview**

Bike-sharing systems generate a large amount of data, which can be used to predict demand. This project focuses on:
✅ Predicting bike demand for **day** and **hour** datasets
✅ Building and training **machine learning models**
✅ Deploying the solution using **Flask** for an interactive web interface

---

## 🛠️ **Tech Stack**

* **Python**
* **Flask** (for web app)
* **Pandas**, **NumPy** (data processing)
* **Matplotlib**, **Seaborn** (visualization)
* **Scikit-learn** (ML models)

---

## 📂 **Project Structure**

```
├── app.py                # Flask app for prediction
├── bike_prediction.py    # ML model and prediction logic
├── day.csv               # Daily bike sharing dataset
├── hour.csv              # Hourly bike sharing dataset
├── README.md             # Project documentation
```

---

## 🔍 **Dataset Details**

* **Day Dataset (day.csv)**
  Contains daily bike rental data with features like season, weather, temperature, etc.
* **Hour Dataset (hour.csv)**
  Contains hourly rental data for more granular predictions.

---

## ⚙️ **How to Run**

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/IBM-Edunet-2.git
   cd IBM-Edunet-2
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. **Open in browser**

   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 **Features**

✔ Predicts bike rental count based on user input
✔ Handles both **daily** and **hourly** datasets
✔ Simple and interactive **Flask web interface**

---

## 📊 **Machine Learning Approach**

* **Preprocessing:** Handling missing values, encoding categorical variables
* **Model:** Linear Regression, Decision Tree, Random Forest (choose the best)
* **Evaluation:** R² Score, RMSE

---

## 📷 **Sample Output**

*(Add screenshot of the web app here)*

---

## 📜 **License**

This project is licensed under the **Apache 2.0 License**.

---

### ✍ **Author**

Developed as part of the **IBM-Edunet Internship Program**.
