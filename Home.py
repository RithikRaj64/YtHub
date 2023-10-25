import streamlit as st

st.set_page_config(
    page_title="YtHub | Home",
    layout="centered",
    page_icon="🎥",
    initial_sidebar_state="auto",
)

st.title("🎥 YtHub")

st.write(open("README.md").read())  # type: ignore
