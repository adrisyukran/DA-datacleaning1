import pandas as pd
import numpy as np

# Import csv file
df = pd.read_csv('ecom-testdata.csv',low_memory=False)


# Display the first few rows of the DataFrame
# print(df.head(4))

# Display the DataFrame's shape (number of rows and columns)
# print(df.shape)

# Display data types
# print(df.info())

# Date Cleaning
df['crawl_timestamp'] = pd.to_datetime(df['crawl_timestamp'], errors='coerce')

# Sort rows by Date
df = df.reindex(df['crawl_timestamp'].sort_values().index)

#Clean product_category_tree
def clear(x):
    return x.replace('["', ' ').replace('"]', ' ').replace('"', "'").split('>>')
df['product_category_tree'] = df['product_category_tree'].apply(clear)

# Display product category tree
# print(df['product_category_tree'][4])


