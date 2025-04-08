# 🔥 Algerian Forest Fires Prediction App

This project is a simple machine learning web application built using **Flask** that predicts forest fire occurrence based on environmental conditions. The Ridge Regression model is trained on the **Algerian Forest Fires Dataset**.

---

## 🚀 Features

- Clean and minimalistic web interface
- Accepts user input for 9 parameters:
  - Temperature
  - Relative Humidity (RH)
  - Wind Speed (WS)
  - Rain
  - FFMC (Fine Fuel Moisture Code)
  - DMC (Duff Moisture Code)
  - ISI (Initial Spread Index)
  - Classes (Fire / No Fire)
  - Region (Bejaia / Sidi-Bel Abbes)
- Predicts forest fire intensity using a trained Ridge Regression model
- Deployed locally via Flask

---

## 🛠 Tech Stack

- Python
- Flask
- HTML/CSS
- Scikit-learn
- NumPy
- Pandas

---

## 🗂 Project Structure
test_forest_fires/
│
├── app.py                    # Main Flask application
├── requirements.txt          # List of all dependencies
├── README.md                 # Project documentation
│
├── models/                   # Folder for model files
│   ├── ridge_reg.pkl         # Trained Ridge Regression model
│   └── scaler.pkl            # StandardScaler for input normalization
│
├── templates/                # HTML templates for rendering UI
│   ├── index.html            # Landing page
│   └── home.html             # Main form + prediction output
