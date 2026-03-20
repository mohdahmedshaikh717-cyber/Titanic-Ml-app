import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))

st.title("Titanic Survival Prediction")

st.write("Name: Mohd Ahmed Shaikh")
st.write("SPN: 2403093")

pclass = st.selectbox("Passenger Class",[1,2,3])
sex = st.selectbox("Sex (0=Male,1=Female)",[0,1])
age = st.number_input("Age")
fare = st.number_input("Fare")

if st.button("Predict"):
    prediction = model.predict([[pclass,sex,age,fare]])

    if prediction[0]==1:
        st.success("Passenger will SURVIVE")
    else:
        st.error("Passenger will NOT survive")