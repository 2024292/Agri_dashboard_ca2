import streamlit as st
import pandas as pd
import numpy as np


# Load datasets
value = pd.read_csv('Datasets/cleaned/export_value.csv') 
quantity = pd.read_csv('Datasets/cleaned/export_quantity.csv')
c_quantity = pd.read_csv('Datasets/cleaned/countries_quantity.csv')
c_value = pd.read_csv('Datasets/cleaned/countries_value.csv')

# Sidebar
st.sidebar.title('Ireland Agricultural Export Data')
# Sidebar options
dataset = st.sidebar.selectbox('Select Dataset', ['Export Value', 'Export Quantity', 'Countries Quantity', 'Countries Value'])

if dataset == 'Export Value':
    df = value
elif dataset == 'Export Quantity':
    df = quantity
elif dataset == 'Countries Quantity':
    df = c_quantity
else:
    df = c_value

year = st.sidebar.selectbox('Select Year', df['Year'].unique())
items = st.sidebar.multiselect('Select Items', df['Item'].unique())
countries = st.sidebar.multiselect('Select Countries', df['Area'].unique())

# Filter data based on selections
filtered_df = df[(df['Year'] == year) & (df['Item'].isin(items)) & (df['Area'].isin(countries))]

# Display table
st.write('Filtered Data', filtered_df)

# Main page
st.title('Ireland Agricultural Export Dashboard')

# Time series line chart
st.subheader('Time Series of Selected Items and Countries')
time_series_df = df[(df['Item'].isin(items)) & (df['Area'].isin(countries))]
time_series_df = time_series_df.groupby(['Year']).sum().reset_index()

st.line_chart(time_series_df.set_index('Year'))