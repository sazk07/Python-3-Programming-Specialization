"""
Currently there is a string called `str1`. Write code to 
create a list called `chars` which should contain the 
characters from `str1`. Each character in `str1` should be
its own element in the list `chars`.
"""
str1 = "I love python"
chars = [letter for letter in str1 if letter !=' ']
