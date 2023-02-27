import streamlit as st
import pandas as pd
import plotly.express as px

# Load the COVID-19 data
data = pd.read_csv('country_wise_latest.csv')

# Calculate the total number of cases
total_cases = data['Confirmed'].sum()

# Calculate the percentage of cases by country
data['Percentage'] = data['Confirmed'] / total_cases * 100

# Set the page title
st.set_page_config(page_title='COVID-19 Visualization')

# Add a title to the page
st.title('COVID-19 Visualization')

# Display the raw data
st.subheader('Raw Data')
st.write(data)

# Create a bar chart of total cases by country
st.subheader('Total Cases by Country')
fig1 = px.bar(data, x='Country/Region', y='Confirmed')
st.plotly_chart(fig1)

# Create a choropleth map of total cases by country
st.subheader('Total Cases by Country')
fig1 = px.choropleth(data, locations='Country/Region', locationmode='country names', color='Confirmed',
                     hover_name='Country/Region', title='Total Cases by Country')
st.plotly_chart(fig1)
