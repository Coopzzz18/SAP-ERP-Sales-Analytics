import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# -------------------------------------------------
# Project paths
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FOLDER = BASE_DIR / "data" / "raw"

CUSTOMERS_FILE = RAW_FOLDER / "customers.csv"
MATERIALS_FILE = RAW_FOLDER / "materials.csv"
PLANTS_FILE = RAW_FOLDER / "plants.csv"
OUTPUT_FILE = RAW_FOLDER / "sales_orders.csv"


# -------------------------------------------------
# Verify required master-data files exist
# -------------------------------------------------

required_files = [
    CUSTOMERS_FILE,
    MATERIALS_FILE,
    PLANTS_FILE,
]

for file_path in required_files:
    if not file_path.exists():
        raise FileNotFoundError(
            f"Required file not found: {file_path}\n"
            "Run generate_erp_data.py first."
        )


# -------------------------------------------------
# Read ERP master data
# -------------------------------------------------

customers_df = pd.read_csv(CUSTOMERS_FILE)
materials_df = pd.read_csv(MATERIALS_FILE)
plants_df = pd.read_csv(PLANTS_FILE)

customer_ids = customers_df["CustomerID"].tolist()
plant_ids = plants_df["PlantID"].tolist()

material_prices = dict(
    zip(
        materials_df["MaterialID"],
        materials_df["UnitPrice"],
    )
)

material_ids = list(material_prices.keys())


# -------------------------------------------------
# Sales-order options
# -------------------------------------------------

sales_channels = [
    "Direct Sales",
    "Distributor",
    "Retail",
    "E-Commerce",
]

order_statuses = [
    "Completed",
    "Completed",
    "Completed",
    "In Process",
    "Backordered",
    "Cancelled",
]

currencies = [
    "USD",
    "USD",
    "USD",
    "USD",
    "CAD",
    "AUD",
]

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 6, 30)

date_range_days = (end_date - start_date).days


# -------------------------------------------------
# Generate 10,000 sales-order lines
# -------------------------------------------------

sales_order_rows = []

for i in range(1, 10001):
    material_id = random.choice(material_ids)
    standard_price = material_prices[material_id]

    quantity = random.randint(10, 1500)

    # Simulates customer pricing, discounts, and contract rates.
    price_multiplier = random.uniform(0.90, 1.10)
    sales_price = round(standard_price * price_multiplier, 2)

    gross_revenue = round(quantity * sales_price, 2)

    discount_percent = random.choice([
        0,
        0,
        0,
        2,
        5,
        7.5,
        10,
    ])

    discount_amount = round(
        gross_revenue * (discount_percent / 100),
        2,
    )

    net_revenue = round(
        gross_revenue - discount_amount,
        2,
    )

    order_date = (
        start_date
        + timedelta(days=random.randint(0, date_range_days))
    )

    requested_delivery_date = (
        order_date
        + timedelta(days=random.randint(3, 30))
    )

    actual_delivery_date = (
        requested_delivery_date
        + timedelta(days=random.randint(-2, 8))
    )

    order_status = random.choice(order_statuses)

    if order_status in ["In Process", "Backordered"]:
        actual_delivery_date = None

    if order_status == "Cancelled":
        actual_delivery_date = None
        net_revenue = 0

    sales_order_rows.append({
        "SalesOrderID": f"SO{i:06}",
        "OrderLine": 10,
        "CustomerID": random.choice(customer_ids),
        "MaterialID": material_id,
        "PlantID": random.choice(plant_ids),
        "OrderDate": order_date.date(),
        "RequestedDeliveryDate": requested_delivery_date.date(),
        "ActualDeliveryDate": (
            actual_delivery_date.date()
            if actual_delivery_date is not None
            else None
        ),
        "Quantity": quantity,
        "UnitPrice": sales_price,
        "GrossRevenue": gross_revenue,
        "DiscountPercent": discount_percent,
        "DiscountAmount": discount_amount,
        "NetRevenue": net_revenue,
        "Currency": random.choice(currencies),
        "SalesChannel": random.choice(sales_channels),
        "OrderStatus": order_status,
    })


sales_orders_df = pd.DataFrame(sales_order_rows)


# -------------------------------------------------
# Add delivery-performance indicator
# -------------------------------------------------

sales_orders_df["RequestedDeliveryDate"] = pd.to_datetime(
    sales_orders_df["RequestedDeliveryDate"]
)

sales_orders_df["ActualDeliveryDate"] = pd.to_datetime(
    sales_orders_df["ActualDeliveryDate"]
)

sales_orders_df["DeliveryStatus"] = "Not Delivered"

delivered_mask = sales_orders_df["ActualDeliveryDate"].notna()

sales_orders_df.loc[
    delivered_mask
    & (
        sales_orders_df["ActualDeliveryDate"]
        <= sales_orders_df["RequestedDeliveryDate"]
    ),
    "DeliveryStatus",
] = "On Time"

sales_orders_df.loc[
    delivered_mask
    & (
        sales_orders_df["ActualDeliveryDate"]
        > sales_orders_df["RequestedDeliveryDate"]
    ),
    "DeliveryStatus",
] = "Late"


# -------------------------------------------------
# Save file
# -------------------------------------------------

sales_orders_df.to_csv(
    OUTPUT_FILE,
    index=False,
)


print("=" * 55)
print("ERP Sales Order Data Generated")
print("=" * 55)
print(f"Sales order lines : {len(sales_orders_df):,}")
print(f"Customers used    : {sales_orders_df['CustomerID'].nunique()}")
print(f"Materials used    : {sales_orders_df['MaterialID'].nunique()}")
print(f"Plants used       : {sales_orders_df['PlantID'].nunique()}")
print(f"Net revenue       : ${sales_orders_df['NetRevenue'].sum():,.2f}")
print(f"Saved to          : {OUTPUT_FILE}")