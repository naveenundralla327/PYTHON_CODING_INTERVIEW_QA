# FIBONACCI SERIES IS A SEQUENCE OF INTEGER NUMBERS FORMED BY THE ADDITION OF THE PRECEEDING TWO NUMBRS IN THE SERIES.

#   OR 

# IT'S A SEQUENCE OF NUMBERS IN WHICH EACH NUMBER IS THE SUM OF THE TWO PRECEEDING ONCE.

def fibonacci(n):
    fibonacci_series = [0,1]
    
    if n <= 0:
        return []
    
    elif n == 1:
        return [0]
    
    elif n == 2:
        return fibonacci_series 
    
    for i in range(2,n):
        next_number = fibonacci_series[i - 1] + fibonacci_series[i - 2]
        fibonacci_series.append(next_number)
    return fibonacci_series 

number_terms = 12
fibonacci_seriess = fibonacci(number_terms)
print(fibonacci_seriess)
