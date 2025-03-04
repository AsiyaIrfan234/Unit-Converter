import streamlit as st

st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E;
            color: white;
        }
        .stApp {
            background-color: #1E1E1E;
            color: white;
        }
        .stTitle {
            color: #F39C12;
            font-size: 28px;
            text-align: center;
        }
        .stMarkdown {
            color: #E74C3C;
            font-size: 20px;
            text-align: center;
        }
        .stSelectbox, .stNumberInput, .stButton button {
            background-color: #FDEBD0 !important;
            color: black !important;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #F39C12 !important;
            border: none;
            color: black !important;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Unit Converter App")
st.markdown("### Converts Length, Weight, Time, and Temperature Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":  
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9

    return None  

if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "Temperature":
    unit = st.selectbox("Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:  
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion. Please check your inputs.")
