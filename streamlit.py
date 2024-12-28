import streamlit as st
import pandas as pd
import numpy as np


# Load datasets
dairy_list = pd.read_csv('Datasets/Ireland_dairy_list.csv')
four_dairy_ex = pd.read_csv('Datasets/Four_dairy_ex.csv')

# Display datasets in the dashboard
st.title('Ireland Agriculture Dashboard')
st.header('Dairy List')
st.dataframe(dairy_list)

st.header('Four Dairy Exports')
st.dataframe(four_dairy_ex)
# Add a selectbox to choose the year
year = st.selectbox('Select Year', dairy_list['Year'].unique())

# Filter data based on the selected year
filtered_dairy_list = dairy_list[dairy_list['Year'] == year]
filtered_four_dairy_ex = four_dairy_ex[four_dairy_ex['Year'] == year]

# Display filtered datasets
st.header(f'Dairy List for {year}')
st.dataframe(filtered_dairy_list)

st.header(f'Four Dairy Exports for {year}')
st.dataframe(filtered_four_dairy_ex)

# Plotting
st.header('Dairy List Plot')
st.line_chart(filtered_dairy_list.set_index('Month'))

st.header('Four Dairy Exports Plot')
st.line_chart(filtered_four_dairy_ex.set_index('Month'))

