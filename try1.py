import streamlit as st

st.title("Welcome to Streamlit!")

selectbox = st.selectbox(
    "Select yes or no",
    ["Yes", "No"]
)
st.write(f"You selected {selectbox}")