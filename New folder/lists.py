# my_dict = {
#             'a' : 10,
#             'b' : 20,
#             'c' : 30,
#             'a': 40
# }

# print(my_dict)
# my_dict['a']= 100
# print(my_dict)

# user = {"id":1,"age":30,"city":"berlin"}

# print(user["city"])

# print(user.get("name","Unknown"))

# Checks 
# print("age" in user)

# View  Objects
# print(user.keys())
# print(user.values())
# print(user.items())

# for u in user:
#     print(u,user[u])

# for key, value in user.items():
#     print(key,value)


# user = {"id":1,"age":30,"city":"berlin"}

# Add , Remove ,Update

# user["name"] = "Jhon"  # Add
# user["age"] = 35 #update
# user.update({"age":40,"city":"Paris"})
# print(user)

# age = user.pop("salry","Not FOund")
# print("Removed Item:", age)

# To remove and delet the most rescent key value pair from the dictionary 
# user.popitem()
# print(user)

# Creation 
# user = dict.fromkeys(["id","name","age","city"],None)
# print(user)

user = {"id": 1, "age": 40, "city": 'Paris', "name": "Jhon"}
user_str = {
            k:v.upper() # Expression 
            for k,v in user.items()# Loop
            if isinstance(v,str)# Filter  
}

print(user_str)
