import streamlit as st
import pandas as pd

# Load data
file_path = 'New Microsoft Excel Worksheet.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the current inventory
st.title("Inventory Tracking System")
st.subheader("Current Inventory")
st.write(df)

# Input sales data
st.subheader("Sales Entry")
style = st.selectbox("Select Style", df['STYLE'].unique())
colour = st.selectbox("Select Colour", df[df['STYLE'] == style]['COLOUR'].unique())
sizes = ['XS/S', 'M/L', 'XL/2XL', '3XL']
sales = {size: st.number_input(f"Sales for {size}", min_value=0, max_value=int(df.loc[(df['STYLE'] == style) & (df['COLOUR'] == colour), size].values[0])) for size in sizes}

# Update inventory
if st.button("Update Inventory"):
    for size in sizes:
        df.loc[(df['STYLE'] == style) & (df['COLOUR'] == colour), size] -= sales[size]
    df['Qty'] = df[sizes].sum(axis=1)
    st.success("Inventory updated successfully!")
    st.write(df)

    # Save updated inventory back to the same Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    st.success("Inventory saved to Excel file successfully!")
