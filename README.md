<div align="center">

# 🚗 Used Car Price Predictor  
### *ML–Powered Web Application*

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-Web_App-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple?style=for-the-badge&logo=bootstrap)

💡 **Predict the resale value of a used car using Machine Learning — instantly, accurately, and interactively.**

</div>

---

## 📌 Project Overview

The **Used Car Price Predictor** is an end-to-end **Machine Learning + Web Application** designed to estimate the resale price of a car based on multiple real-world parameters such as brand, year, mileage, engine specifications, fuel type, ownership, and more.

The project goes beyond model training — it demonstrates:
- Real-world **data preprocessing**
- **Model comparison & selection**
- Seamless **ML model deployment**
- A clean and user-friendly **web interface**

---

## ✨ Key Features

✔️ Interactive Web Interface built with **HTML + Bootstrap**  
✔️ Handles both **numerical and categorical inputs**  
✔️ Robust preprocessing using **One-Hot Encoding**  
✔️ Multiple ML models trained & evaluated  
✔️ **Best-performing model deployed** for real-time predictions  
✔️ Clean, scalable, and beginner-friendly code structure  

---

## 🖼️ Demo Screenshots

<div align="center">

### 📊 Prediction Results

![alt text](sampleScreenshots/Screenshot%20(1686).png)

![alt text](sampleScreenshots/Screenshot%20(1687).png)

*Real-time classification results with model comparison*

</div>

---

## 🧠 Machine Learning Workflow

### 🔹 Data Preprocessing
- Removed inconsistencies & missing values
- Encoded categorical features using **OneHotEncoder**
- Feature scaling where necessary
- Split dataset into training and testing sets

### 🔹 Models Trained
The following models were trained and evaluated in the Jupyter Notebook:

| Model | Purpose |
|-----|-----|
| 🌲 Random Forest Regressor | Baseline ensemble model |
| 🚀 Gradient Boosting Regressor | High-performance boosting model |

---

## 🏆 Model Selection – Why Gradient Boosting?

After evaluating both models on accuracy and generalization performance:

✅ **Gradient Boosting Regressor outperformed Random Forest**  
- Lower prediction error  
- Better handling of complex feature interactions  
- More stable predictions on unseen data  

📌 **Final Decision:**  
➡️ **Gradient Boosting** was selected as the production model and integrated into the Flask web application.

---

## 🌐 Web Application Highlights

🖥️ **User-Friendly UI**
- Dropdowns for categorical features
- Radio buttons for binary choices
- Validated numerical inputs

⚙️ **Backend**
- Flask handles form submission
- Inputs transformed using the same pipeline as training
- Model predicts price in real-time

📊 **Output**
- Clean and instant price prediction
- Displayed dynamically on the same page

---
