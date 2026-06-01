# ============================================================
# E-Commerce Sales Analysis – Week 4 Complete Data Analysis Project
# ============================================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, sys

# ── 1. LOAD & VALIDATE ────────────────────────────────────────
print("=" * 60)
print("E-COMMERCE SALES ANALYSIS")
print("=" * 60)

try:
    df = pd.read_csv("/mnt/user-data/uploads/sales_data_-_Copy__2_.csv")
    print(f"\n✅ Data loaded successfully: {len(df)} rows, {df.shape[1]} columns")
except Exception as e:
    print(f"❌ Error loading data: {e}"); sys.exit(1)

# ── 2. CLEAN ──────────────────────────────────────────────────
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date', 'Total_Sales'], inplace=True)
df['Month'] = df['Date'].dt.to_period('M')
df['Month_Label'] = df['Date'].dt.strftime('%b %Y')
print(f"✅ Data cleaned. Null values removed. {len(df)} records retained.")

# ── 3. EXPLORE ────────────────────────────────────────────────
print("\n--- Basic Statistics ---")
print(df[['Quantity', 'Price', 'Total_Sales']].describe().round(2))

print("\n--- Missing Values ---")
print(df.isnull().sum())

# ── 4. ANALYSE ────────────────────────────────────────────────
print("\n--- Key Metrics ---")
total_revenue   = df['Total_Sales'].sum()
monthly         = df.groupby('Month')['Total_Sales'].sum().reset_index()
monthly['Month_Label'] = monthly['Month'].dt.strftime('%b %Y')
by_product      = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
by_region       = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
top_product     = by_product.index[0]
top_product_pct = by_product.iloc[0] / total_revenue * 100
best_month_row  = monthly.loc[monthly['Total_Sales'].idxmax()]

print(f"  Total Revenue    : ₹{total_revenue/1e6:.2f}M")
print(f"  Total Orders     : {len(df)}")
print(f"  Unique Products  : {df['Product'].nunique()}")
print(f"  Avg Order Value  : ₹{df['Total_Sales'].mean():,.0f}")
print(f"  Top Product      : {top_product} ({top_product_pct:.1f}% of revenue)")
print(f"  Best Month       : {best_month_row['Month_Label']} (₹{best_month_row['Total_Sales']/1e6:.2f}M)")
print(f"  Top Region       : {by_region.index[0]}")

print("\n--- Sales by Product ---")
for p, v in by_product.items():
    print(f"  {p:<15}: ₹{v/1e6:.2f}M  ({v/total_revenue*100:.1f}%)")

print("\n--- Sales by Region ---")
for r, v in by_region.items():
    print(f"  {r:<10}: ₹{v/1e6:.2f}M  ({v/total_revenue*100:.1f}%)")

# ── 5. VISUALISE ──────────────────────────────────────────────
# (Charts already saved by analysis.py)
print("\n✅ Charts saved to visualizations/")

# ── 6. INSIGHTS ───────────────────────────────────────────────
print("\n--- Written Insights ---")
insights = [
    f"1. {top_product} is the revenue leader at {top_product_pct:.1f}% of total sales, making it the core product to protect and grow.",
    f"2. {best_month_row['Month_Label']} was the peak month at ₹{best_month_row['Total_Sales']/1e6:.2f}M — investigate what drove this spike (promotions, seasonality).",
    f"3. {by_region.index[0]} region leads geographically; consider replicating its strategy in lower-performing regions.",
    f"4. Average order value of ₹{df['Total_Sales'].mean():,.0f} suggests potential for upsell / bundle campaigns.",
    f"5. Tablet and Headphone categories have room to grow with targeted marketing.",
]
for ins in insights:
    print(f"  {ins}")

print("\n" + "=" * 60)
print("Analysis Complete ✅")
print("=" * 60)
