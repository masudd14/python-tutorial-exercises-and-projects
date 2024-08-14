# me={
#     "name":"masud",
#     "family":"vatankhah",
#     "age":19,
#     "email":"masudkharast@gmail.com"
# }
# print(me["name"])
# print(me["family"])
# print(me["age"])

# mydictionary=dict(name="masud",age=19)
# print(mydictionary["name"])

# print(me.values())
# print(me.keys())

# for value in me.values():
#     print(value)

# for key in me.keys():
#     print(me[key])

# for key,value in me.items():
#     print(key,value)

# isExist="name" in me 
# if "email" in me:
#     print(me["email"])
# else:
#     print("there is no email key in me")

# isNameExist="masud" in me.values()
# print(isNameExist)

# me.clear()
# print(me)

# copy_me=me.copy()
# print(me)
# print(copy_me)

# print(me == copy_me)
# print(me is copy_me)

# nweUser={"name":"unknown","family":"unknown"}
# newUser_2=dict.fromkeys(["name","family"],"something")
# print(newUser_2)

# print(me["name"])
# print(me.get("name"))

# isNameExist=me.get("phone")
# print(isNameExist is None)

# me.pop("name")
# me.popitem()
# print(me)

# second={
#     "age":20,
#     "name":"shadi"
# }
# print(second)

# second.update(me)
# print(second)