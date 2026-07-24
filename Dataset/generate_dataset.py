from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker("en_IN")

products = [
    ("Laptop", "Electronics", 65000),
    ("Mouse", "Electronics", 700),
    ("Keyboard", "Electronics", 1200),
    ("Monitor", "Electronics", 15000),
    ("Office Chair", "Furniture", 8500),
    ("Study Table", "Furniture", 12000),
    ("Notebook", "Stationery", 120),
    ("Printer", "Electronics", 18000),
    ("Headphones", "Electronics", 2500),
    ("Pen Drive", "Accessories", 900)
]

regions = ["North", "South", "East", "West"]
payment_modes = ["Cash", "UPI", "Credit Card", "Debit Card"]

rows = []

for i in range(1, 501):
    product, category, price = random.choice(products)
    quantity = random.randint(1, 10)
    discount = random.choice([0, 5, 10, 15])
    sales = quantity * price * (1 - discount / 100)
    profit = round(sales * random.uniform(0.08, 0.25), 2)

    rows.append({
        "Order_Date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "Customer_Name": fake.name(),
        "Product_Name": product,
        "Category": category,
        "Region": random.choice(regions),
        "Payment_Mode": random.choice(payment_modes),
        "Quantity": quantity,
        "Unit_Price": price,
        "Discount": discount,
        "Sales": round(sales, 2),
        "Profit": profit
    })

df = pd.DataFrame(rows)

df.to_csv("Dataset/sales_data.csv", index=False)
df.to_excel("Dataset/sales_data.xlsx", index=False)

print("Dataset created successfully!")
print(df.head())