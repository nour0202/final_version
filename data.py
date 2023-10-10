import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv("https://raw.githubusercontent.com/nour0202/final_version/main/Data_set.csv", encoding='ISO-8859-1', nrows=5000)

st.set_page_config(page_title='Company Portfolio')
st.title('Company Portfolio 2023')
st.subheader('Welcome to XYZ Co!')

st.markdown('---')

#insert select box

selected_Segment = st.selectbox("Select a Segment", ['All'] + list(df['Segment'].unique()))

fil_df = df[df.Segment == selected_Segment]

fig = px.bar(
    fil_df if selected_Segment != 'All' else df, 
    x="Segment", 
    y="Profit",   
    title="Profit Distribution by Customer Segment"
)

st.plotly_chart(fig) 

st.write("This pie chart the percentages of profit as of each segment.")
st.write("As shown in the figure, Consumer Segment accounts for the highest portion of profits which is approximately 45K.")

st.markdown("---") #horizontal line

# Group by the "State" column and sum the "Sales" column
sales_by_state = df.groupby("State")["Sales"].sum().reset_index()

# Insert a slider to filter the Sales variable
sales_range = st.slider("Select Sales Range", min(sales_by_state['Sales']), max(sales_by_state['Sales']), (min(sales_by_state['Sales']), max(sales_by_state['Sales'])))

# Filter the aggregated data based on the selected sales range
filtered_sales_by_state = sales_by_state[(sales_by_state['Sales'] >= sales_range[0]) & (sales_by_state['Sales'] <= sales_range[1])]

#insert bar graph

fig = px.histogram(
    filtered_sales_by_state,
    x="State",
    y="Sales",
    title="Sales Across the States"
)
fig

st.write("This bar chart shows the total sales for each state within the specified range. You can scroll the slide bar and specify the minimum and the maximum amount of sales.")
st.write("By hovering on the columns, California registered the highest sales, then New York, and then Washington having 146K, 93k, 65k, respectively.")


st.markdown("---")
