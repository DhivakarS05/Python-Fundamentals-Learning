#creating a dictionary
cars = {"audi":"A10",
        "maruti":"dizire",
        "tata":"nexon",
        "mahindra":"xuv700"}
#print(cars.get("innnova"))

#check key already exsists or not
if cars.get("innnova"):
    print("Already exsists")
else:
    print("Doesn't exsists")
#update
cars.update({"toyato":"innova"})
print(cars)

#pop
cars.pop("tata")
cars.popitem()
cars.clear()
print(cars)

#print keys only
key = cars.keys()
print(key)

#print values only
value = cars.values()
print(value)

#print values using for
for values in cars.values():
    print(values)

#print values using for
for keys in cars.keys():
    print(keys)

#print ke value using cars.item()
for keys,values in cars.items():
    print(f"{keys}:{values}")

otal = 0
products ={"soap":20,
           "brush":15,
           "snacks":20,
           "milk":10,
           "panner":50}
for value in products.values():
    total = total + value
print(total)