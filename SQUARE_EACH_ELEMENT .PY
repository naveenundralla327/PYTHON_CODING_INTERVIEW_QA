# using loops :

my_list = [1,3,5,7,33,45,77,88,99]
squared_list = []

for i in my_list:
    squared_list.append(i ** 2)
print(squared_list)


# using lists :

LIST = [1,3,5,7,9,11,13,15,17]
square = [x ** 2 for x in LIST]
print(square)
