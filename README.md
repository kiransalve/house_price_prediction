# 🏠 Streamlit House Price Prediction App

A **Streamlit web application** that uses **Linear Regression** to predict house prices.  
The app can train on the **California Housing dataset** or your own uploaded CSV file,  
and provides an interactive interface to select features, visualize predictions, and test custom inputs.

---

## 📌 Features
- 📂 **Dataset Options**  
  - Use the built-in **California Housing dataset**  
  - Upload your own CSV file

- ⚙ **Feature Selection**  
  - Select features for training  
  - Option to standardize data  
  - Add polynomial features for non-linear relationships

- 📊 **Model Training**  
  - Trains a **Linear Regression** model  
  - Displays **Intercept** and **Slopes** (coefficients)  
  - Shows evaluation metrics:
    - **RMSE** (Root Mean Squared Error)  
    - **R² Score**  

- 📈 **Visualizations**  
  - Actual vs Predicted scatter plot  
  - Residual plot

- 🔮 **Prediction Tool**  
  - Enter manual feature values to get predictions instantly  
  - Download model coefficients as CSV

---

## 🚀 Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/streamlit-house-price-app.git
   cd streamlit-house-price-app
