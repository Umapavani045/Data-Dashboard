import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ✅ Load CSV data from file
df = pd.read_csv("sales_data.csv")

# ➕ Add a column for total sale
df["Total Sale"] = df["Units Sold"] * df["Price per Unit"]

# 📊 Basic statistics
print("📈 Basic Stats:")
print(df.describe())

# 🏷️ Total sales by product
product_sales = df.groupby("Product")["Total Sale"].sum()
print("\n📦 Total Sales by Product:")
print(product_sales)

# 📊 Plot 1: Bar Chart - Sales by Product
plt.figure(figsize=(6,4))
product_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.show()

# 📊 Plot 2: Pie Chart - Region-wise Sales
region_sales = df.groupby("Region")["Total Sale"].sum()

plt.figure(figsize=(5,5))
region_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Sales by Region")
plt.ylabel("")
plt.show()

# 📈 Plot 3: Line Chart - Daily Sales Trend
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Total Sale"].sum()

plt.figure(figsize=(6,4))
daily_sales.plot(marker='o', color="orange")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sale")
plt.grid(True)
plt.tight_layout()
plt.show()
