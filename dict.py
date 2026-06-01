user={
"name":"yuva",
"age":22
}
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())


for x in user:
    print(x," ",user[x])

for x in user.values():
    print(x)
  
for x in user.keys():
    print(x)
    
for x,y in user.items(): 
    print(x,y)    
    
user.update({"gender":"male"})
print(user)
user["age"]=25
print(user)
user.pop("age")
print(user)
user.clear()
print(user)


users={
   "user1":{
      "name":"yuva",
      "age":22
},
    "user2":{
      "name":"raj",
      "age":30
            }
}
print(users)

