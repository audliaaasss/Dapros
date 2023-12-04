import streamlit as st
import pandas as pd

def main():
    st.title("Data Processing Project")
    st.write("Kelompok: Alfajri, Hafizh, Kharisma, Odi")

    # Upload CSV file through Streamlit
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Tombol "Process" untuk menampilkan data setelah file diunggah
    if uploaded_file is not None:
        if st.button("Process CSV"):
            # Read CSV file into DataFrame
            df = pd.read_csv(uploaded_file)

            # Display the DataFrame
            st.write("## Data Preview:")
            st.write(df)

            # Additional functionalities can be added here based on your requirements

if __name__ == "__main__":
    main()
