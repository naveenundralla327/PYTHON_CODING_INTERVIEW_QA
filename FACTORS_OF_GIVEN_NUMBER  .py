# USING FUNCTIONS:

def print_factors(number):
    for i in range(1, number + 1):
        if(number % i) == 0:
            print(i)

numbers = 18
print_factors(numbers)



# USING LOPPS : 

num = [1,2,3,4,5,6]
for i in num:
    factor_sum = 0 
    for j in range(1, i + 1):
        if i % j == 0:
            factor_sum += j 
    print(f"The sum of factors for {i} is {factor_sum}")
    
    