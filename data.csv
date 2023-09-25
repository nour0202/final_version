import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_excel(r"C:\Users\Admin\Desktop\Data.xlsx")

st.set_page_config(page_title='Company Portfolio')
st.title('Company Portfolio 2023')
st.subheader('Welcome to XYZ Co!')

st.markdown('---')

df=pd.read_excel(r"C:\Users\Admin\Desktop\Data.xlsx")

#insert select box

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

option = st.selectbox(
        "Select a Segment",
        ("All", "Consumer", "Home Office Segment", "Corporate"),
        key=df,
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
)

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
