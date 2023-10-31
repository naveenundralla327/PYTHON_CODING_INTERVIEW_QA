# USING LOOPS :
 
numbers = 1,2,3,4 
sum_of_digits = 0 

for i in numbers:
    sum_of_digits += int(i)
print(sum_of_digits)



# USING LOOPS TO FIRST SUM NEXT SUM * SQUARE :

numbers = 1,2,3,4,5,6 
sum_of_elements = 0 

for i in numbers:
    squares = int(i) ** 2 
    sum_of_elements += squares 
print(sum_of_elements)
