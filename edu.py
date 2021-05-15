# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:11:41 2021

@author: Suman
"""


#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Tips_Dataset")

#import dataset
df = pd.read_csv(r'C:\\users\\suman\\tips.csv')
#First thirty rows
tips = df.head(10)
#Display the table
st.table(tips)
#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='sex',palette='rainbow')
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()