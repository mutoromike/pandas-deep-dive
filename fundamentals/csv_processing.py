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
