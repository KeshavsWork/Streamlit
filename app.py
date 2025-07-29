import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")
st.subheader("By keshav")
st.write("This is a simple write")

#Dataframe
df=pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[5,6,7,8]
})

st.write("Here is the dataframe")
st.write(df) 

st.text("This is a text")

#Select Box
st.selectbox("Your Favorite Chai:",["Masala Chai","Kesar Chai", "Lemon Chai"])
st.success("Your chai has brewed!!")

#line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)