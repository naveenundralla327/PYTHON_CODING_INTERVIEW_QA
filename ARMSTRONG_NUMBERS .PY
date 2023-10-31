# AN ARMSTRONG NUMBER IS A NUMBER THAT IS EQUAL TO 
# THE SUM OF ITS OWN DIGITS EACH RAISED TO THE POWER OF THE NUMBER OF DIGITS.

number = 6 
sum = 0 

for i in range(number):
    sum += int(i) ** 3 
    
if sum == int(number):
    print("Armstrong")
else:
    print("Not a Armstrong number")