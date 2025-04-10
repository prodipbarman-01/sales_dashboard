import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cleaned_orders.csv")

st.title("📊 Sales Dashboard")

# Total Sales
total_sales = df['Amount'].sum()
st.metric("💰 Total Sales", f"${total_sales:,.2f}")

# Top Product
top_product = df['Product'].value_counts().idxmax()
st.metric("🏆 Top Product", top_product)

# Sales by City
st.subheader("📍 Sales by City")
city_sales = df.groupby('City')['Amount'].sum().sort_values()
st.bar_chart(city_sales)

# Orders Over Time
st.subheader("📅 Orders Over Time")
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_orders = df.groupby('Month').size()
st.line_chart(monthly_orders)
