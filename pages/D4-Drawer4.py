import streamlit as st
import pandas as pd
import os

st.title("Drawer 4 Inventory")

# Folder containing CSV files
data_folder = "data"

# List available CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

# Dropdown to select file
selected_file = st.selectbox("📂 Select a CSV file", csv_files)

if selected_file:
    file_path = os.path.join(data_folder, selected_file)
    df = pd.read_csv(file_path)

    st.subheader(f"Contents of {selected_file}")
    st.dataframe(df, use_container_width=True)
