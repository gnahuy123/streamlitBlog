import streamlit as st
from sidebar import render_sidebar

st.set_page_config(page_title="Tan Yu Hang", page_icon=":tada:", layout="wide")

render_sidebar()
# Main Page Content
st.title("Hi, I am Yu Hang")
st.image("pictures/selfie.jpg", caption="Figure 1: Picture of me taken on 9th May 2025")

st.subheader("A Year 1 Computer Science student at NUS")
st.write("This blog contains my journey at NUS, mod reviews and also gives tips to students doing Computer Science in NUS.")

st.markdown("---")

