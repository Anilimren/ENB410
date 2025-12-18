import streamlit as st
import json
import pandas as pd

# Page config
st.set_page_config(page_title="ENB410 Lab Layout", layout="wide")

# Title
st.title("ENB410 Main Page")
st.subheader("Lab Floor Plan")

## adding white background color
st.markdown("""
<style>
    .stImage {
        background-color: white;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Placeholder for map - replace with your actual map file
st.image("images/ENB410_FloorPlan.svg",caption="Lab Layout Map", use_container_width=True)


# Sidebar navigation
st.sidebar.title("🔍 Navigation")

# Navigation sections
st.header("Quick Navigation")

# Table data with Markdown link
data = {
    "Category Name": ["Bolts, Washers, Nuts"],
    "Location": ["[Drawer 4](pages/D4-Drawer4.py)"]  # clickable link
}

df = pd.DataFrame(data)

# Render table with markdown
st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)