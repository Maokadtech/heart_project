import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import pickle
import streamlit as st


heart_model=pickle.load(open('C:/Users/USER/Desktop/heartdisea/heartdiseases_model.sav','rb'))
st.title('ML deployment')

#age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
age=st.text_input('Age')
sex=st.text_input('Sex')
cp=st.text_input('cp')
trestbps=st.text_input('trestbps')
chol=st.text_input('cholestrol')
fbs=st.text_input('fbs')
restecg=st.text_input('restecg')
thalach=st.text_input('thalach')
exang=st.text_input	('exang')
oldpeak=st.text_input('oldpeak')
slope=st.text_input	('slope')
ca=st.text_input('ca')	
thal=st.text_input('thal')
heart_dis=''
#creating a button
if st.button('RESULT'):
    heart_predict=heart_model([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if heart_predict==1:
        heart_dis='heart disease detected'
    else:
        heart_dis= 'heart disease not detected'
st.success(heart_dis)     