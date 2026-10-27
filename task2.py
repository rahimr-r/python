# Creating Functions

prices = [500,1200,800,2500,300]

# Create apply discount

def apply_discount(price,discount=10):
    discount_amt= price * discount/100
    final= price - discount_amt
    return final

print("apply_discount(1000) --> ",apply_discount(1000))
print("apply_discount(1000,25) --> ",apply_discount(1000,25))

# Creating total(*args)

def total(*args):
    return sum(args)

print("total(5,10,15) --> ",total(5,10,15))

# Creating describe(**Kwargs)

def describe(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

print("Product details: ")
describe(product="Shirt",price=4000,count=2)

# Building List comprehension

above_1000 = [price for price in prices if price > 1000]
print("Price Above 1000:",above_1000)

# Using map() with lambda

gst = list(map(lambda price : round(price*1.18,2),prices))
print("With GST:",gst)

# Using filter() with lambda

below_1000 = list(filter(lambda price : price < 1000 , prices))
print("Price Below 1000: ",below_1000)