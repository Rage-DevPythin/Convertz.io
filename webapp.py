import streamlit as st

# Setting the page configuration
st.set_page_config(
    page_title="Convertz.io",  # Updated title to match your app
    page_icon="🐱‍👤"
)

# Writing the title for the app
st.title("Welcome to Convertz.io")

# Making a description for this app
st.write("Convertz.io is a user-friendly online tool that makes unit conversions simple and fast. Easily convert distances between Metric and Imperial units with just a few clicks. Perfect for quick and accurate measurements anytime, anywhere!")

# Length Conversion Input (Kilometers to Miles)
km = st.number_input("Length - Kilometers to Miles", min_value=0.0, placeholder="Enter your value here: ")

# Capacity Conversion Input (Grams to Ounces)
grams = st.number_input("Capacity - Grams to Ounces", min_value=0.0, placeholder="Enter your value here: ")

# Weight Conversion Input (Kilograms to Pounds)
kg = st.number_input("Weight - Kilograms to Pounds", min_value=0.0, placeholder="Enter your value here: ")

# Conversion Logic: Kilometers to Miles
if km > 0:
    miles = km * 0.621371  # Convert kilometers to miles
    st.write(f"{km} kilometers is equal to {miles:.2f} miles.")
else:
    st.write("Please enter a valid number for kilometers.")

# Conversion Logic: Grams to Ounces
if grams > 0:
    ounces = grams * 0.035274  # Convert grams to ounces
    st.write(f"{grams} grams is equal to {ounces:.2f} ounces.")
else:
    st.write("Please enter a valid number for grams.")

# Conversion Logic: Kilograms to Pounds
if kg > 0: 
    lbs = kg * 2.20462 # Convert kilograms to pounds
    st.write(f"{kg} is equal to {lbs:.2f} lbs")