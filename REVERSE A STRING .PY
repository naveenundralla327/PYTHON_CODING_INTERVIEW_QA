
def reverse_string(string):     # "Naveen", "Praveen", "Raju"
    return string[: : -1]

input_string = input("Enter a string : ")
print("reverse of the given string: ", reverse_string(input_string))




# ANOTHER WAY :

N = int(input())          # 123445, 456778, 987654 
reverse = 0 

while N > 0:
    digit = N % 10 
    reverse = reverse * 10 + digit 
    N = N // 10 
print(reverse)
