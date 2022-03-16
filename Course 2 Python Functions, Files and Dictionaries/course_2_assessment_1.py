"""
The textfile, `travel_plans.txt`, contains the summer travel 
plans for someone with some commentary. Find the total 
number of characters in the file and save to the variable `num`.
"""
num = 0
with open("travel_plans.txt",'r',encoding="utf-8") as tp:
    lines = tp.read()
    for charac in lines:
        num += 1
        
"""
We have provided a file called `emotion_words.txt` that contains 
lines of words that describe emotions. Find the total number 
of words in the file and assign this value to the variable `num_words`.
"""
num_words = 0
with open('emotion_words.txt','r',encoding="utf-8") as emot:
    lines = emot.read()
    split_lines = lines.split()
    for element in split_lines:
        num_words += 1
        
"""
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
"""
with open("school_prompt.txt",'r',encoding="utf-8") as sp:
    lines = sp.read()
    num_lines = lines.count('\n')
    
"""
Assign the first 30 characters of `school_prompt.txt` as a string to the variable `beginning_chars`.
"""
with open("school_prompt.txt",'r',encoding="utf-8") as sp:
    lines = sp.read()
    beginning_chars = lines[:30]
    
"""
Challenge: Using the file `school_prompt.txt`, assign the third word of every line to a list called `three`.
"""
three = []
with open("school_prompt.txt",'r',encoding="utf-8") as sp:
    lines = sp.read()
    split_lines = [lines for lines in sp]
    three.append(split_lines[3])
    
"""
Challenge: Create a list called `emotions` that contains the first word of every line in` emotion_words.txt`.
"""
emotions = []
with open("emotions_words.txt",'r',encoding="utf-8") as ew:
    split_lines = [lines for lines in ew]
    emotions.append(split_lines[0])
    
"""
Assign the first 33 characters from the textfile, `travel_plans.txt` to the variable `first_chars`.
"""
first_chars = ""
with open("travel_plans.txt",'r',encoding="utf-8") as tp:
    line = tp.read()
    first_chars = line[:33]
    
"""
Challenge: Using the file `school_prompt.txt`, if the character 'p' is in a word, then add the word to a list called `p_words`.
"""
p_words = []
with open("school_prompt.txt",'r',encoding="utf-8") as sp:
    lines = sp.read()
    split_words = lines.split()
    for word in line:
        if 'p' in word:
            p_words.append(word)
            
