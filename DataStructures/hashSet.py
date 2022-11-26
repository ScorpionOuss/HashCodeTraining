import random

myset = set()

# Operations on sets:
"""
* add/update: To add one/multiple elements
* remove: To remove elements from the set, error if the element doesn't exist in the set
* discard: Removes if it exists, otherwise no error
* pop: removes and returns a random element from the set
* clear: remove all the elements of the set
* Union: Union of two sets (Also using the | (or) logical operator)
* Intersection: intersection of two sets (Also using the & (and) logical operator)
* Difference: Difference (There is an order is this case) difference of the second - first. Can also be done using the - operator.  
* Symmetric difference: (Xor of the two sets) Can also be done using the ^ (xor) logical operator
* in: tests if an element is in the set.
"""


# Define my set
myset = set()

malist = [random.randint(0, 10) for _ in range(20)]
print(malist)
for i in range(len(malist)):
    lastset = myset.copy()
    myset.add(malist[i])
    myset = myset.difference(lastset)
    print("last", lastset)
    print(myset)


if 0 in myset:
    print("Holle")


