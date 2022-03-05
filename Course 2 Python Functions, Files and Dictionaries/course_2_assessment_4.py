"""
Write a function called `int_return` that takes an integer as input and returns the same integer.
"""
def int_return(input_integer: int) -> int:
    return input_integer
"""
Write a function called `add` that takes any number as its input and returns that sum with 2 added.
"""
def add(num1: int) -> int:
    return num1+2
"""
Write a function called `change` that takes any string, adds “Nice to meet you!” 
to the end of the argument given, and returns that new string.
"""
def change(string_: str) -> str:
    return f"{string_} Nice to meet you!"
"""
Write a function, `accum`, that takes a list of integers as input and returns the sum of those integers.
"""
def accum(list_integers: list) -> int:
    sum=0
    for integer_ in list_integers:
        sum=sum+integer_
    return sum
"""
Write a function, `length`, that takes in a list as the input. 
If the length of the list is greater than or equal to 5, 
return “Longer than 5”. If the length is less than 5, return “Less than 5”.
"""
def length(list_: list) -> str:
    length_of_list = len(list_)
    if length_of_list >=5:
        return "Longer than 5"
    else:
        return "Less than 5"
"""
You will need to write two functions for this problem. 
The first function, `divide` that takes in any number and 
returns that same number divided by 2. The second function 
called `sum` should take any number, divide it by 2, and add 6. 
It should return this new number. You should call the `divide` 
function within the `sum` function. Do not worry about decimals.
"""
def divide(number_: int) -> float:
    return number_/2
def sum(second_number: int) -> float:
    return divide(second_number)+6
