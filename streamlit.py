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

# Load datasets for the visualizations
countries = pd.read_csv('Datasets/Four_dairy_ex.csv.csv')
Ireland_data = pd.read_csv('Datasets/Ireland_dairy_list.csv')
import matplotlib.pyplot as plt

# Main page
st.title('Ireland Dairy Export Data')

# Time series plot for countries data
st.subheader('Time Series of Dairy Exports by Country')
fig, ax = plt.subplots()
for country in countries['Area'].unique():
    country_data = countries[countries['Area'] == country]
    ax.plot(country_data['Year'], country_data['Value'], label=country)
ax.set_xlabel('Year')
ax.set_ylabel('Export Value')
ax.legend()
st.pyplot(fig)

# Time series plot for Ireland data
st.subheader('Time Series of Dairy Exports in Ireland')
fig, ax = plt.subplots()
for item in Ireland_data['Item'].unique():
    item_data = Ireland_data[Ireland_data['Item'] == item]
    ax.plot(item_data['Year'], item_data['Value'], label=item)
ax.set_xlabel('Year')
ax.set_ylabel('Export Value')
ax.legend()
st.pyplot(fig)