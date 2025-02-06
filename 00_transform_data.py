# %% [markdown]
# ## Transforming the data a bit

# %%
from pathlib import Path

import pandas as pd

from utils import excel_to_file

# data path
data_path = Path("data")

# read in raw data
df = pd.read_csv(data_path / "responses_raw.csv")

# read in column mapping (as dictionary)
columns = (
    pd.read_csv(data_path / "column_mapping.csv").set_index("existing")["new"].to_dict()
)

# rename columns
df = df.rename(columns=columns)

# strip whitespace from all data
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Drop first row since it is just an example
df = df.drop(0)

df


# %% [markdown]
# ## Geography
#
# Let's have a little look at the geography of the data and see if it needs to be
# consolidated a bit.

# %%
df.groupby("geography").size()


# %%
# change values starting with "For the" to "Worldwide"
df["geography"] = df["geography"].apply(
    lambda x: "Worldwide" if x.startswith("For the") else x
)

# check counts again
df.groupby("geography").size()


# %%
# make ca_prov NaN if geography is not Canada
df.loc[df["geography"] != "Canada", "ca_prov"] = None

# make us_state NaN if geography is not US
df.loc[df["geography"] != "United States", "us_state"] = None


# %% [markdown]
# ## Company Type
#
# Let's have a look at the company type and see if it needs to be consolidated a bit.

# %%
df["company_type"].value_counts()


# %%
df["company_type"] = (
    df["company_type"]
    .str.replace("|".join(["MGU/MGA", "Mga"]), "MGA", regex=True)
    .str.replace("Agnecy", "Agency")
)


# %% [markdown]
# ## Unique Identifiers
#
# Let's create a unique identifier for each company to make it possible to filter
# to see all results for a specific company, across geographies.

# %%
df["company_code"] = (
    df["company_name"]
    .str.upper()
    # replace "W R" with "WR" (for WR Berkley)
    .str.replace(r"\bW R\b", "WR", regex=True)
    # Replace "LLOYDS SYNDICATE KI" with "KI"
    .str.replace("LLOYDS SYNDICATE KI", "KI")
    # clean up ANON companies
    .str.replace(
        "|".join(["ANONYMOUS", "PRIVATE", "CORPORATION", "SMALL BIZ"]),
        "ANON",
        regex=True,
    )
    # replace all non word / space characters with nothing
    .str.replace(r"[^A-Z\s]", "", regex=True)
    .str.split()
    .str[0]
)

# move company_code to just after company_name
cols = df.columns.tolist()
cols.insert(cols.index("company_name") + 1, cols.pop(cols.index("company_code")))
df = df[cols]

df


# %% [markdown]
# ## Save to a Spreadsheet
# Because, you know, insurance.

# %%
# Save what we have so far

with open(data_path / "responses_clean.csv", "w+") as f:
    df.to_csv(f, index=False)


# %%
with pd.ExcelWriter(data_path / "responses_clean.xlsx") as writer:
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

    cols_df = pd.read_csv(data_path / "column_mapping.csv")
    cols_df.to_excel(writer, sheet_name="column_mapping", index=False)
    df.to_excel(writer, index=False, sheet_name="responses")

cols_df = pd.read_csv(data_path / "column_mapping.csv")
excel_to_file(df, cols_df, data_path / "responses_clean.xlsx")
