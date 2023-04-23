import streamlit as st
import pandas as pd
import plotly.express as px

DATA_PATH = "C:/Users/Revanth Kumar/OneDrive/Desktop/Innomatics/Pub Project/resources/data/pub_data.csv"

df = pd.read_csv(DATA_PATH)

area = st.selectbox("Select an area", df['local_authority'].unique())

filtered_df = df[df['local_authority'] == area]

fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", hover_name="name", zoom=7, height=600, color_discrete_sequence=['red'])

center_lat = filtered_df['latitude'].mean()
center_lon = filtered_df['longitude'].mean()

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(mapbox_zoom=10, mapbox_center_lat=center_lat, mapbox_center_lon=center_lon)

st.plotly_chart(fig)
