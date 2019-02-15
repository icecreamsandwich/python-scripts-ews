import json

#list
print("\nlist\n")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#tuples
print("\ntuples\n")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#set
print("\nset\n")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#dictionary 
print("\ndictionary\n")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

def my_function():
  print("Hello from a function")

my_function()

print("\nlamda\n")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# some JSON:
print("\nconvert json to array\n")
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
