import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta

fake = Faker()

# Helper to generate dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = pd.Timestamp("2020-01-01")
end_date = pd.Timestamp("2025-01-01")

# 1. customers.csv
customers = []
for i in range(1, 81):
    customers.append([
        i,
        fake.name(),
        fake.email(),
        random_date(start_date, end_date).date()
    ])

customers_df = pd.DataFrame(customers, columns=["customer_id", "name", "email", "signup_date"])
customers_path = "/mnt/data/customers.csv"
customers_df.to_csv(customers_path, index=False)

# 2. products.csv
categories = ["Electronics", "Books", "Clothing", "Home", "Beauty", "Sports"]
products = []
for i in range(1, 91):
    products.append([
        i,
        fake.word().capitalize() + " " + fake.word().capitalize(),
        random.choice(categories),
        round(random.uniform(10, 500), 2)
    ])

products_df = pd.DataFrame(products, columns=["product_id", "name", "category", "price"])
products_path = "/mnt/data/products.csv"
products_df.to_csv(products_path, index=False)

# 3. orders.csv
orders = []
for i in range(1, 70):
    orders.append([
        i,
        random.randint(1, len(customers)),
        random_date(start_date, end_date).date(),
        round(random.uniform(50, 2000), 2)
    ])

orders_df = pd.DataFrame(orders, columns=["order_id", "customer_id", "order_date", "total_amount"])
orders_path = "/mnt/data/orders.csv"
orders_df.to_csv(orders_path, index=False)

# 4. order_items.csv
order_items = []
order_item_id = 1
for order in orders:
    for _ in range(random.randint(1, 5)):
        order_items.append([
            order_item_id,
            order[0],
            random.randint(1, len(products)),
            random.randint(1, 5)
        ])
        order_item_id += 1

order_items_df = pd.DataFrame(order_items, columns=["order_item_id", "order_id", "product_id", "quantity"])
order_items_path = "/mnt/data/order_items.csv"
order_items_df.to_csv(order_items_path, index=False)

# 5. reviews.csv
reviews = []
review_texts = [
    "Great quality!", "Not what I expected.", "Worth the price.",
    "Fast delivery, good packaging.", "Would not recommend.", 
    "Excellent product!", "Average experience.", "Loved it!"
]

for i in range(1, 90):
    reviews.append([
        i,
        random.randint(1, len(products)),
        random.randint(1, len(customers)),
        random.randint(1, 5),
        random.choice(review_texts)
    ])

reviews_df = pd.DataFrame(reviews, columns=["review_id", "product_id", "customer_id", "rating", "review_text"])
reviews_path = "/mnt/data/reviews.csv"
reviews_df.to_csv(reviews_path, index=False)

customers_path, products_path, orders_path, order_items_path, reviews_path
