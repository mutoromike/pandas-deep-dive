# Dealing with CSV files

import os

import pandas as pd
import numpy as np

CSV_PATH = os.path.join(os.path.dirname(__file__), "artwork_data.csv")

# Read a CSV file into a DataFrame

# Create columns to use in the DataFrame
COLS_TO_USE = [
    "id",
    "artist",
    "title",
    "medium",
    "year",
    "acquisitionYear",
    "height",
    "width",
    "units",
]

df = pd.read_csv(CSV_PATH, index_col="id", usecols=COLS_TO_USE)

df.to_pickle("artwork_data.pickle")

# Get unique artists
artists = pd.unique(df["artist"])
print(len(artists))

new_df = df[df["artist"] == "Bacon, Francis"]
print(df['artist'].value_counts())


# You can also filter a df by a series of booleans
# Example: get all rows where the artist is "Bacon, Francis"
new_df = df[df["artist"] == "Bacon, Francis"]

# Selecting data can be done by using the loc and iloc methods
# loc is used to select data by label
# iloc is used to select data by position(index)


# LOC example
# Select all rows where the artist is "Bacon, Francis"
new_df = df.loc[df["artist"] == "Bacon, Francis", :]
# The first parameter is the rows, the second is the columns
# : means all columns, but you can specify a list of columns

# ILOC example
# Select the first 5 rows, with the first 3 columns
new_df = df.iloc[:5, :3]

# You can also select a range of rows and columns
# Select rows 3 to 5, and columns 1 to 3
new_df = df.iloc[3:6, 1:4]

# Yoou can select all rows, and only some columns
# Select all rows, and columns 1 and 3
new_df = df.iloc[:, [1, 3]]

# Getting the largest article

# doing df["height"] * df["Width"] will get an error since the data types are not the same
# Convvert strings to numbers

df.loc[:, "width"] = pd.to_numeric(df["width"], errors="coerce")

df.loc[:, "height"] = pd.to_numeric(df["height"], errors="coerce")

# Get the largest artwork, start by getting the area
df["area"] = df["height"] * df["width"]
max_area = df["area"].max()

# OPERATIONS ON GROUPS
small_df = df.iloc[49980:50019, :].copy()
grouped = small_df.groupby("artist")
