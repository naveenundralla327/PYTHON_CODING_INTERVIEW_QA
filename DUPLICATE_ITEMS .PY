# set() operator is a built-in function that creates an un-ordered collection of unique elements.
# It's takes an iterable as an argument and return a set containing all the unique elements from the iterable.

# USING SET() OPERATOR : 

data = [1,1,1,2,2,3,3,4,5,4,5,5,6,6,7,8,8,9,9]
print(list(set(data)))

# USING DICT() OPERATOR :

Data = data = [1,1,1,2,2,3,3,4,5,4,5,5,6,6,7,8,8,9,9]
print(list(dict.fromkeys(Data)))

#USING FOR LOOP :

DATA = [1,1,1,2,2,3,3,4,5,4,5,5,6,6,7,8,8,9,9]
duplicate = []
for i in DATA:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
