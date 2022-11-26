# The maps methods in python
"""
* keys: Returns an iterator of keys
* items: Returns an iterable of tuples (key, value)
* values: Returns an iterable of 
* get: Returns the value associated with the given key, Returns None if the key doesn't exist
* []: Gets the value associated to the key, but an exception is raised if the key doesn't exist
* update: Updates the content of the dictionary with the new provided items
* setdefault: Returns the value associated to the key from the dictionary, otherwise the default value provided is seted and returned
* pop : Removes the value associated with the provided key
* popitem: Removes the last appended item
"""

mymap = {}

print(mymap)
print(mymap.get(0))
try:
    print(mymap[0])
except KeyError:
    print("Doesn't exist\n")


mymap.update({0: 1})
mymap[1] = 2

print(mymap.pop(0))
print(mymap)