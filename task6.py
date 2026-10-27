import pandas as pd

df=pd.read_csv("employees.csv")

print("First Five rows:\n",df.head())
print("Showing Informations:")
df.info()
print("Statistical Summary:\n",df.describe())

print("Name column selected:\n",df["name"])
print("Name and Salary columns are selected:\n",df[["name","salary"]])

place = df.loc[df["city"] == "Chennai","name"]
print("Chennai:",",".join(place))


print("Slicing the Details:\n",df.iloc[0:3,1:3])

amount=df[df["salary"]>50000]
print("Salary above 50000:\n",amount)
print("Employees above 50000 salary:",amount.shape[0],"employees")


dept=df.loc[df["department"]=="IT","name"].to_list()
print("IT Employees:",",".join(dept))
