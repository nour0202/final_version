import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv("https://raw.githubusercontent.com/nour0202/final_version/main/Data_set.csv", encoding='utf-8', nrows=10000)

st.set_page_config(page_title='Company Portfolio')
st.title('Company Portfolio 2023')
st.subheader('Welcome to XYZ Co!')

st.markdown('---')

#insert select box



Segment = st.selectbox(
        "Select a Segment",
        ("All", "Consumer", "Home Office Segment", "Corporate"))
st.write('You selected:', Segment)

#bar graph

fig = px.bar(
      df,
      x="Segment",
      y="Profit",
      title="Profit Per Customer Segment"       
)
fig 

st.markdown("---") #horizontal line

#insert bar graph

fig = px.histogram(
    df,
    x="State",
    y="Sales",
    title="Sales Across the States"
)
fig

st.markdown("---")

#insert check box

agree = st.checkbox('I am not a Robot')

if agree:
    st.write('Welcome!')
