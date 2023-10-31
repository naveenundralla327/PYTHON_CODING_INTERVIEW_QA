
def find_maximum_minimum(Array):
    maximum_number= Array[0]
    minimum_number = Array[0]
    
    for number in Array:
        if number > maximum_number:
            maximum_number = number
            
        if number < minimum_number:
            minimum_number = number 
    return maximum_number, minimum_number 

Array = [54,545,465,258,456]
maximum_number, minimum_number = find_maximum_minimum(Array)
print("Maximum: ", maximum_number)
print("Minimum: ", minimum_number)


