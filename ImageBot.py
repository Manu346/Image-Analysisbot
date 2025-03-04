# -*- coding: utf-8 -*-
"""ChatBot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qb9pbj1VNRvB7L-EgMEswBbRkPs0LXec
"""

# !pip install google-generativeai

"""import os
import google.generativeai as genai
apikey="AIzaSyBHwvYB2BJhI1Peug2wmPAZXBtZUJdpz68"
genai.configure(api_key=apikey)
"""

import os

import google.generativeai as genai

apikey= "Your-API-key"
genai.configure(api_key=apikey)

model=genai.GenerativeModel("gemini-1.5-pro-latest")

response= model.generate_content('List of top 10 Indian Cricketers in tabular format')
print(response.text)

import os
import google.generativeai as genai
from PIL import Image
img=Image.open('download.jpeg')
img.tobytes()
apikey= "AIzaSyBHwvYB2BJhI1Peug2wmPAZXBtZUJdpz68"
genai.configure(api_key=apikey)
model=genai.GenerativeModel('gemini-1.5-flash')
prompt="List 5 historic events about the city in that picture"
response=model.generate_content([prompt,img])
print(response.text)

!pip install streamlit

!npm install localtunel

# Commented out IPython magic to ensure Python compatibility.
%%writefile app.py
import streamlit as st
import google.generativeai as genai
from PIL import Image
apikey= "AIzaSyBHwvYB2BJhI1Peug2wmPAZXBtZUJdpz68"
genai.configure(api_key =apikey)
st.header("IMAGE ANALYSIS")
uploaded_file= st.file_uploader("Choose an image...", type=["png","jpeg","jpg"])
if uploaded_file is not None:
  st.image(Image.open(uploaded_file))
  # img.tobytes()
prompt=st.text_input("Enter text")
if st.button("GET RESPONSE"):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([prompt,img])
    st.markdown(response.text)


!streamlit run app.py & npx localtunnel --port 8501 & curl ipv4.icanhazip.com