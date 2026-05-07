import pandas as pd

# Load dataset
data = pd.read_csv('data/raw/superstore.csv', encoding='latin1')

# Convert date columns
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

# Top products analysis
top_products = data.groupby('Product Name')['Sales'].sum()

top_products = top_products.sort_values(ascending=False)

print(top_products.head(10))