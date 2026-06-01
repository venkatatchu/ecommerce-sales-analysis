# E-Commerce Sales Analysis Report
**Week 4: Complete Data Analysis Project**  
*Data: sales_data.csv | Period: Jan 2024 – Apr 2024 | 100 transactions*

---

## 1. Executive Summary

This report presents a complete end-to-end data analysis of an e-commerce sales dataset covering 100 transactions across 5 product categories and 4 geographic regions, generating a total revenue of **₹12.37 Million**.

---

## 2. Dataset Overview

| Attribute | Value |
|-----------|-------|
| Total Records | 100 |
| Date Range | Jan 2024 – Apr 2024 |
| Products | Laptop, Tablet, Phone, Headphones, Monitor |
| Regions | North, South, East, West |
| Total Revenue | ₹12.37M |
| Avg Order Value | ₹1,23,650 |

**Data Quality**: No missing values detected. All records retained after cleaning.

---

## 3. Analysis & Visualizations

### 3.1 Sales by Product Category (Bar Chart)

Laptops dominate with **31.5%** of total revenue (₹3.89M), followed closely by Tablets (23.3%) and Phones (23.1%). Headphones and Monitors each account for roughly 11%.

| Product | Revenue | Share |
|---------|---------|-------|
| Laptop | ₹3.89M | 31.5% |
| Tablet | ₹2.88M | 23.3% |
| Phone | ₹2.86M | 23.1% |
| Headphones | ₹1.38M | 11.2% |
| Monitor | ₹1.35M | 10.9% |

### 3.2 Monthly Sales Trend (Line Chart)

Sales show variability across months, peaking in **March 2024 at ₹4.49M** — more than double the average monthly revenue of ₹3.09M. This spike warrants investigation into promotional activities or seasonal demand.

### 3.3 Sales by Region (Pie Chart)

The **North region leads** at 32.2% of total sales, with South close behind at 30.2%. East and West are underperforming relative to their potential.

| Region | Revenue | Share |
|--------|---------|-------|
| North | ₹3.98M | 32.2% |
| South | ₹3.74M | 30.2% |
| East | ₹2.52M | 20.4% |
| West | ₹2.12M | 17.2% |

---

## 4. Key Insights

1. **Laptop is the star product** — at 31.5% of revenue, it should be the centerpiece of marketing campaigns and inventory planning.

2. **March 2024 spike** — revenue in March was 45% above average. Identifying the drivers (discounts, campaigns, new listings) could help replicate this in future months.

3. **North-South dominance** — together, these two regions account for 62.4% of revenue. East and West are growth opportunities.

4. **High avg order value (₹1.23L)** — customers are making significant purchases. Bundle offers (e.g., Laptop + Monitor) or EMI options could further increase basket size.

5. **Headphones & Monitors underperform** — at ~11% each, these categories may benefit from promotions, better visibility, or pricing adjustments.

---

## 5. Recommendations

- Run targeted campaigns in **East and West** regions to close the 13–15% gap with North/South.
- Analyze **March 2024** sales data for replicable patterns (discount codes, festive events).
- Create **product bundles** pairing Laptops with Monitors or Headphones.
- Introduce **loyalty programs** for high-value customers (avg ₹1.23L/order).

---

## 6. Technical Notes

- **Tools**: Python 3, pandas, matplotlib
- **Pipeline**: Load → Clean → Explore → Analyse → Visualise → Report
- **Error Handling**: Date parsing errors handled via `errors='coerce'`; null records dropped
- **Charts**: Bar (product comparison), Line (monthly trend), Pie (regional distribution)

---

*Report generated as part of Week 4 – Data Visualization & Complete Project submission.*
