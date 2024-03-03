import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    data = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return data

data = load_data()

st.title("Bike Sharing Dashboard")

st.sidebar.title("Information")
st.sidebar.info(
    "This dashboard displays visualizations for a Bike Sharing dataset. "
    "The dataset contains information about bike rentals based on various factors such as season, temperature, humidity, and more."
    )

st.sidebar.subheader("Dataset Exploration")
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

st.sidebar.subheader("Dataset Source")
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

st.sidebar.subheader("Weather Situations Explanations")
st.sidebar.markdown('**1:** Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('**2:** Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('**3:** Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('**4:** Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')

st.sidebar.subheader("Humidity")
st.sidebar.markdown('**Info:** Normalized and each divided by 100 (max is 100)')

st.sidebar.subheader("Humidity")
st.sidebar.markdown('**Info:** Normalized and each divided by 67 (max is 67)')

st.sidebar.subheader("Temperature")
st.sidebar.markdown('**Info:** temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)')


st.header("Explore Bike Rental Data")

st.subheader("Bike Rental Total by Season")
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x="season", y="cnt")
plt.xlabel("Season")
plt.ylabel("Bike Rental Count")
plt.title("Season-wise Bike Rental Count")
st.pyplot(plt)

st.subheader("Bike Rental Total by Weather")
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x="weathersit", y="cnt")
plt.xlabel("Weather Situation")
plt.ylabel("Bike Rental Count")
plt.title("Weather Situation-wise Bike Rental Count")
st.pyplot(plt)

st.subheader("Hourly Bike Rental Count")
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="hr", y="cnt")
plt.xlabel("Hour")
plt.ylabel("Bike Rental Count")
plt.title("Hourly Bike Rental Count")
st.pyplot(plt)

st.subheader("Scatter Plots")
col1, col2, col3 = st.columns(3)

with col1:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x="hum", y="cnt")
    plt.xlabel("Humidity")
    plt.ylabel("Bike Rental Count")
    plt.title("Humidity vs. Bike Rental Count")
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x="windspeed", y="cnt")
    plt.xlabel("Wind Speed")
    plt.ylabel("Bike Rental Count")
    plt.title("Wind Speed vs. Bike Rental Count")
    st.pyplot(plt)

with col3:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x="temp", y="cnt")
    plt.xlabel("Temperature")
    plt.ylabel("Bike Rental Count")
    plt.title("Temperature vs. Bike Rental Count")
    st.pyplot(plt)

st.sidebar.title("Created by:")
st.sidebar.markdown("**Author:** Antonius Yabes Sieman")
st.sidebar.markdown("**Email:** [yabesanthony@gmail.com](yabesanthony@gmail.com)")
st.sidebar.markdown("**LinkedIn:** [Antonius Yabes Sieman](https://www.linkedin.com/in/antoniusyabes7/)")