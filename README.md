# 📊 SAP ERP Sales Analytics Dashboard

End-to-end Business Intelligence project simulating an SAP ERP sales environment for a manufacturing company.

This project demonstrates the complete analytics workflow from **data generation** to **executive dashboards** using:

- Python
- SQLite
- SQL
- Power BI
- Git & GitHub

---

# Project Overview

The objective of this project was to simulate an ERP sales system similar to SAP and analyze business performance through SQL and Power BI.

The project includes:

- Python-generated ERP datasets
- Relational SQLite database
- SQL reporting queries
- Executive Power BI Dashboard
- Operational Power BI Dashboard

---

# Business Questions Answered

This project answers common business questions such as:

- What is total company revenue?
- Which customers generate the most revenue?
- Which products sell the most?
- Which manufacturing plants perform best?
- Which countries generate the highest sales?
- What is the monthly sales trend?
- What percentage of orders are Completed, Cancelled, Backordered, or In Process?

---

# Tech Stack

| Tool | Purpose |
|-------|----------|
| Python | Generate ERP data |
| SQLite | Relational database |
| SQL | Business analysis |
| Power BI | Interactive dashboards |
| Git | Version control |
| GitHub | Portfolio hosting |

---

# Project Structure

```
SAP-ERP-Sales-Analytics/

├── data/
│   └── raw/
│
├── database/
│   └── erp.db
│
├── powerbi/
│   └── SAP_ERP_Sales_Dashboard.pbix
│
├── sql/
│   ├── customer_revenue.sql
│   ├── monthly_sales.sql
│   ├── top_materials.sql
│   └── ...
│
├── scripts/
│   ├── generate_erp_data.py
│   └── generate_sales_orders.py
│
├── screenshots/
│
└── README.md
```

---

# Data Model

The Power BI model follows a Star Schema.

Fact Table

- Sales Orders

Dimension Tables

- Customers
- Materials
- Plants
- Suppliers

Relationships were built using unique keys to simulate a real ERP reporting environment.

---

# SQL Analysis

SQL queries include:

- Customer Revenue Analysis
- Monthly Revenue Trends
- Top Selling Products
- Revenue by Country
- Revenue by Plant
- Order Status Analysis
- Customer Volume Analysis
- Product Performance

---

# Executive Dashboard

### Executive KPI Dashboard

![Executive Dashboard](screenshots/ERP%20Sales%20Analytics%20Dashboard.png)


Features

- Total Revenue
- Total Orders
- Total Units Sold
- Average Order Value
- Total Customers
- Revenue by Month
- Revenue by Category
- Top Customers
- Revenue by Country
- Top Products
- Order Status Breakdown

---

# Operational Dashboard

![Operational Dashboard](screenshots/operational_sales_analysis.png)

Features

- Detailed Sales Order Table
- Revenue by Country
- Revenue by Plant
- Monthly Revenue
- Operational Filtering

---

# Key Insights

Example insights from the simulated ERP data:

- Generated over **$241M** in total revenue.
- Processed over **10,000 sales orders**.
- Revenue decreased significantly after July, indicating possible seasonality.
- Completed orders represented approximately 50% of all orders.
- Revenue distribution was balanced across four manufacturing plants.

---

# Skills Demonstrated

✔ Data Modeling

✔ ETL Concepts

✔ SQL

✔ SQLite

✔ Power BI

✔ DAX Measures

✔ Dashboard Design

✔ Business Intelligence

✔ Data Visualization

✔ Git

✔ GitHub

---

# Future Improvements

Possible future enhancements include:

- Inventory Dashboard
- Supply Chain KPIs
- Sales Forecasting
- Customer Segmentation
- Machine Learning Sales Prediction
- Power BI Drillthrough Pages
- Power BI Bookmarks
- Automated Python ETL Pipeline

---

# How to Run

1. Clone the repository

```bash
git clone https://github.com/Coopzzz18/SAP-ERP-Sales-Analytics.git
```

2. Open the SQLite database

```
database/erp.db
```

3. Run SQL queries

```
sql/
```

4. Open the Power BI dashboard

```
powerbi/SAP_ERP_Sales_Dashboard.pbix
```

---

# Author

**Garrett Miranda**

Aspiring Supply Chain & Data Analyst

Skills:

- SQL
- Python
- Power BI
- Supply Chain Analytics
- Business Intelligence
- Manufacturing Analytics
