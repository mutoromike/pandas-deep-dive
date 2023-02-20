# We are assuming you have already installed pandas and numpy
# If not, run: pip install pandas numpy

import pandas as pd
import numpy as np

# Create a series with 10 random numbers
series = pd.Series(np.random.randn(10))

# Show the series
print(series)
# A Series is a one-dimensional array of indexed data.
# The index labels can be anything you want, but they must be unique.

series.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(series)

# A dataframe is a two-dimensional array of indexed data.
# It can be thought of as a dictionary of Series objects.

df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
print(df)

# You can get a column by name, which returns a Series
data = df['A']
print(data)

# You can also filter a df by a series of booleans
# Example: get all rows where the artist is "Bacon, Francis"
new_df = df[df['artist'] == 'Bacon, Francis']

# Selecting data can be done by using the loc and iloc methods
# loc is used to select data by label
# iloc is used to select data by position(index)


# LOC example
# Select all rows where the artist is "Bacon, Francis"
new_df = df.loc[df['artist'] == 'Bacon, Francis', :]
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