# Credit Card Fraud Detection System

<p align="center">
  <b>Deep learning-based fraud detection system for identifying suspicious online credit card transactions in real time.</b>
</p>

---

## Overview

The **Credit Card Fraud Detection System** is a web-based machine learning application designed to analyze online financial transactions and detect potentially fraudulent activities.

Built with **Streamlit**, **TensorFlow**, and **Python**, the system leverages an **Autoencoder deep learning model** trained on large-scale transaction data to identify abnormal transaction behavior patterns.

The platform provides:
- Real-time fraud prediction  
- Transaction data analysis  
- Interactive visualizations  
- User-friendly fraud detection interface  

---

##  Key Features

### 🧠 Deep Learning Fraud Detection Engine
Uses an Autoencoder neural network to detect anomalous transaction behavior associated with fraudulent activity.

---

### 📈 Transaction Data Visualization
Interactive visualizations for exploring:
- Transaction distributions  
- Fraud vs non-fraud patterns  
- Behavioral trends in payment activity  

---

### ⚡ Real-Time Prediction System
Allows users to input transaction details and instantly receive fraud prediction results.

---

### 📊 Dataset Exploration Interface
Provides insight into transaction records, feature distributions, and sample financial data.

---

## Model Overview

- **Algorithm:** Deep Learning Autoencoder  
- **Task Type:** Anomaly Detection / Fraud Detection  
- **Framework:** TensorFlow / Keras  
- **Input Features:** Online transaction attributes  
- **Output:** Fraudulent or Non-Fraudulent transaction prediction  

The model was trained using a large-scale online payment transaction dataset containing millions of transaction records.

---

## 🏗️ System Architecture

```text
User Transaction Input
        ↓
Data Validation & Preprocessing
        ↓
Feature Engineering Layer
        ↓
Autoencoder Deep Learning Model
        ↓
Anomaly Detection Logic
        ↓
Fraud Prediction Output
        ↓
Streamlit Visualization Interface

```
##Run Locally 

#### Clone the repo
```bash
git clone https://github.com/Pro-phet123/Final-year-work.git
```
#### Enter into project directory
```bash
cd Final-year-work
```
#### Create virtual environment
```bash
python -m venv venv
```
#### Activate virtual environment(windows)
```bash
venv\Scripts\activate
```

#### Activate virtual environment(mac/linux)
```bash
source venv/bin/activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```
#### Run the application
```bash
streamlit run main.py
```

## 🌐 Live Demo

[Launch Web App](https://pro-phet123-final-year-work-main-6mzu7f.streamlit.app/)
