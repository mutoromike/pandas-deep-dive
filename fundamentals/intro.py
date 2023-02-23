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

series.index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(series)

# A dataframe is a two-dimensional array of indexed data.
# It can be thought of as a dictionary of Series objects.

df = pd.DataFrame(np.random.rand(10, 4), columns=["A", "B", "C", "D"])
print(df)

# You can get a column by name, which returns a Series
data = df["A"]
print(data)
