import streamlit as st
import json

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Simple password check
def check_password():
    if st.session_state.password == "swansong":
        st.session_state.authenticated = True
    else:
        st.error("❌ Incorrect password")

# Login page
if not st.session_state.authenticated:
    st.title("🔐 Lab Inventory Login")
    st.text_input("Enter Password", type="password", key="password", on_change=check_password)
    st.stop()

# Main app (only shown after authentication)
st.title("Lab Inventory")

# Load categories from JSON
@st.cache_data
def load_categories():
    with open('./data/categories.json', 'r') as f:
        return json.load(f)

categories = load_categories()

# Sidebar category selection
st.sidebar.header("Filter by Category")

category = st.sidebar.selectbox(
    "Select Category",
    list(categories.keys())
)

subcategory = st.sidebar.selectbox(
    "Select Subcategory",
    categories[category]["subcategories"]
)

# Display selected filters
st.subheader(f"Category: {category}")
st.write(f"Subcategory: {subcategory}")