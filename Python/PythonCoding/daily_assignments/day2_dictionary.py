'''
date: 23/04/2026
description: dictionary
'''

myself = {"name" : "pp", "age" : 23, "hobby" : "sleep"}
print("my dictionary: ", myself)
print("my name: ", myself["name"])

myself["food"] = "milk"
myself["hobby"] = "tv"
print("my new dictionary: ", myself)

print("all keys: ", tuple(myself.keys()))
print("all values: ", set(myself.values()))

del myself["age"]
print("my latest dictionary: ", myself)
