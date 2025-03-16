import streamlit as st

st.title("Weather Forecast for the Coming Days")

place = st.text_input("Search location")

days = st.slider("Forecast days", min_value=1, max_value=5, help="Adjust the number of days you want to forecast.")

day_word = "day" if days == 1 else "days"

option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {day_word} in {place}:")
