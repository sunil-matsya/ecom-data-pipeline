import sqlite3
import pandas as pd

# ---------- 1. READ CSV FILES ----------
customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")
order_items_df = pd.read_csv("order_items.csv")
reviews_df = pd.read_csv("reviews.csv")

# ---------- 2. CONNECT TO SQLITE ----------
conn = sqlite3.connect("ecom.db")
cursor = conn.cursor()

# ---------- 3. CREATE TABLES ----------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    signup_date TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    rating INTEGER,
    review_text TEXT,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
""")

conn.commit()

# ---------- 4. INSERT CSV DATA INTO TABLES ----------
customers_df.to_sql("customers", conn, if_exists="append", index=False)
products_df.to_sql("products", conn, if_exists="append", index=False)
orders_df.to_sql("orders", conn, if_exists="append", index=False)
order_items_df.to_sql("order_items", conn, if_exists="append", index=False)
reviews_df.to_sql("reviews", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Database 'ecom.db' created and data inserted successfully!")
