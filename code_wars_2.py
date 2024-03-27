#####################################################################################
###############   ZADANIE 100     ###################################################
#####################################################################################

"""Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21]."""


# Rozwiązanie 1
def delete_nth(order, max_e):
    result = []
    occurrences = {}

    for motif in order:
        if motif not in occurrences:
            occurrences[motif] = 1
            result.append(motif)
        elif occurrences[motif] < max_e:
            occurrences[motif] += 1
            result.append(motif)

    return result


# Rozwiązanie 2
def delete_nth(order, max_e):
    result = []
    occurrences = {}

    for motif in order:
        count_motif = order.count(motif)

        if count_motif <= max_e:
            result.append(motif)
        elif count_motif not in occurrences:
            result.append(motif)
            occurrences[count_motif] = True

    return result


#####################################################################################
###############   ZADANIE 101     ###################################################
#####################################################################################


"""
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, 
there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'"""


# Rozwiązanie 1
def smash(words):
    sentence = (" ").join(words)
    return sentence


# Rozwiązanie 2
def smash(words):
    return " ".join(words)


#####################################################################################
###############   ZADANIE 102     ###################################################
#####################################################################################
"""In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats with decimal part non equal to zero are considered UNeven for this kata."""


# Rozwiązanie 1
def is_even(n):
    return False if n % 2 != 0 else True


# Rozwiązanie 2
def is_even(n):
    return n % 2 == 0


#####################################################################################
###############   ZADANIE 103     ###################################################
#####################################################################################
"""Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest

Example:

  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00


After 1st Year -->
  P = 1041.00
After 2nd Year -->
  P = 1083.86
After 3rd Year -->
  P = 1128.30
Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideratio
 that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.

"""


# Rozwiązanie
def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        year += 1

    return year


#####################################################################################
###############   ZADANIE 104     ###################################################
#####################################################################################
"""Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height of the cuboid.
 Write a function to help Bob with this calculation."""


# Rozwiązanie 1
def get_volume_of_cuboid(length, width, height):
    return length * width * height


# Rozwiązanie 2
import math


def get_volume_of_cuboid(length, width, height):
    length = float(length)
    width = float(width)
    height = float(float)

    if math.isnan(length) or math.isnan(width) or math.isnan(height):
        return 0

    elif length <= 0 or width <= 0 or height <= 0:
        return 0

    else:
        return length * width * height


#####################################################################################
###############   ZADANIE 105     ###################################################
#####################################################################################
"""As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1
10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

"""


# Rozwiązanie
def gimme(input_array):
    middle_value = sorted(input_array)[1]
    index_of_middle = input_array.index(middle_value)

    return index_of_middle


#####################################################################################
###############   ZADANIE 106     ###################################################
#####################################################################################
"""Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
Note: In COBOL, it should return "found the needle at position 6"

"""


def find_needle(haystack):
    try:
        needle_index = haystack.index("needle")
        return f"found the needle at position {needle_index}"
    except ValueError:
        return "needle not found in haystack"


#####################################################################################
###############   ZADANIE 107     ###################################################
#####################################################################################
"""Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

  ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
For example, if this array were passed as an argument:

 ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed.
 Note that all of the strings will be in the same case as those provided, and some elements may be repeated."""

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    geese_check = []
    for element in birds:
        if element not in geese:
            geese_check.append(element)

    return geese_check


#####################################################################################
###############   ZADANIE 108     ###################################################
#####################################################################################
"""When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement."""


# Rozwiązanie 1
def switch_it_up(number):
    variables = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for name, num in variables.items():
        if number < 0 and number * (-1) == num:
            return f"minus {name.capitalize()}"
        elif number == num:
            return name.capitalize()


# rozwiązanie 2
def switch_it_up(number):
    number_converter = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return number_converter[number]


#####################################################################################
###############   ZADANIE 109     ###################################################
#####################################################################################
"""Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)"""


# Rozwiązanie 1
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        return sum(range(begin_number, end_number + 1, step))


# Rozwiązanie 2
def sequence_sum(begin_number, end_number, step):
    return (
        0
        if begin_number > end_number
        else sum(range(begin_number, end_number + 1, step))
    )


#####################################################################################
###############   ZADANIE 110     ###################################################
#####################################################################################

#####################################################################################
###############   ZADANIE 111     ###################################################
#####################################################################################

#####################################################################################
###############   ZADANIE 112     ###################################################
#####################################################################################

#####################################################################################
###############   ZADANIE 113     ###################################################
#####################################################################################

#####################################################################################
###############   ZADANIE 114     ###################################################
#####################################################################################
