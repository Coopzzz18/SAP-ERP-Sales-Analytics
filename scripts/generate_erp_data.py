import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker()

# -------------------------
# Create folders
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FOLDER = BASE_DIR / "data" / "raw"

RAW_FOLDER.mkdir(parents=True, exist_ok=True)

# -------------------------
# Customers
# -------------------------

customers = []

for i in range(1, 201):

    customers.append({

        "CustomerID": f"CUST{i:04}",

        "CustomerName": fake.company(),

        "Country": fake.country(),

        "City": fake.city(),

        "CustomerType": random.choice([
            "Retail",
            "Distributor",
            "Restaurant",
            "Wholesaler"
        ])
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    RAW_FOLDER / "customers.csv",
    index=False
)

# -------------------------
# Materials
# -------------------------

materials = []

material_names = [
    "Olive Oil",
    "Canola Oil",
    "Cooking Spray",
    "Shortening",
    "Mayonnaise",
    "Ketchup",
    "Mustard",
    "BBQ Sauce",
    "Butter Blend",
    "Salad Dressing"
]

for i in range(1, 151):

    materials.append({

        "MaterialID": f"MAT{i:04}",

        "MaterialName": random.choice(material_names),

        "Category": random.choice([
            "Oil",
            "Condiments",
            "Sauces",
            "Butter"
        ]),

        "UnitPrice": round(random.uniform(8, 75), 2)

    })

materials_df = pd.DataFrame(materials)

materials_df.to_csv(
    RAW_FOLDER / "materials.csv",
    index=False
)

# -------------------------
# Suppliers
# -------------------------

suppliers = []

for i in range(1, 51):

    suppliers.append({

        "SupplierID": f"SUP{i:03}",

        "SupplierName": fake.company(),

        "Country": fake.country(),

        "Rating": random.randint(1, 5)

    })

suppliers_df = pd.DataFrame(suppliers)

suppliers_df.to_csv(
    RAW_FOLDER / "suppliers.csv",
    index=False
)

# -------------------------
# Plants
# -------------------------

plants = pd.DataFrame({

    "PlantID": [

        "PL01",
        "PL02",
        "PL03",
        "PL04"

    ],

    "PlantName": [

        "Los Angeles Plant",

        "Chicago Plant",

        "Dallas Plant",

        "Atlanta Plant"

    ]

})

plants.to_csv(
    RAW_FOLDER / "plants.csv",
    index=False
)

print("=" * 50)
print("ERP Master Data Generated")
print("=" * 50)

print(f"Customers : {len(customers_df)}")
print(f"Materials : {len(materials_df)}")
print(f"Suppliers : {len(suppliers_df)}")
print(f"Plants    : {len(plants)}")