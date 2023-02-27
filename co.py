import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("country_wise_latest.csv")

# Set the page title
st.set_page_config(page_title="COVID-19 Dashboard")

# Set the page layout
st.title("COVID-19 Dashboard")
st.write("This dashboard shows the latest COVID-19 data by country.")

# Display a selectbox to choose the chart type
chart_type = st.selectbox("Select a chart type", ["Bar Chart", "Bubble Chart", "Choropleth Map"])

# Bar chart
if chart_type == "Bar Chart":
    st.subheader("Bar Chart")
    chart_data = df.sort_values("Confirmed", ascending=False).head(10)
    fig = px.bar(chart_data, x="Country/Region", y="Confirmed")
    st.plotly_chart(fig)

# Bubble chart
elif chart_type == "Bubble Chart":
    st.subheader("Bubble Chart")
    chart_data = df.groupby("Country/Region").agg({"Confirmed": "sum", "Recovered": "sum", "Deaths": "sum"}).reset_index()
    fig = px.scatter(chart_data, x="Recovered", y="Deaths", size="Confirmed", color="Country/Region", 
                     hover_name="Country/Region", log_x=True, log_y=True, size_max=60, title="COVID-19 Bubble Chart")
    st.plotly_chart(fig)

# Choropleth map
elif chart_type == "Choropleth Map":
    st.subheader("Choropleth Map")
    fig = px.choropleth(df, locations="Country/Region", locationmode="country names", color="Confirmed",
                        hover_name="Country/Region", projection="natural earth", title="Confirmed cases by country")
    st.plotly_chart(fig)


# Copyright
st.write("© 2023 Raghu Suraj. All rights reserved.")