
import pandas as pd

orders = pd.read_csv("orders.csv", dtype={"customer_id": str})
orders = orders.drop_duplicates()

customers = pd.read_csv("customers.csv", dtype={"customer_id": str})

#Inner Join

merge = pd.merge(orders, customers, on="customer_id", how="inner")

# Finding customer IDs that are missing from customers.csv

dropped = orders[~orders["customer_id"].isin(customers["customer_id"])]


if not dropped.empty:
    missing_id = dropped["customer_id"].iloc[0]
    print(f"Inner join rows: {len(merge)} (customer {missing_id} dropped)")
else:
    print(f"Inner join rows: {len(merge)} (no customers dropped)")

#Find customers with no orders(Left Join)

left = customers.merge(orders, on="customer_id", how="left")

no_orders = left[left["order_id"].isna()]
print("No orders:", ",".join(no_orders["name"]))

#Finding orders without customer records(Outer Join)

outer = pd.merge(orders, customers, on="customer_id",
                 how="outer", indicator=True)

no_Customer = outer[outer["_merge"] == "left_only"]

print(
    "Order without customer: customer_id",
    ",".join(no_Customer["customer_id"].astype(str).unique())
)
