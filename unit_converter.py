import streamlit as st
import streamlit.components.v1 as components

# Length Converter Function
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Weight Converter Function
def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Temperature Converter Function
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Streamlit App
def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

    st.title("🌎 Universal Unit Converter")
    st.write("Convert between different units with ease!")

    category = st.radio("Select conversion type", ["Length", "Weight", "Temperature", "Speed", "Time"], horizontal=True)
    value = st.number_input("Enter value to convert", min_value=0.0, format="%.2f")

    if category == "Length":
        from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"], index=0)
        to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"], index=1)
        result = length_converter(value, from_unit, to_unit)
    elif category == "Weight":
        from_unit = st.selectbox("From", ["kilograms", "grams", "pounds", "ounces"], index=0)
        to_unit = st.selectbox("To", ["kilograms", "grams", "pounds", "ounces"], index=1)
        result = weight_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"], index=0)
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"], index=1)
        result = temperature_converter(value, from_unit, to_unit)
    elif category == "Speed":
        from_unit = st.selectbox("From", ["meters per second", "kilometers per hour", "miles per hour", "feet per second"], index=0)
        to_unit = st.selectbox("To", ["meters per second", "kilometers per hour", "miles per hour", "feet per second"], index=1)
        conversion_factors = {"meters per second": 1, "kilometers per hour": 3.6, "miles per hour": 2.23694, "feet per second": 3.28084}
        result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    else:
        from_unit = st.selectbox("From", ["seconds", "minutes", "hours", "days"], index=0)
        to_unit = st.selectbox("To", ["seconds", "minutes", "hours", "days"], index=1)
        conversion_factors = {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400}
        result = value * conversion_factors[to_unit] / conversion_factors[from_unit]

    if st.button("🔄 Convert"):
        st.metric(label=f"Converted Value", value=f"{result:.2f} {to_unit}")
        st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}. This conversion is based on standard mathematical formulas.")
    
    st.markdown("---")
    st.markdown("<h3 style='color:green;'>🌟 Features:</h3>", unsafe_allow_html=True)
    st.markdown("✔️ Supports multiple unit conversions\n\n✔️ User-friendly interface\n\n✔️ Instant results with a single click\n\n✔️ Modern UI with enhanced styling\n\n✔️ Added Speed and Time conversions")

    components.html("""
        <div style="text-align:center; margin-top:20px;">
            <small>Developed with ❤️ using Streamlit</small>
        </div>
    """, height=50)

if __name__ == "__main__":
    main()
