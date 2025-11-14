import pandas as pd
import streamlit as st

def clean_data(df, action):
    """Clean the data based on user's choice"""
    st.write("### Cleaning Data")
    st.write(f"Initial Data Shape: {df.shape}")

    # Replace blank strings with NaN
    df = df.replace(r'^\s*$', pd.NA, regex=True)

    if action == "Remove missing/blank values":
        df = df.dropna()
        st.success("Removed missing and blank values successfully!")
    elif action == "Fill with 'NA'":
        df = df.fillna("NA")
        st.success("Replaced missing and blank values with 'NA'!")

    # Remove duplicates
    df = df.drop_duplicates()
    st.info(f"After cleaning, data shape: {df.shape}")

    return df


def main():
    st.title("🧹 Data Cleaner App")
    st.write("Upload your CSV file and clean missing/blank values interactively.")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Initial Data Preview")
        st.dataframe(df.head())

        action = st.radio(
            "Choose how to handle missing/blank values:",
            ["Remove missing/blank values", "Fill with 'NA'"]
        )

        if st.button("Clean Data"):
            cleaned_df = clean_data(df, action)
            st.subheader("✅ Cleaned Data Preview")
            st.dataframe(cleaned_df.head())

            # Download button
            csv = cleaned_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Cleaned CSV",
                data=csv,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )
    else:
        st.info("Please upload a CSV file to begin.")


if __name__ == "__main__":
    main()



