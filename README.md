# Credit Card Fraud Detection System Web-Based GUI

The Credit Card Fraud Detection System is a web-based graphical user interface (GUI) built to analyze online credit card transactions and predict fraudulent activities. It utilizes Python programming with libraries such as Streamlit, NumPy, TensorFlow, and pandas to create an interactive and informative platform.

## Features

**Dataset Exploration:** Provides insights into the online credit card transactions dataset, sourced from Kaggle, including key features and sample data.

**Data Visualizations:** Visualizes the distribution of online credit card transactions to understand trends and patterns.

**Model Prediction:** Utilizes a deep learning autoencoder algorithm to predict fraudulent transactions based on user input.


## Prerequisites

Before running the project, ensure you have Python 3.9 installed on your system.


## To Setup Locally


**1. Clone this project repository :**


```bash
git clone https://github.com/Pro-phet123/Final-year-work.git
```

**2. Change into the project directory :**

```bash
Cd main.py/ 
```

**3. Install Project Dependencies :**

```bash
pip install -r requirements.txt
```

**4. Run The Web Application :**

```bash
streamlit run main.py 
```


# About The Web Application

## Link To The Web Application (Deployed Using Streamlit): https://pro-phet123-final-year-work-main-6mzu7f.streamlit.app/


## Using The Web Application 

**1. Provide Input for Prediction:** Enter the following values:

A Dropdown menu was used to choose the type of transaction to take place.

While textbox was used to:

Enter transaction amount.

Enter current account balance.

Enter account balance after the transaction.

**2. Click Predict:** The application will display the prediction of the transactionwhetherit was fraudulentor not.


## Dataset

The dataset I used is a sample of a dataset gotten from Kaggle. It contains six million online credit card transaction samples and 11 features of each transaction. An autoencoder was used for the development(which includes training and testing the model) and Streamlit was used to create a web app for the application.

*The link to the full dataset:* https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset


## Model

The prediction model is an Autoencoder model trained on the provided dataset.

## Technology Stack

Python

Streamlit

NumPy

Seaborn

TensorFlow

Matplotlib

Pandas

Keras

H5py


## Some Informations To Note

The ```autoenconder_mmodel.h5``` file contains the trained deep learning model.

The ```transactions.csv``` file contains the past history of users transactions dataset.

## Contact

For any questions or feedback, please reach out to [Name: Olalemi Olaoluwakintan, E-mail: olalemiolaoluwakintan@gmail.com].
