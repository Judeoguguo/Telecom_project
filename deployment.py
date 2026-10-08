import pandas as pd
import streamlit as st
import joblib
import os
from PIL import Image
print("All modules imported successfully")

# Getting the directory path
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory saved successfully")

# Loading the trained Model
model_path = os.path.join(script_dir, "cusomer_churn_model.pkl")
model = joblib.load(model_path)
print("Telecon Churn Model Loaded Successfully")

# Loading Image
image_path = os.path.join(script_dir, "telecom_churn_image.jpg")
image = Image.open(image_path)
print("Image Loaded Successfully")

#mapping the categorical columns
gender = {0: "Male", 1: "Female"}
Partner = {0: "No", 1: "Yes"}
Dependents = {0: "No", 1: "Yes"}
PhoneService = {0: "No", 1: "Yes"}
MultipleLines = {0: "No", 1: "No Phone Service", 2: "Yes"}
InternetService = {0: "DSL", 1: "Fiber Optic", 2: "No"}
OnlineSecurity = {0: "No", 1: "No Internet Service", 2: "Yes"}
OnlineBackup = {0: "No", 1: "No Internet Service", 2: "Yes"}
DeviceProtection = {0: "No", 1: "No Internet Service", 2: "Yes"}
TechSupport = {0: "No", 1: "No Internet Service", 2: "Yes"}
StreamingTV = {0: "No", 1: "No Internet Service", 2: "Yes"}
StreamingMovies = {0: "No", 1: "No Internet Service", 2: "Yes"}
Contract = {0: "Month-to-Month", 1: "One Year", 2: "Two Year"}
PaperlessBilling = {0: "No", 1: "Yes"}
PaymentMethod = {0: "Bank Transfer", 1: "Credit Card", 2: "Electronic Check", 3: "Mailed Check"}
Churn = {0: "No", 1: "Yes"}
print("All Mappings Saved Successfully")

# Creating user interface
st.title("Customer Churn Prediction Project")
st.image(image)
st.write("Enter the customer's details below to make predictions:")

#collect user input features
gender =  st.selectbox("Gender", options=[0, 1], format_func=lambda x: gender[x])            
SeniorCitizen = st.number_input("Senior Citizen", min_value=0, max_value=1, value=1, step=1)
Partner =  st.selectbox("Partner", options=[0, 1], format_func=lambda x: Partner[x])            
Dependents =  st.selectbox("Dependents", options=[0, 1], format_func=lambda x: Dependents[x])            
tenure =      st.number_input("Tenure", min_value=0, max_value=72, value=10, step=1)       
PhoneService =  st.selectbox("Phone Service", options=[0, 1], format_func=lambda x: PhoneService[x])            
MultipleLines =  st.selectbox("Multiple Lines", options=[0, 1, 2], format_func=lambda x: MultipleLines[x])      
InternetService =    st.selectbox("Internet Service", options=[0, 1, 2], format_func=lambda x: InternetService[x])   
OnlineSecurity =   st.selectbox("Online Security", options=[0, 1, 2], format_func=lambda x: OnlineSecurity[x])  
OnlineBackup =     st.selectbox("Online Backup", options=[0, 1, 2], format_func=lambda x: OnlineBackup[x])  
DeviceProtection =   st.selectbox("Device Protection", options=[0, 1, 2], format_func=lambda x: DeviceProtection[x])
TechSupport =       st.selectbox("Tech Support", options=[0, 1, 2], format_func=lambda x: TechSupport[x])
StreamingTV =       st.selectbox("Streaming TV", options=[0, 1, 2], format_func=lambda x: StreamingTV[x])
StreamingMovies =   st.selectbox("Streaming Movies", options=[0, 1, 2], format_func=lambda x: StreamingMovies[x])
Contract =          st.selectbox("Contract", options=[0, 1, 2], format_func=lambda x: Contract[x])
PaperlessBilling =  st.selectbox("Paperless Billing", options=[0, 1], format_func=lambda x: PaperlessBilling[x])
PaymentMethod =     st.selectbox("Payment Method", options=[0, 1, 2, 3], format_func=lambda x: PaymentMethod[x])
MonthlyCharges =    st.number_input("Monthly Charges", min_value=0, max_value=1584, value=50, step=1)
TotalCharges =      st.number_input("Total Charges", min_value=0,  max_value=6530, value=10,step=1)
print("All User Inputs Saved Successfully")

#predictions
if st.button("Predict Churn"):
    
    
    input_data = pd.DataFrame(
        [[gender, SeniorCitizen, Partner, Dependents,
       tenure, PhoneService, MultipleLines, InternetService,
       OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
       StreamingTV, StreamingMovies, Contract, PaperlessBilling,
       PaymentMethod, MonthlyCharges, TotalCharges]],
        columns=["Gender", "SeniorCitizen", "Partner", "Dependents", "Tenure", "PhoneService", "MultipleLines", "InternetService", 
                 "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", 
                 "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
                   "PaymentMethod", "MonthlyCharges", "TotalCharges"]
    )
    
    prediction = model.predict(input_data)[0]
    prediction_label = "Yes" if prediction == 1 else "No"
    st.success(f"Predicted Churn: *{prediction_label}*")
print("Prediction Made Successfully")