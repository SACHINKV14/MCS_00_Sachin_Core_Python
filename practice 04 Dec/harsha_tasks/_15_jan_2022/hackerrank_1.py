"""You are given a spreadsheet that contains a list of  athletes and their details
(such as age, height, weight and so on).
You are required to sort the data based on the th attribute and print the final resulting table.
Follow the example given below for better understanding.
"""

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Rank': [1,2,3,4,5],
        'Age': [32,35,41,26,24],
        'Height': [190,175,188,195,176]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Sorting by column 'Country'
sorted_df=df.sort_values(by=['Age'])
print(sorted_df)

