#Create variables of every data types and print their values and types

name="Rahim"
age=23
height=6.2
things=["Shirt","Pant","Shoes"]
others={"fav_colour": "Blue", "fav_food": "Biryani"}
numbers={1, 2, 3, 4, 5,6}
born=(11,11,2002)
print(name,type(name))
print(age,type(age))
print(height,type(height))
print(things,type(things))
print(others,type(others))
print(numbers,type(numbers))
print(born,type(born))

#Looping through a list of sales values and handling invalid or high values

sales=[12000,0,8500,15000,-200,9800]
total=0

for values in sales:
    if values <=0:
        print("Skipped ivalid value:",values)
        continue

    total=total+values

    if values > 30000:
        break

if total > 30000:
    print("Target Reached:",total)
elif total <= 30000:
    print("Target still needed to be Reached:",total)
else:
    print("Target not Reached:",total)