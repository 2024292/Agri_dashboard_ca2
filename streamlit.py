import streamlit as st
import pandas as pd
import numpy as np


# Load datasets
dairy_list = pd.read_csv('Datasets/Ireland_dairy_list.csv')
four_dairy_ex = pd.read_csv('Datasets/Four_dairy_ex.csv')

# Sidebar
st.sidebar.title('Ireland Agricultural Export Data')

# Select year or product
option = st.sidebar.selectbox(
    'Select View By',
    ('By Year', 'By Product')
)

# Display data based on selection
if option == 'By Year':
    year = st.sidebar.selectbox('Select Year', dairy_list['Year'].unique())
    filtered_data = dairy_list[dairy_list['Year'] == year]
else:
    product = st.sidebar.selectbox('Select Product', dairy_list['Product'].unique())
    filtered_data = dairy_list[dairy_list['Product'] == product]

# Display table
st.write('Data Table', filtered_data)

# Display line chart
st.line_chart(filtered_data.set_index('Year' if option == 'By Year' else 'Product')['Value'])

