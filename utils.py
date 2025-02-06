import io

import pandas as pd
import streamlit as st


def load_data():
    if "data" not in st.session_state:
        st.session_state.data = pd.read_csv("data/responses_clean.csv")
    return st.session_state.data


def to_excel(results, cols_df):
    output = io.BytesIO()
    with pd.ExcelWriter(output) as writer:
        workbook = writer.book
        info_sheet = workbook.create_sheet("info")

        info = [
            "Insurancewomen parental leave survey data",
            "",
            "see: https://instagram.com/insurancewomen for more information (and for some insurance memes too)",
            "",
            "The survey itself can be found at: https://forms.gle/AKhds1jFq5mQeddz6",
            "",
            "This file includes:",
            " - column mapping / descriptions",
            " - cleaned up version of the raw data",
            "",
            f"It was generated on {pd.Timestamp.now(tz='Europe/London').strftime('%d %B %Y @ %H:%M:%S %Z')}",
            "",
            "Apart from a little tidying here and there, the data is as it was submitted.",
            "",
            "If you believe there is an error in the data, please contact me via Instagram / insurancewomeninsta@gmail.com",
            "Evidence of the error would be appreciated.",
            "",
            f"© {pd.Timestamp.now(tz="Europe/London").year}. This work is openly licensed via CC BY-NC. Non commercial use is forbidden, and any other use must credit Insurance Women.",
            "https://creativecommons.org/licenses/by-nc/4.0/",
        ]

        for line in info:
            info_sheet.append([line])

        cols_df.to_excel(writer, sheet_name="column_mapping", index=False)
        results.to_excel(writer, index=False, sheet_name="responses")
    return output.getvalue()


def excel_to_file(results, cols_df, file):
    output_value = to_excel(results, cols_df)
    with open(file, "wb") as f:
        f.write(output_value)
