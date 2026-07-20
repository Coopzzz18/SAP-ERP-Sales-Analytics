from pathlib import Path
import sqlite3
import pandas as pd

# -------------------------
# Project Paths
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
DATABASE = BASE_DIR / "database" / "erp.db"

DATABASE.parent.mkdir(exist_ok=True)

# -------------------------
# Connect to SQLite
# -------------------------

conn = sqlite3.connect(DATABASE)

# -------------------------
# Load each CSV
# -------------------------

tables = {
    "customers": "customers.csv",
    "materials": "materials.csv",
    "plants": "plants.csv",
    "suppliers": "suppliers.csv",
    "sales_orders": "sales_orders.csv",
}

for table_name, csv_file in tables.items():

    file_path = RAW / csv_file

    print(f"Loading {csv_file}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

print("\n=================================")
print("ERP DATABASE CREATED")
print("=================================")
print(f"Database saved to:\n{DATABASE}")

conn.close()