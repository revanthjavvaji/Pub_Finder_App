import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os 

st.title('Nearest Pub Finder')
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "pub_data.csv")

df = pd.read_csv(DATA_PATH)


user_lat = st.number_input("Enter your latitude:")
user_lon = st.number_input("Enter your longitude:")


distances = np.sqrt((df['latitude'] - user_lat)**2 + (df['longitude'] - user_lon)**2)

nearest_pubs = df.iloc[distances.argsort()[:5]]

fig = px.scatter_mapbox(nearest_pubs, lat="latitude", lon="longitude", hover_name="name", zoom=10, height=600,color_discrete_sequence=['red'])
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_center_lat=user_lat, mapbox_center_lon=user_lon)

st.plotly_chart(fig)
