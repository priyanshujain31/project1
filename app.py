import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("project1.pkl","rb")
model=pickle.load(pickle_in)
dataset= pd.read_csv('insurance.csv')


dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

# encoding 'smoker' column
dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

X = dataset.iloc[:,0:6].values

def predict_note_authentication(age,sex,bmi,children,smoker,region):
  output= model.predict([[age,sex,bmi,children,smoker,region]])
  print("Medical Insurance Cost =", output)
  #prediction=("Medical Insurance Cost=",output)

  #print(prediction)
  x=output
  output=abs(x)
  return output
def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;">Machine Learning Project</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Medical Insurance Cost Prediction")

    age=st.number_input('Insert Age',0,100)
    sex=st.number_input('Insert 0 For Male 1 For Female ',0,1)
    bmi=st.number_input('Insert a BMI',10.0,70.0)
    children=st.number_input('Insert childrens',0,6)
    smoker=st.number_input('Insert a Smoker 0 For No 1 For Yes',0,1)
    region=st.number_input('Insert a Region 0 For southeast, 1 For southwest, 2 For northeast, 3 For northwest ',0,3)

    
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(age,sex,bmi,children,smoker,region)
      st.success('Model has predicted Medical Insurance Cost= {}'.format(result))
    if st.button("About"):
      st.subheader("Developed by Priyanshu Jain")
      st.subheader("C-Section,PIET")

if __name__=='__main__':
  main()
   
