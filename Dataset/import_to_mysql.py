import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("Dataset/sales_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="SalesAnalyticsDB"
)

cursor = conn.cursor()

sql = """
INSERT INTO sales (
    order_date,
    customer_name,
    product_name,
    category,
    region,
    payment_mode,
    quantity,
    unit_price,
    discount,
    sales,
    profit
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(sql, (
        row["Order_Date"],
        row["Customer_Name"],
        row["Product_Name"],
        row["Category"],
        row["Region"],
        row["Payment_Mode"],
        int(row["Quantity"]),
        float(row["Unit_Price"]),
        float(row["Discount"]),
        float(row["Sales"]),
        float(row["Profit"])
    ))

conn.commit()

print(f"Inserted {cursor.rowcount} rows successfully!")

cursor.close()
conn.close()