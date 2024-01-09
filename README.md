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

## Deployment

The Decision Tree model was deployed using various frameworks for interactive user interfaces:

1. **Streamlit App**
   - A user-friendly web app created with Streamlit for exploring predictions interactively.

2. **Gradio App**
   - Another web app created with Gradio, providing a simple and intuitive interface for making predictions.

3. **FastAPI**
   - A web API built with FastAPI to serve predictions programmatically.

## Usage

- Clone the repository:

```bash
git clone https://github.com/your_username/income-prediction.git
cd income-prediction

