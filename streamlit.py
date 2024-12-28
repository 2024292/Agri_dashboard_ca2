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

# Add some basic statistics
st.header('Basic Statistics')
st.subheader('Dairy List Statistics')
st.write(dairy_list.describe())

st.subheader('Four Dairy Exports Statistics')
st.write(four_dairy_ex.describe())