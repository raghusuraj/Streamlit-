import streamlit as st
import pandas as pd

# Load the data from the CSV file and remove the 'Unnamed: 0' and 'rating&reviews' columns
df = pd.read_csv("mobiles.csv", usecols=lambda x: x not in ['Unnamed: 0', 'rating&reviews'])

# Remove all NaN values
df.dropna(inplace=True)

# Add star emoji to 'stars' column
def add_star_emoji(stars):
    return '⭐️' * int(stars)

df['stars'] = df['stars'].apply(add_star_emoji)

# Set page configuration with Device Doc name and emoji
st.set_page_config(page_title="Device Doc 👨‍⚕️")

# Display dropdown menu to select mobile
st.title("Mobile Detailing App")
mobile_list = list(df['names'])
selected_mobile = st.selectbox("Select a mobile", mobile_list)

# Display details of selected mobile
if selected_mobile:
    mobile_details = df[df['names'] == selected_mobile].iloc[0]
    st.subheader(mobile_details['names'])
    st.image(mobile_details['images_links'], use_column_width=True)
    st.write(f"Stars: {mobile_details['stars']}")
    st.write(f"Price Details: {mobile_details['price_details']}")
    st.write(f"Memory: {mobile_details['memory']}")
    st.write(f"Camera Info: {mobile_details['camara_info']}")
    st.write(f"Display: {mobile_details['display']}")
    st.write(f"Battery: {mobile_details['battery']}")
    st.write(f"Processor: {mobile_details['processor']}")
    st.write(f"Warranty: {mobile_details['warranty']}")
