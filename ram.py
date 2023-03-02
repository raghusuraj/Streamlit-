import streamlit as st

def load_hanuman_chalisa(language):
    """
    Load Hanuman Chalisa lyrics in the specified language
    """
    file_path = f'{language} Lyrics.txt'
    with open(file_path, 'r', encoding='utf-8') as f:
        lyrics = f.read()
    return lyrics

# Define the available languages
languages = ['Hindi', 'English', 'Telugu']

# Set the default language to Hindi
default_language = 'Hindi'

# Add a heading and description for the app
st.title('Hanuman Chalisa')
st.write('This app displays the Hanuman Chalisa lyrics in various languages.')

# Display a 4K picture of Lord Hanuman
st.image('https://wallpaperaccess.com/full/1667709.jpg', use_column_width=True)

# Create the dropdown menu for language selection
selected_language = st.selectbox('Select a language:', languages, index=languages.index(default_language))

# Load the Hanuman Chalisa lyrics in the selected language
hanuman_chalisa_lyrics = load_hanuman_chalisa(selected_language)

# Set the font family for the app using a workaround
st.write(f'<style>body {{ font-family: Times New Roman; }}</style>', unsafe_allow_html=True)

# Display the lyrics
st.write(hanuman_chalisa_lyrics)
