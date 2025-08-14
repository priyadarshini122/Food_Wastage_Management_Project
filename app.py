import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    providers = pd.read_csv("cleaned_data/providers_clean.csv")
    receivers = pd.read_csv("cleaned_data/receivers_clean.csv")
    food_listings = pd.read_csv("cleaned_data/food_listings_clean.csv")
    claims = pd.read_csv("cleaned_data/claims_clean.csv")
    return providers, receivers, food_listings, claims

st.title("Food Wastage Dashboard")

providers, receivers, food_listings, claims = load_data()

st.subheader("Providers Data")
st.dataframe(providers)

st.subheader("Receivers Data")
st.dataframe(receivers)
