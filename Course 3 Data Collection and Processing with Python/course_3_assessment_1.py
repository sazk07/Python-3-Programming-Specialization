"""
The variable nested contains a nested list. Assign 'snake' to the variable `output` using indexing.
"""
nested = [
    ["dog", "cat", "horse"],
    ["frog", "turtle", "snake", "gecko"],
    ["hamster", "gerbil", "rat", "ferret"],
]
output = nested[1][2]
"""
Below, a list of lists is provided. Use in and not in tests
to create variables with Boolean values. See comments for further instructions.
"""
lst = [
    ["apple", "orange", "banana"],
    [5, 6, 7, 8, 9.9, 10],
    ["green", "yellow", "purple", "red"],
]
# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
true_or_false = lambda var, depth: True if var in lst[depth - 1] else False
yellow = true_or_false("yellow", 3)
# Test to see if 4 is in the second list of lst. Save to variable ``four``
four = true_or_false(4, 2)
# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = true_or_false("orange", 1)
"""
Below, we've provided a list of lists. Use in statements to create
variables with Boolean values - see the ActiveCode window for further directions.
"""
L = [[5, 8, 7], ["hello", "hi", "hola"], [6.6, 1.54, 3.99], ["small", "large"]]
# Test if 'hola' is in the list L. Save to variable name test1
check_if_in = lambda item, depth: True if item in L[depth - 1] else False
test1 = check_if_in("hola", 1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = bool([check_if_in([5, 8, 7], 0)])
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = check_if_in(6.6, 3)
"""
Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
"""
nested = {
    "data": ["finding", 23, ["exercises", "hangout", 34]],
    "window": [
        "part",
        "whole",
        [],
        "sum",
        [
            "math",
            "calculus",
            "algebra",
            "geometry",
            "statistics",
            ["physics", "chemistry", "biology"],
        ],
    ],
}
check_item_type = lambda item_type: nested.keys() if "key" else nested.values()
check_if_in = (
    lambda item, item_type: True if item in check_item_type(item_type) else False
)
# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = check_if_in("data", "key")
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = check_if_in(24, "value")
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = check_if_in("whole", "value")
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = check_if_in("physics", "key")
"""
The variable nested_d contains a nested dictionary with the gold medal counts
for the top four countries in the past three Olympics. Assign the value of
Great Britain's gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
"""
nested_d = {
    "Beijing": {"China": 51, "USA": 36, "Russia": 22, "Great Britain": 19},
    "London": {"USA": 46, "China": 38, "Great Britain": 29, "Russia": 22},
    "Rio": {"USA": 35, "Great Britain": 22, "China": 20, "Germany": 13},
}
london_gold = nested_d["London"]["Great Britain"]
"""
Below, we have provided a nested dictionary.
Index into the dictionary to create variables that we have listed in the ActiveCode window.
"""
sports = {
    "swimming": ["butterfly", "breaststroke", "backstroke", "freestyle"],
    "diving": ["springboard", "platform", "synchronized"],
    "track": ["sprint", "distance", "jumps", "throws"],
    "gymnastics": {
        "women": ["vault", "floor", "uneven bars", "balance beam"],
        "men": ["vault", "parallel bars", "floor", "rings"],
    },
}
# Assign the string 'backstroke' to the name v1
v1 = sports["swimming"][2]
# Assign the string 'platform' to the name v2
v2 = sports["diving"][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports["gymnastics"]["women"]
# Assign the string 'rings' to the name v4
v4 = sports["gymnastics"]["men"][-1]
"""
Given the dictionary, nested_d, save the medal count for
the USA from all three Olympics in the dictionary to the list US_count.
"""
nested_d = {
    "Beijing": {"China": 51, "USA": 36, "Russia": 22, "Great Britain": 19},
    "London": {"USA": 46, "China": 38, "Great Britain": 29, "Russia": 22},
    "Rio": {"USA": 35, "Great Britain": 22, "China": 20, "Germany": 13},
}
US_count = []
for idx1 in nested_d:
    for idx2 in nested_d[idx1]:
        x = nested_d[idx1].get("USA")
        US_count.append(x)
        break
"""
Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.
"""
l_of_l = [
    ["purple", "mauve", "blue"],
    ["red", "maroon", "blood orange", "crimson"],
    ["sea green", "cornflower", "lavender", "indigo"],
    ["yellow", "amarillo", "mac n cheese", "golden rod"],
]
third = [element[2] for element in l_of_l]
"""
Given below is a list of lists of athletes. Create a list, t,
that saves only the athlete???s Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.name if it contains the letter ???t???.
If it does not contain the letter ???t???, save the athlete name into list other.
"""
athletes = [
    ["Phelps", "Lochte", "Schooling", "Ledecky", "Franklin"],
    ["Felix", "Bolt", "Gardner", "Eaton"],
    ["Biles", "Douglas", "Hamm", "Raisman", "Mikulak", "Dalton"],
]
t = []
other = []


def list_flatter(input_list: list) -> list:
    flat_list = [item for sublist in input_list for item in sublist]
    return flat_list


new_athletes = list_flatter(athletes)
for iterable in new_athletes:
    if iterable.__contains__("t"):
        t.append(iterable)
    else:
        other.append(iterable)
