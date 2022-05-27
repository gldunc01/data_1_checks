from unicodedata import name

# statement that prints Hello World
print('Hello World!')

# a list with several values and a dictionary with 2 key value pairs and a tuple with 4 values
clients = [
    {
    "name" : "John",
    "age" : 12,
    "gender" : "Male",
    "city_state" : ("Phoenix", "Arizona")},
    {
    "name" : "Kim",
    "age" : 39,
    "gender" : "Female",
    "city_state" : ("Seattle", "Washington")
    }
]

# print one of the dictionary items and one of the tuples
# added formatting which is why you see so many prints

print('Our new client is:\n', "", "Name:", clients[1]["name"])
print(" ","Age:", clients[1]["age"])
print(" ", "Gender:", clients[1]["gender"])

print(" ", 'Coming all the way from', clients[1]["city_state"][0], clients[1]["city_state"][1])

