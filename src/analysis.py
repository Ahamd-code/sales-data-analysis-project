import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned data
df = pd.read_csv('data/processed/cleaned_superstore.csv')

# Fix date column
df['order_date'] = pd.to_datetime(df['order_date'])

# --- Top Products ---
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False)
print("Top 10 Products by Sales:")
print(top_products.head(10))

# Save chart
os.makedirs('outputs/figures', exist_ok=True)

plt.figure(figsize=(12, 6))
top_products.head(10).plot(kind='bar')
plt.title('Top 10 Products by Sales')
plt.ylabel('Total Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig('outputs/figures/top_products.png')
plt.show()

# --- Monthly Trend ---
monthly_sales = df.groupby(df['order_date'].dt.month)['sales'].sum()
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')
plt.xticks(ticks=range(1, 13), labels=months)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('outputs/figures/monthly_trend.png')
plt.show()

# --- Regional Sales ---
regional_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
regional_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('outputs/figures/regional_sales.png')
plt.show()

print("All charts saved to outputs/figures/")