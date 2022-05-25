print('Hello World!')


clients = [
    {
    "name" : "John",
    "age" : 12,
    "gender" : "male",
    "city_state" : ("Phoenix", "Arizona")},
    {
    "name" : "Kim",
    "age" : 39,
    "gender" : "female",
    "city_state" : ("Seattle", "Washington")
    }
]

print('Our new client is', clients[1])

print('Coming all the way from', clients[1]["city_state"])

