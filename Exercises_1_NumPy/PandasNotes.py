# Pandas is a data manipulation/preparation module
# If you used loops with pandas, you messed up.
------
import pandas as pd


# calling dataframes
df

# series (not used much)
-----
labels = ['first', 'second', 'third']
values = [100, 200, 400]
ser1 = pd.Series(data=values, index=labels)

# We can use df format for series to look a bit prettier in Jupyter.
ser1.to_frame() 

# This works with dictionaries as well.
d= {'a':10, 'b':20,'c':30}
ser1 = pd.Series(d)
ser1.to_frame

# Dataframes basically look like excel spreadsheets
# Most important feature in pd

# using randint to generate a seed to make fake data (pg.16 in ppt)
from numpy.random import randint
np.random.seed(321)

# filtering data
# one column 
col_df = df['Europe']

# filtering multiple columns
# COMMON
cols_df = df[['NA','SA','EU']],

# if there is an error 
 print(df['NA'])

# one-line version
cols_df = df[['NA','SA']]

# combining columns
df['Americas'] = df['NA'] + df['SA']

# quick tip, you can use backslash to continue a code line into the next line

# you can replace parts of a cell
# str , going to look for. brings it back to int
# COMMON
df['Total'] = df['Total'].str.replace('$', ").astype(int)

# checking datatypes of all columns 
df.dtypes

# custom calculations
df['MonthlySales'] = df['Total'] / 12

# dropping df variables
# ideal if you're not using them
# axis=1 is columns, axis=0 is rows.
# COMMON
df = df.drop('stuff', axis=1)

# Selecting based on values
# used as a selector
# use iloc
# VERY UNCOMMON
df.loc[]

# based on  index-based selections
# used as a selector
# COMMON
row = df.iloc[1]
row.to-frame()

df_smol = df.iloc[0:200]

-------------------------------------------------------------------------------
# Conditional filtering
-------------------------------------------------------------------------------
# INCREDIBLY COMMON
# select rows in europe that are over 40,000
# filter_df = df[condition]
# ONE FILTER
resultdf = df[df['Europe'] > 40000]
# MULTIPLE (scuffed, don't use this )
filtered = df[(df['Europe']>30000) & (df['Asia']>20000)]

# Using query for filtering
# best for advanced filtering operations
filtered = df.query("europe > 30000 and Asia > 20000")

# RECOMMENDED METHOD
# do it line by line
# easier to remember, and coherent
# Works exactly the same as using AND conditional reasoning
df = df[df['Europe] > 50000]
df = df[df['Asia'] > 40000]
df

# Resetting your index
# Sometimes, after dropping certain rows, you'll have to reset the index.
df.reset_index()

# Setting the index
# RARE
df.set_index('country')

# Using a custom function to clead/add/modify data.
# see page.41 in ppt
# COMMON

-------------------------
DATETIMES
------------------------
# When you have a datatime object 

# convert the timestamp into a datetime-object
df['LastUpdateDate'] = pd.to_datetime(df['LastUpdateDate'])

# get separate values for year, month, day
df['Year'] = df['LastUpdateDate'].dt.year
df['Month'] = df['LastUpdateDate'].dt.month
df['Day'] = df['LastUpdateDate'].dt.day


# PIP INSTALLS
#dtale
#pandas GUI