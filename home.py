from sklearn.neighbors import KNeighborsClassifier  
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🫀🫀🫀การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล🫀🫀🫀")

##st.image('./img/Heart-Disease.jpg')
##st.subheader("🫀🫀🫀🫀HeartDisease🫀🫀🫀🫀🫀")
##c1,c2,c3=st.columns(3)
##with c1:
   ## st.write("")
##with c2 :
    ##st.image('./img/HeartDisease01.jpg')
##with c3 :
    ##st.write("")

dt = pd.read_csv("./data/pollution.csv")
st.header("🫀🫀🫀Data HeartDisease🫀🫀🫀")
st.write(dt.head(10))
st.subheader("สถิติโรคหัวใจ")
st.write(dt.describe())

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>มลพิศ</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

##A1 = st.number_input("กรุณาเลือกข้อมูล Age(อายุ)")
##A2 = st.selectbox("กรุณาเลือก Sex(เพศ)ชาย=1 หญิง=0",[0,1])
##A3 = st.selectbox("กรุณาเลือก ChestPainType ASY = 1 ATA =2 NAP = 3 TA = 4",[1,2,3,4])
##A4 = st.number_input("กรุณาเลือกข้อมูล RestingBP 0 - 200")
##A5 = st.number_input("กรุณาเลือกข้อมูล Cholesterol 0 - 603")
##A6 = st.selectbox("กรุณาเลือก FastingBS ",[0,1])
##A7 = st.selectbox("กรุณาเลือก RestingECG LVH = 1 Normal = 2 ST =3",[1,2,3])
##A8 = st.number_input("กรุณาเลือกข้อมูล MaxHR 0 - 202")
##A9 = st.selectbox("กรุณาเลือก ExerciseAngina Y = 1 N = 0",[0,1])
##A10 = st.number_input("กรุณาเลือกข้อมูล Oldpeak -2.6 - 6.2")
##A11= st.selectbox("กรุณาเลือก ST_Slope Down = 1 Flat = 2 UP = 3",[1,2,3])

##if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   ##dt = pd.read_csv("./data/heart02.csv") 
   ##X = dt.drop('HeartDisease', axis=1)
   ##y = dt.HeartDisease   

  ## Knn_model = KNeighborsClassifier(n_neighbors=3)
   ##Knn_model.fit(X, y)  
    
  ## x_input = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]])
   ##st.write(Knn_model.predict(x_input)
   
   ##out=Knn_model.predict(x_input)

   ##if out[0] == 1 :
    ##st.image("./img/HeartDisease01.jpg")
   ##else:
    ##st.image("./img/HT.jpg")
##else:
    ##st.write("ไม่ทำนาย")
