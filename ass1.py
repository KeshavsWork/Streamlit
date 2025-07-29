import streamlit as st

st.title("Choose Yout Favorite Programming Language")

lang=st.selectbox("Select any one:",["Python","JavaScript","Ruby","C++","Java","C"])
st.success(f"Your choice {lang} is successfully added")