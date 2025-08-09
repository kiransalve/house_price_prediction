# 🏠 Streamlit House Price Prediction App

A **Streamlit web application** that uses **Linear Regression** to predict house prices.
---

## 📌 Features
- 📂 **Dataset**  
  - Used boston house price dataset
  - that has four columns -

    | Column      | Meaning                                                         | Why it matters for price prediction                                                        |
| ----------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **RM**      | Average number of rooms per house                            | More rooms usually mean larger houses, which often have higher prices.                     |
| **LSTAT**   | Percentage of lower-status population                           | Higher % often correlates with lower house prices.                                         |
| **PTRATIO** | Pupil–teacher ratio in schools for the town                     | Lower ratios (smaller classes) are often linked with better schools → higher house prices. |
| **MEDV**    | Median value of owner-occupied homes (in \$1000’s) -Target | This is what we want to predict.                                                           |


- ⚙ **Outlier Removal**  
  - When outlier removed model's accuracy increased to from 69% to 72% also RMSE reduced from 82K to 62K

- 📊 **Model Training**  
  - Trains a **Linear Regression** model  
  - **Intercept (β₀):** `547146.1653322706`

| Feature  | Slope (β)       |
|----------|-----------------|
| RM       | 55164.033894    |
| LSTAT    | -11535.492244   |
| PTRATIO  | -16542.866348   |
  - Shows evaluation metrics:
    - **RMSE** (Root Mean Squared Error)  -  62461.55
    - **R² Score**   71.97%

- 📈 **Visualizations**

- Finding Outlier using Boxplot

<img width="1800" height="1200" alt="LSTAT_boxplot" src="https://github.com/user-attachments/assets/28c1ab6d-6d4b-40b0-8abc-ac293f054c68" />

<img width="1800" height="1200" alt="PTRATIO_boxplot" src="https://github.com/user-attachments/assets/74d000f3-c3b7-43c2-af34-c13c599cc765" />

<img width="1800" height="1200" alt="MEDV_boxplot" src="https://github.com/user-attachments/assets/546e7d7f-6d27-456a-b8dc-a467a94888a2" />

<img width="1800" height="1200" alt="RM_boxplot" src="https://github.com/user-attachments/assets/407e2f32-0592-43ed-a2f7-6ec596c71350" />

- Visualizing Distribution

<img width="1800" height="1200" alt="LSTAT_histplot" src="https://github.com/user-attachments/assets/7e86c5e3-9a6c-4e05-8159-7e1a8f1d5066" />

<img width="1800" height="1200" alt="PTRATIO_histplot" src="https://github.com/user-attachments/assets/91659cee-7456-495b-8fe3-465989f50eea" />

<img width="1800" height="1200" alt="PTRATIO_histplot" src="https://github.com/user-attachments/assets/9ab1bfa3-9233-4adf-880e-3cc331de3caf" />

<img width="1800" height="1200" alt="RM_histplot" src="https://github.com/user-attachments/assets/2907000d-0624-449d-97aa-685e78308ced" />

- Scatter plot

  -LSTAT
<img width="1800" height="1200" alt="LSTAT_scatter" src="https://github.com/user-attachments/assets/d3fdfbbf-c1a1-47d4-b02f-cfcd6f608f40" />

  -PTRATIO
<img width="1800" height="1200" alt="PTRATIO_scatter" src="https://github.com/user-attachments/assets/bf16d784-4664-4e66-91cc-a3f4586079c9" />
 
  -RM
<img width="1800" height="1200" alt="RM_scatter" src="https://github.com/user-attachments/assets/6e317599-6c03-4bfe-a262-82b182f06887" />

- Actual vs Predicted scatter plot  

<img width="1920" height="1440" alt="Actual_vs_predicted" src="https://github.com/user-attachments/assets/ecb3108d-2423-4d5d-a119-f3423f4dedfb" />

<img width="4500" height="900" alt="Actualvspredicted" src="https://github.com/user-attachments/assets/adacc4c4-0f6a-4df1-81eb-402c4e4b908e" />

- Residual plot

<img width="3600" height="900" alt="error" src="https://github.com/user-attachments/assets/7cdcfb64-f383-4b46-8838-0ef9cdf191f3" />


