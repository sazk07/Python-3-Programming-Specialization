"""
Below are a set of scores that students have received 
in the past semester. Write code to determine how many
are 90 or above and assign that result to the value `a_scores`.
"""
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
split_scores=scores.split()
a_scores = int()
for value in split_scores:
    if int(value)>=90:
        a_scores +=1
"""
Write code that uses the string stored in `org` and creates an acronym 
which is assigned to the variable `acro`. Only the first letter of each 
word should be used, each letter in the acronym should be a capital 
letter, and there should be nothing to separate the letters of the acronym.
Words that should not be included in the acronym are stored in the list
`stopwords`. For example, if `org` was assigned the string “hello to world” then
the resulting acronym should be “HW”.
"""
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
split_org = org.split()
acro = str()
for word in split_org:
    if word not in stopwords:
        acro += word[0].capitalize()
"""
Write code that uses the string stored in `sent` and 
creates an acronym which is assigned to the variable `acro`.
The first two letters of each word should be used, each letter 
in the acronym should be a capital letter, and each element of 
the acronym should be separated by a “. ” (dot and space). Words 
that should not be included in the acronym are stored in the list 
`stopwords`. For example, if `sent` was assigned the string “height and 
ewok wonder” then the resulting acronym should be “HE. EW. WO”.
"""
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
split_sent = sent.split()
acro = str()
for word in split_sent:
    if word not in stopwords:
        acro += f"{word[0].capitalize()}{word[-1].capitalize()}. "
"""
A palindrome is a phrase that, if reversed, would read the exact same.
Write code that checks if `p_phrase` is a palindrome by reversing it 
and then checking if the reversed version is equal to the original. 
Assign the reversed version of `p_phrase` to the variable `r_phrase` so 
that we can check your work.
"""
p_phrase = "was it a car or a cat I saw"
r_phrase2 = str()
for i in p_phrase:
    i = i.strip()
    r_phrase2 +=i[::-1]
if r_phrase2 == p_phrase.replace(' ', ''):
    r_phrase = p_phrase[::-1]
"""
Provided is a list of data about a store's inventory where each item
in the list represents the name of an item, how much is in stock, 
and how much it costs. Print out each item in the list with the same 
formatting, using the .format method (not string concatenation). For 
example, the first print statment should read `The store has 12 shoes, each for 29.99 USD`.
"""
# using f-strings because they are more readable than .format
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for element in inventory:
    split_at_comma = element.split(',')
    quantity = split_at_comma[1]
    description = split_at_comma[0]
    price = split_at_comma[2]
    print(f"The store has{quantity} {description}, each for{price} USD")