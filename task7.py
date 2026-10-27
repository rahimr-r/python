import pandas as pd

df = pd.read_csv("orders.csv")

missing=df.isna().sum().sum()
duplicate=df.duplicated().sum()


print("Missing: amount ",missing," | Duplicates: ",duplicate)


df=df.drop_duplicates()

#Filling missing amount using median

md_value= df["amount"].median()
df["amount"]=df["amount"].fillna(md_value)
print("Median used: ",md_value)

#type conversion to numeric and string

df["amount"]=pd.to_numeric(df["amount"],errors="coerce")
df["order_id"]=df["order_id"].astype(str)

#Using groupby and agg

result=df.groupby("customer_id").agg(total=("amount","sum"),orders=("order_id","count"))
print(result)