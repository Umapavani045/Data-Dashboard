import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

# Step 1: CSV data as a string (no file needed)
csv_data = """
Date,Product,Region,Units Sold,Price per Unit
2024-01-01,A,North,120,10
2024-01-02,B,South,80,20
2024-01-03,A,East,150,10
2024-01-04,C,West,60,25
2024-01-05,B,North,90,20
2024-01-06,C,East,70,25
2024-01-07,A,South,130,10
"""

# Step 2: Load data using StringIO
df = pd.read_csv(StringIO(csv_data))

# Step 3: Add total sale column
df["Total Sale"] = df["Units Sold"] * df["Price per Unit"]

# Step 4: Basic statistics
print("📊 Basic Statistics:\n")
print(df.describe())

# Step 5: Sales by Product
product_sales = df.groupby("Product")["Total Sale"].sum()
print("\n💰 Total Sales by Product:\n", product_sales)

# Plot 1: Bar chart - Sales by Product
plt.figure(figsize=(6,4))
product_sales.plot(kind='bar', color='lightgreen')
plt.title("Total Sales by Product")
plt.ylabel("Sales in $")
plt.xlabel("Product")
plt.tight_layout()
plt.show()

# Plot 2: Pie chart - Region-wise Sales Share
region_sales = df.groupby("Region")["Total Sale"].sum()

plt.figure(figsize=(5,5))
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# Plot 3: Line chart - Daily Sales
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Total Sale"].sum()

plt.figure(figsize=(6,4))
daily_sales.plot(marker='o', linestyle='-', color='orange')
plt.title("Daily Sales Trend")
plt.ylabel("Total Sale")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()
