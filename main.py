import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Coming Days")

place = st.text_input("Search location")

days = st.slider("Forecast days", min_value=1, max_value=5, help="Adjust the number of days you want to forecast.")

day_word = "day" if days == 1 else "days"

option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {day_word} in {place}:")


def get_data(days):
    dates = ["1", "2", "3", "4", "5"]
    temperatures = [20, 22, 20, 22, 20]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

dates, temperatures = get_data(days)

figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
st.plotly_chart(figure)
