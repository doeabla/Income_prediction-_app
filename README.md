# Income Prediction Project

This project aims to predict income levels based on various demographic features using machine learning. The predictive model is built using CatBoost, Decision Tree, and Logistic Regression algorithms. The best-performing model, Decision Tree, achieved an accuracy of 97%.

![income_prediction](https://github.com/doeabla/Income_prediction_app/assets/137217264/58793d76-b0c1-4af9-95db-cb1c6c4d1412)


## Table of Contents
- [Introduction](#introduction)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Introduction

The growing disparity in income distribution poses a significant challenge, especially in developing nations. Traditional methods of monitoring income levels between census years are costly and may lack accuracy. This project addresses this issue by employing machine learning to predict income levels, offering a more efficient and precise alternative for policymakers.

## Exploratory Data Analysis (EDA)

- EDA was performed to understand the distribution of income across various demographic features.
- Visualizations were created to analyze the relationships between age, gender, education, work class, marital status, race, etc., with income levels.

## Modeling

Three machine learning models were used for predicting income levels:

1. **CatBoost**
2. **Decision Tree**
3. **Logistic Regression**

The Decision Tree model outperformed others, achieving an accuracy of 97%.

## Evaluation

The evaluation metrics for the Decision Tree model include accuracy, precision, recall, and F1-score. Detailed information about the model's performance can be found in the respective sections of the project.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/244891dc-c899-425d-97b9-d5f5e36bfebe)

## Deployment

The Decision Tree model was deployed using various frameworks for interactive user interfaces:

1. **Streamlit App**
   - A user-friendly web app created with Streamlit for exploring predictions interactively.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/bec6286b-d98f-49a1-97ec-12ca8433a841)
snapshot of code to build streamlit app

![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/02d1c9ed-8dd3-4938-b050-36ed7c05e78d)
snapshot of app

![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef945bd5-b292-46d3-98ed-ada85bb23315)
snapshot of response message after prediction

2. **Gradio App**
   - Another web app created with Gradio, providing a simple and intuitive interface for making predictions.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef68e6ed-d202-429e-bb4b-d32652d4fa24)
snapshot of code to build gradio app

![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/b8e72429-9c1f-4171-9432-0cac4ab102f5)
snapshot demonstrating performance of gradio app

3. **FastAPI**
   - A web API built with FastAPI to serve predictions programmatically.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/f5b14c9d-3b8c-4bf4-bb12-95e104556e7e)
snapshot of code for building fastapi

![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef9f8ccd-6099-43ae-9132-b801ef124b0f)
snapsot of performance of fastapi 

## Usage

- Clone the repository:

```bash
git clone https://github.com/doeabla/Income_prediction_app.git
cd income-prediction
```

- Install dependencies:

```bash
pip install -r requirements.txt
```
- Run the Streamlit App:
  
```bash
streamlit run streamapp.py
```
- Run the Gradio App:

```bash
python gradapp.py
```
- Run FastAPI:
```bash
uvicorn main:app --reload
```

Access the respective URLs provided in the console for each deployment.
