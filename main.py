import streamlit as st
import plotly.express as px
from backend import get_data


# title, text input, slider, selext-box, plot header

st.title("Weather Forecast for the Coming Days")
place = st.text_input("Search location")
days = st.slider("Forecast days", min_value=1, max_value=5, 
                 help="Adjust the number of days you want to forecast.")
day_word = "day" if days == 1 else "days"
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {day_word} in {place}:")

# get temperature / sky data

if place: # only run further code when a place is chosen

    filtered_data = get_data(place, days)

    # display the forecast

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]

        figure = px.line(x=dates, y=temperatures, 
                         labels={"x":"Date", "y":"Temperature (C)"})
        st.plotly_chart(figure)

    images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
              "Rain":"images/rain.png","Snow":"images/snow.png"}

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=88)