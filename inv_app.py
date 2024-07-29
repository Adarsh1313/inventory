import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to simulate loading data from Excel file
@st.cache_data
def load_data():
    return load_data

# Sidebar for navigation
def sidebar():
    st.sidebar.title("Navigation")
    pages = ["Home", "Kidswear", "Ladieswear", "Menswear", "Accessories", "Other Items", "Activewear", "Sales Tracking"]
    return st.sidebar.radio("Go to", pages)

# Home Page
def home_page():
    st.title("Inventory Management System")
    st.write("Welcome to the Inventory Management System for your textile business.")
    st.write("Use the navigation sidebar to switch between different sections.")

# Category Pages
def category_page(category, data):
    st.title(f"{category} Inventory")
    st.write(f"Manage and view your {category} inventory here.")
    st.dataframe(data)

# Sales Tracking Page
def sales_tracking_page(data):
    st.title("Sales Tracking")
    st.write("Track your sales data here.")
    st.dataframe(data)

# Main Function to Control Page Navigation
def main():
    data = load_data()
    page = sidebar()
    
    if page == "Home":
        home_page()
    elif page in ["Kidswear", "Ladieswear", "Menswear", "Accessories", "Other Items", "Activewear"]:
        category_page(page, data.get(page, pd.DataFrame()))
    elif page == "Sales Tracking":
        sales_tracking_page(data.get("Sales", pd.DataFrame()))

if __name__ == "__main__":
    main()
