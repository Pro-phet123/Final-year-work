#The credit card fraud detection system web-based Gui code
import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.models import load_model
import h5py
import os



header = st.container()
dataset = st.container()
visualisations = st.container()
model_training = st.container()

@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.title('Credit Card Fraud Detection System')
    st.text('In my project, I looked into the trends of \nonline fraudulent credit card transactions.')


with dataset:
    st.header('The Online Credit Card Transactions Dataset')
    st.text("I got this dataset from Kaggle. \nIt contains over six million samples and, \n11 features of online transactions.")
    st.subheader('The Datasets First Five Rows(The Head)')
    online_transactions = get_data('transact.csv')
    st.write(online_transactions.head())


with visualisations:
    st.header('visualisation')
    st.subheader('The Distribution of the Online Credit Card Transactions')
    payment_type = pd.DataFrame(online_transactions['type'].value_counts())
    st.bar_chart(payment_type)


with model_training:
    st.subheader("**User's Input**")
    st.text("A deep learning autoencoder (AE) algorithm, \nwas used to create the model for prediction.")
    st.text("PROVIDE YOUR TRANSACTION DETAILS FOR PREDICTION.")
    

# Transaction types mapping
    transaction_types = {
        1: 'CASH_OUT',
        2: 'PAYMENT',
        3: 'CASH_IN',
        4: 'TRANSFER',
        5: 'DEBIT'
}

    input_feature_1 = st.selectbox('Select transaction type', list(transaction_types.values()))
    input_feature_2 = st.number_input('Enter transaction amount', min_value=0.0)
    input_feature_3 = st.number_input('Enter current account balance', min_value=0.0)
    input_feature_4 = st.number_input('Enter account balance after the transaction', min_value=0.0)

# Convert transaction type to numeric
    transaction_type_numeric = list(transaction_types.keys())[list(transaction_types.values()).index(input_feature_1)]


model_path = 'autoenconder_mmodel.h5'
with h5py.File(model_path, 'r') as model_path:
    model = tf.keras.models.load_model(model_path)

    submit = st.button('Predict')
    if submit:
        prediction = model.predict([[transaction_type_numeric, input_feature_2, input_feature_3, input_feature_4]])
        threshold = 0.39727665
        if prediction[0][0] <= threshold :
           st.write('This transaction is **fraudulent**.')
        else:
            st.write('This transaction is **non fraudulent**.')

