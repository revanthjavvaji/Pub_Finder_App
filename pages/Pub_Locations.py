import streamlit as st
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "pub_data.csv")

df = pd.read_csv(DATA_PATH)

area = st.selectbox("Select an area", df['local_authority'].unique())

filtered_df = df[df['local_authority'] == area]

fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", hover_name="name", zoom=7, height=600, color_discrete_sequence=['red'])

center_lat = filtered_df['latitude'].mean()
center_lon = filtered_df['longitude'].mean()

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_zoom=10, mapbox_center_lat=center_lat, mapbox_center_lon=center_lon)

st.plotly_chart(fig)
