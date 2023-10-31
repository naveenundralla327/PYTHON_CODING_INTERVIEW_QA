# PRIME NUMBER IS A NUMBER THAT IS ONLY DIVISIBLE BY 1 AND ITAELF.


# PRIME NUMBERS FROM 1 TO as your wish the desired number - USING LOOPS :

start = int(input())
end = int(input())

for i in range(start, end + 1):
    counter = 0 
    
    for j in range(2, i):
        if (i % j == 0):
            counter = 1 
            break 
        
    if (counter == 0):
        print(i, end = " ")
        
        
# ANOTHER WAY :

initial = int(input())
final = int(input())
a = 0 

for i in range(initial, final + 1):
    if i > 1:
        if i in range(2, i):
            if(i % 1 == 0):
                break 
            else:
                a.append(i)
                
print(initial, final,len(a))
print(initial, final, a)


# ANOTHER WAY :

def is_prime(Number):
    if Number < 2:
        return False 
    
    for i in range(2, int(Number / 2) + 1):
        if Number % i == 0:
            return False 
    return True 

Number = int(input("Enter a number :  "))
if is_prime(Number):
    print("Yes")
else:
    print("No")
    
    