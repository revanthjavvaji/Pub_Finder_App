from matplotlib import image
import streamlit as st
import pandas as pd
import os

st.title("Welcome to  UK Pub Finder App ")
IMAGE_PATH= "C:/Users/Revanth Kumar/OneDrive/Desktop/Innomatics/Pub Project/resources/images/pub.jpeg"
DATA_PATH = "C:/Users/Revanth Kumar/OneDrive/Desktop/Innomatics/Pub Project/resources/data/pub_data.csv"
df = pd.read_csv(DATA_PATH)
img = image.imread(IMAGE_PATH)
st.image(img)
st.dataframe(df)

count_pubs=df.shape[0]

st.header('Number of Pubs : %d' % count_pubs)

st.header('Number of Postal Codes : %d' % df['postcode'].unique().shape[0])