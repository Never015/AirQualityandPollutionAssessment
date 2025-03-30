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

A1 = st.number_input("กรุณากรอกข้อมูล Temperature ",13.4,58.4)
A2 = st.slider("กรุณาเลือกข้อมูล Humidity ",36,128.1)
A3 = st.slider("กรุณาเลือกข้อมูล PM2.5 ",0,259)
A4 = st.slider("กรุณาเลือกข้อมูล PM10 ",-0.2,315.8)
A5 = st.slider("กรุณาเลือกข้อมูล NO2",7.4,64.9)
A6 = st.slider("กรุณาเลือกข้อมูล SO2",-6.2,44.9)
A7 = st.slider("กรุณาเลือกข้อมูล CO",0.65,3.72)
A8 = st.slider("กรุณาเลือกข้อมูล Proximity_to_Industrial_Areas",2.5,25.8)
A9 = st.slider("กรุณาเลือกข้อมูล Population_Density",188,957)

if st.button("ทำนายผล"):
    #st.write("ทำนาย"S) 
   dt = pd.read_csv("./data/pollution01.csv")
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
