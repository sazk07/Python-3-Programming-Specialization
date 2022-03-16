"""
Write a function, `sublist`, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until 
it reaches the number 5 (it should not contain the number 5).
"""


def sublist(input_list: list) -> list:
    sub_list = []
    count = 0
    while count < len(input_list):
        element = input_list[count]
        if element != 5:
            sub_list.append(element)
        elif element == 5:
            break
        count += 1
    return sub_list


"""
Write a function called check_nums that takes a list as its parameter, 
and contains a while loop that only stops once the element of the list 
is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
"""


def check_nums(input_list: list) -> list:
    sub_list = []
    count = 0
    while count < len(input_list):
        element = input_list[count]
        if element != 7:
            sub_list.append(element)
        elif element == 7:
            break
        count += 1
    return sub_list


"""
Write a function, `sublist`, that takes in a list of strings as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it 
reaches the string “STOP” (it should not contain the string “STOP”).
"""


def sublist(input_list: list) -> list:
    sub_list = []
    count = 0
    while count < len(input_list):
        element = input_list[count]
        if element != "STOP":
            sub_list.append(element)
        elif element == "STOP":
            break
        count += 1
    return sub_list


"""
Write a function called `stop_at_z` that iterates through a list of strings. 
Using a while loop, append each string to a new list until the string that 
appears is “z”. The function should return the new list.
"""


def stop_at_z(input_list: list) -> list:
    sub_list = []
    count = 0
    while count < len(input_list):
        element = input_list[count]
        if element != "z":
            sub_list.append(element)
        elif element == "z":
            break
        count += 1
    return sub_list


"""
Below is a for loop that works. Underneath the for loop, rewrite the problem 
so that it does the same thing, but using a while loop instead of a for loop. 
Assign the accumulated total in the while loop code to the variable `sum2`. 
Once complete, sum2 should equal sum1.
"""
sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
# Answer
sum2 = 0
count = 0
while count < len(lst):
    sum2 = sum2 + lst[count]
    count += 1
"""
Challenge: Write a function called `beginning` that takes a list as input 
and contains a while loop that only stops once the element of the list 
is the string 'bye'. What is returned is a list that contains up to the 
first 10 strings, regardless of where the loop stops. (i.e., if it stops 
on the 32nd element, the first 10 are returned. If “bye” is the 5th element, 
the first 4 are returned.) If you want to make this even more of a challenge, 
do this without slicing
"""


def beginning(input_list: list) -> list:
    sub_list = []
    count = 0
    while count < len(input_list):
        element = input_list[count]
        if element != "bye":
            sub_list.append(element)
        elif element == "bye":
            break
        count += 1
    return sub_list[:10]
