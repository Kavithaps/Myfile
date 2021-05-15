# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:14:45 2021

@author: Suman
"""
import streamlit as st
st.title("streamlit demo")
st.header("ICFOSS")
# Subheader
st.subheader("Language&Technology")

# Text
st.text("ML BATCH")

# Markdown
st.markdown("### Streamlit ")
# Adding A Link
url_link = "https://icfoss.in/"
st.markdown(url_link)

st.markdown("[Google](https://google.com)")
# Error text
st.success("Successful")

st.info("This is an info alert ")

st.warning("This is a warning ")

st.error("This shows an error ")

st.exception("NameError('name not defined')")
# Images
from PIL import Image 
img = Image.open(r"C:\\users\\suman\\icfosslogo_0.png")
st.image(img,width=300,caption='Streamlit Images')
# Videos
video_file = open(r"E:\\radvdo\\VID-5-new.mp4",'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# # Audio
st.write("MP3 SONG")
audio_file = open(r"E:\\radvdo\\VID-5-new.mp4",'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes,format='audio/mp3')

# Checkbox
if st.checkbox("Show/Hide"):
        st.text("Showing or Hiding Widget")
        
# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
        st.text("Status is Active")
else:
        st.warning("Not Active Yet")
# SelectBox
occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)
# MultiSelect
location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")
salary = st.slider("What is your salary",1000,10000)
# Text Input
name = st.text_input("Enter Name","Type Here...")
if st.button('Submit'):
    result = name.title()
    st.success(result)
else:
    st.write("Press the above button..")
 # Text Area
c_text = st.text_area("Enter Text","Type Here...")
if st.button('Analyze'):
    c_result = c_text.title()
    st.success(c_result)
# SIDE Bar
st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")


# Balloons
st.balloons()
