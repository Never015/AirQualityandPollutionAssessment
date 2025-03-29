from sklearn.neighbors import KNeighborsClassifier  
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("☁️💨☁️การพยากรณ์ คุณภาพอากาศ และ มลพิษ☁️💨☁️")

st.image('./img/air_pollution.jpg')
##st.subheader("🫀🫀🫀🫀HeartDisease🫀🫀🫀🫀🫀")
##c1,c2,c3=st.columns(3)
##with c1:
   ## st.write("")
##with c2 :
    ##st.image('./img/HeartDisease01.jpg')
##with c3 :
    ##st.write("")

dt = pd.read_csv("./data/pollution01.csv")
X = dt.drop(columns=['AirQuality']) 
st.header("☁️💨☁️Air Quality and Pollution ☁️💨☁️")
st.write(dt.head(10))
st.subheader("สถิติคุณภาพอากาศและมลพิษ")
st.write(dt.describe())

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายคุณภาพอากาศและมลพิษ</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

A1 = st.number_input("กรุณากรอกข้อมูล Temperature ")
A2 = st.slider("กรุณาเลือกข้อมูล Humidity ",float(X[:,0].min()), float(X[:,0].max()), float(X[:,0].mean()))
A3 = st.slider("กรุณาเลือกข้อมูล Weight ",-7.15,5.79)
A4 = st.slider("กรุณาเลือกข้อมูล Sweetness ",-6.89,6.37)
A5 = st.slider("กรุณาเลือกข้อมูล Crunchiness",-6.06,7.62)
A6 = st.slider("กรุณาเลือกข้อมูล Juiciness",-5.96,7.36)
A7 = st.slider("กรุณาเลือกข้อมูล Ripeness",-5.86,7.24)
A8 = st.slider("กรุณาเลือกข้อมูล Acidity",-7.01,7.4)
A9 = st.slider("กรุณาเลือกข้อมูล Acidity",-7.01,7.4)

if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   ##dt = pd.read_csv("./data/heart02.csv") 
   X = dt.drop(columns=['AirQuality']) 
   y = dt.AirQuality 
   Knn_model = KNeighborsClassifier(n_neighbors=7)
   Knn_model.fit(X, y)  
   XIn= np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9]])
   st.write(Knn_model.predict(XIn))
   out=Knn_model.predict(XIn)

   ##if out[0] == 1 :
    ##st.image("./img/HeartDisease01.jpg")
   ##else:
    ##st.image("./img/HT.jpg")
##else:
    ##st.write("ไม่ทำนาย")
