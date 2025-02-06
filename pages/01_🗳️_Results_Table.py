import pandas as pd
import streamlit as st

from utils import load_data, to_excel

st.set_page_config(page_title="Results", page_icon="🗳️", layout="wide")

results = load_data()
cols_df = pd.read_csv("data/column_mapping.csv")

st.markdown(
    """
    # The Results

    Here is a table of the results for your perusal. You can download a `csv`
    by clicking the button in the top right, or below the table.

    An Excel spreadsheet is also available for download - this is insurance after all.
    """
)

st.download_button(
    label="Download `csv`",
    data=results.to_csv(index=False),
    file_name="iw_parental_leave_responses.csv",
    icon=":material/csv:",
)

st.download_button(
    label="Download Excel spreadsheet",
    data=to_excel(results, cols_df),
    file_name="iw_parental_leave_responses.xlsx",
    icon=":material/table:",
)


with st.expander("Question -> Column Mapping"):
    st.write(
        "Here is the full text of each question in the survey, alongside the column name in the data."
    )
    st.dataframe(cols_df)

st.dataframe(results, use_container_width=True)
