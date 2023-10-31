# PALINDROME IS S WORD, NUMBER OR OTHER SEQUENCE OF CHARECTER THAT READS SAME FORWARD AND BACKWARD.
                  # OR
# IN PYTHON, PALINDROME CAN BE CHECKED BY A COMPARING THE ORIGINAL STRING WITH IT'S REVERSE.
# IF BOTH ARE SAME, THEN THE STRING IS A PALINDROME.

Number = input()
reverse_word = (Number[: : -1])

if reverse_word == Number:
    print("It is a Plindrome")
else:
    print("Not a Plindrome")
    
    
# ANOTHER WAY :

number = input()
replace = number.replace(",", "")
replace = replace.replace(" ", "")
Lower_string = replace.lower()
reverse_string = Lower_string[: : -1]

if Lower_string == reverse_string:
    print("It's a Plindrome")
else:
    print("It's Not a Palindrome")
    