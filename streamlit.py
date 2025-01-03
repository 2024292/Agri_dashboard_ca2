import streamlit as st
import pandas as pd
import numpy as np

# Load datasets with error handling
try:
    value = pd.read_csv('Datasets/cleaned/export_value.csv') 
    quantity = pd.read_csv('Datasets/cleaned/export_quantity.csv')
except FileNotFoundError as e:
    st.error(f"Error loading data: {e}")
    st.stop()

value = value[['Item', 'Year', 'Export Value (1000 USD)']]
quantity = quantity[['Item', 'Year', 'Export Quantity (tonnes)']]

# Sidebar
st.sidebar.title('Ireland Agricultural Export Data')

# Sidebar options
dataset = st.sidebar.selectbox('Select Dataset', ['Export Value', 'Export Quantity'])

# Select dataset
if dataset == 'Export Value':
    df = value
elif dataset == 'Export Quantity':
    df = quantity

# Select year and items
year = st.sidebar.selectbox('Select Year', df['Year'].unique())
items = st.sidebar.multiselect('Select Items', df['Item'].unique())

# Filter data based on selections
filtered_df = df[(df['Year'] == year) & (df['Item'].isin(items))]

# Display table and unit price one below the other
st.write('Filtered Data', filtered_df)

# Calculate and display unit price (Export Value per tonne) based on selected year and items
if items:
    merged_df = pd.merge(
        value[(value['Year'] == year) & (value['Item'].isin(items))],
        quantity[(quantity['Year'] == year) & (quantity['Item'].isin(items))],
        on=['Year', 'Item'],
        suffixes=('_value', '_quantity')
    )
    merged_df['Unit Price (USD per tonne)'] = merged_df['Export Value (1000 USD)'] / merged_df['Export Quantity (tonnes)']
    unit_price_df = merged_df[['Year', 'Item', 'Unit Price (USD per tonne)']]
    
    # Display unit price on the main page
    st.write('Unit Price (1000 USD per tonne)', unit_price_df)
else:
    st.write('Select Items to display unit price')

# Line chart for selected items over time
if items:
    if dataset == 'Export Value':
        st.line_chart(df[df['Item'].isin(items)].groupby(['Year', 'Item'])['Export Value (1000 USD)'].sum().unstack())
    elif dataset == 'Export Quantity':
        st.line_chart(df[df['Item'].isin(items)].groupby(['Year', 'Item'])['Export Quantity (tonnes)'].sum().unstack())
else:
    st.write('Select Items to display chart')


