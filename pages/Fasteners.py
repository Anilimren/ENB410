import streamlit as st
import pandas as pd

st.title("🔩 Fasteners")

# Select fastener type
fastener_type = st.selectbox(
    "Select Fastener Type",
    ["Screws", "Washers", "Nuts"]
)

# Map selection to file
file_mapping = {
    "Screws": "data/Screws&Bolts.csv",
    "Washers": "data/Washers.csv",
    "Nuts": "data/Nuts.csv"
}

@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

try:
    df = load_data(file_mapping[fastener_type])
    
    st.subheader(f"{fastener_type} Inventory")
    st.dataframe(df, use_container_width=True, height=600)
    
    # Show total quantity only if column exists
    if 'Quantity' in df.columns:
        st.metric("Total Quantity", df['Quantity'].sum())
    
    # Search
    st.subheader("🔍 Search")
    search = st.text_input("Search in table")
    if search:
        mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
        filtered_df = df[mask]
        st.dataframe(filtered_df, use_container_width=True)
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f'{fastener_type.lower()}_inventory.csv',
        mime='text/csv',
    )
    
except FileNotFoundError:
    st.error(f"CSV file not found: {file_mapping[fastener_type]}")
except Exception as e:
    st.error(f"Error loading data: {e}")