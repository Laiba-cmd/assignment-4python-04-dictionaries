import streamlit as st
import random
import string

# Title of the app
st.title("Powerful Password Generator")

# Function to generate a password
def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User inputs
length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Include uppercase letters")
use_numbers = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

# Button to generate the password
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    st.write("### Your Generated Password:")
    st.code(password)
