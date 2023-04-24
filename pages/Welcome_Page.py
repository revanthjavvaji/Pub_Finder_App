from matplotlib import image
import streamlit as st
import pandas as pd
import os

st.title("Welcome to  UK Pub Finder App ")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "pub_data.csv")

df = pd.read_csv(open(DATA_PATH))
img = image.imread(open(IMAGE_PATH))
st.image(img)
st.dataframe(df)

count_pubs=df.shape[0]

st.header('Number of Pubs : %d' % count_pubs)

st.header('Number of Postal Codes : %d' % df['postcode'].unique().shape[0])