#def main():
# The credit card fraud detection system web-based Gui code
    #import streamlit as st
    #import numpy as np
    #import tensorflow as tf
    import pandas as pd
    from keras.models import load_model
    #import h5py
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
        st.text('In my project, I looked into the trends of online fraudulent credit card transactions')


    with dataset:
        st.header('The Online Credit Card Transactions Dataset')
        st.text('I got this dataset from Kaggle. It contains over six million samples and 11 features of online transactions')
        st.subheader('The Datasets First Five Rows(The Head)')
        online_transactions = get_data("C:/Users/User/Documents/Ntel Ola/GUI/transact.csv")
        st.write(online_transactions.head())


    with visualisations:
        st.header('visualisation')
        st.subheader('The Distribution of the Online Credit Card Transactions')
        payment_type = pd.DataFrame(online_transactions['type'].value_counts())
        st.bar_chart(payment_type)


    with model_training:
        st.header('The Collection of Users Input To Predict Fraudulent Transactions Using The Model')
        st.text('I used  deep learning autoencoder algorithm (AE) to create the model')




        st.text('The list of online credit card transaction types and their corresponding numbers')
        st.markdown('CASH_OUT: 1')
        st.markdown('PAYMENT: 2')
        st.markdown('CASH_IN: 3')
        st.markdown('TRANSFER: 4')
        st.markdown('DEBIT: 5')

        input_feature_1 = st.slider('What transaction are you performing?', min_value=1, max_value=5, step=1, value=1)
        input_feature_2 = st.number_input('What amount would you like to input?', min_value=0.0, step=1000.0)
        input_feature_3 = st.number_input('What is your current account balance?', min_value=0.0, step=1000.0)
        input_feature_4 = st.number_input('What will your account balance be after the transaction?', min_value=0.0, step=1000.0)

    model_path = "C:/Users/User/Documents/Ntel Ola/GUI/autoenconder_mmodel.h5"
    with h5py.File(model_path, 'r') as model_path:
        model = tf.keras.models.load_model(model_path)

        #def preprocess_input(input_data):
            #return input_data

        submit = st.button('Predict')
        if submit:
            prediction = model.predict([[input_feature_1, input_feature_2, input_feature_3, input_feature_4]])
               
            if prediction == 'Fraud':
                st.write('This transaction is **fraudulent.** ')
            else:
                st.write('This transaction is **non fraudulent.** ')

#if __name__ == "__main__":
    #main()
