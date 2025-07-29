import streamlit as st

st.title("Project for learning widgets")
st.subheader("By keshav")

st.write("Navy form")

name=st.text_input("Enter your full name:")
age=st.slider("Select age:",18,25,18)
height=st.text_input("Height in cms")
weight=st.text_input("Weight in kgs")
gender = st.radio("Gender:", ["Male", "Female", "Other"])
email = st.text_input("Email Address:")
terms = st.checkbox("I confirm that the above information is correct.")

st.markdown("---")

if st.button("Submit Application"):
    if name and height and weight and email and terms:
        st.success(f"Thank you, **{name}**! \n\nYour application has been submitted.")
        st.balloons()
        st.info(f"Confirmation will be sent to: `{email}`")
    else:
        st.error("Please fill all required fields and accept the terms.")

with st.expander("Preview Your Data"):
    st.write("**Name:**", name)
    st.write("**Age:**", age)
    st.write("**Height (cm):**", height)
    st.write("**Weight (kg):**", weight)
    st.write("**Gender:**", gender)
    st.write("**Email:**", email)
