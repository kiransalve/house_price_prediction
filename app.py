import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# load data
def load_data():
    return pd.read_csv("housing.csv")

df = load_data()

# remove ouliers
def remove_outliers_iqr(df):
    cleaned_df = df.copy()
    for col in cleaned_df.columns:
        Q1 = cleaned_df[col].quantile(0.25)
        Q3 = cleaned_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        cleaned_df = cleaned_df[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]
    return cleaned_df

df_clean = remove_outliers_iqr(df)

# Train model
def train_model():
    X = df.drop(columns=["MEDV"])
    y = df["MEDV"]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Metrics
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)
    return model, rmse, r2, y, y_pred, X.columns

model, rmse, r2, y_actual, y_pred, feature_names = train_model()


# ---------------- UI ----------------
st.header("📊 Predict House Prices")
st.write("**Developed by: Kiran Salve**")
st.write("**Portfolio** : [Portfolio-Kiran Salve](https://kiran-salve-portfolio.vercel.app/)")

st.write("""A simple and interactive Streamlit web application to predict house prices using Linear Regression.
""")

# Prediction UI
st.subheader("Find Best Price for House")
rm = st.number_input("Average number of rooms per house", min_value=0.0)
lstat = st.number_input("Percentage of lower-status population", min_value=0.0)
ptratio = st.number_input("Pupil–teacher ratio in schools", min_value=0.0)

if st.button("Predict"):
    new_data = np.array([[rm, lstat, ptratio]])
    predicted_price = model.predict(new_data)[0]
    st.success(f"✅ Predicted Price: ₹{round(predicted_price, 2)}")

st.subheader("Model Performance")
st.write(f"Model : Linear Regression")
st.write(f"- **RMSE:** {rmse:.2f}")
st.write(f"- **R² Score:** {r2:.2f}")

st.write(f"""
**RMSE (Root Mean Squared Error) = {rmse:.2f}**  
On average, our predictions are off by about **{rmse:.2f} units** of our target variable.  

**R² Score = {r2:.2f}**  
This means our model explains **{r2*100:.0f}% of the variance** in the target variable.  
The closer to 1, the better — so **{r2:.2f}** indicates the model fits the data very well.
""")

# Coefficients
st.subheader("📋 Model Coefficients")
coeff_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": model.coef_
})
st.write(coeff_df)
st.write(f"**Intercept:** {model.intercept_:.2f}")


# Plot Actual vs Predicted
st.subheader("📉 Actual vs Predicted Sales")
fig, ax = plt.subplots()
ax.scatter(y_actual, y_pred, color="blue", alpha=0.6, label="Predicted vs Actual")
ax.plot([y_actual.min(), y_actual.max()],
        [y_actual.min(), y_actual.max()],
        color="red", linestyle="--", label="Best Fit Line")
ax.set_xlabel("Actual Sales")
ax.set_ylabel("Predicted Sales")
ax.set_title("Actual vs Predicted Sales")
ax.legend()
st.pyplot(fig)
