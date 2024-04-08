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
"""Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17"""


def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


#####################################################################################
###############   ZADANIE 111     ###################################################
#####################################################################################
"""Debugging sayHello function
The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

Example output:

Hello, Mr. Spock"""


def say_hello(name):
    return f"Hello, {name}"


#####################################################################################
###############   ZADANIE 112     ###################################################
#####################################################################################
"""Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"""


# rozwiązanie 1
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    sum = int(a) + int(b)
    return str(sum)


# rozwiązanie 2
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


#####################################################################################
###############   ZADANIE 113     ###################################################
#####################################################################################
"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"""


def domain_name(url):
    url = url.split("://")[-1]
    url = url.split("www.")[-1]
    domain = url.split(".")[0]
    return domain


#####################################################################################
###############   ZADANIE 114     ###################################################
#####################################################################################
"""Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0."""


def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)


#####################################################################################
###############   ZADANIE 115     ###################################################
#####################################################################################
"""Instructions
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]"""


def capitals(word):
    idx = []
    for i, letter in enumerate(word):
        if letter.isupper():
            idx.append(i)
    return idx


#####################################################################################
###############   ZADANIE 116     ###################################################
#####################################################################################
"""In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]"""


def reverse_list(l):
    return l[::-1]


#####################################################################################
###############   ZADANIE 117     ###################################################
#####################################################################################
"""Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.

number of hotdogs	price per unit (cents)
n < 5	100
n >= 5 and n < 10	95
n >= 10	90"""


# Rozwiązanie 1
def sale_hotdogs(n):
    if n <= 0:
        return 0
    elif n < 5:
        return 100 * n
    elif n < 10:
        return 95 * n
    else:
        return 90 * n


# Rozwiązanie 2
def sale_hotdogs(n):
    if n <= 0:
        return 0
    return n * (90 if n >= 10 else (95 if n >= 5 else 100))


#####################################################################################
###############   ZADANIE 118     ###################################################
#####################################################################################
"""You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers."""


# Rozwiązanie 1
def small_enough(array, limit):
    check = 0
    for value in array:
        if value <= limit:
            check += 1
        else:
            check -= 1

    if check == len(array):
        return True
    else:
        return False


# Rozwiązanie 2
def small_enough(array, limit):
    for value in array:
        if value > limit:
            return False
    return True


# Rozwiązanie 3
def small_enough(array, limit):
    return max(array) <= limit


#####################################################################################
###############   ZADANIE 119     ###################################################
#####################################################################################
"""Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number."""


def sum_mix(arr):
    return sum(int(x) for x in arr)


#####################################################################################
###############   ZADANIE 120     ###################################################
#####################################################################################
"""We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not. This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.

You only need to worry about english grammar rules for this kata, where anything that isn't singular (one of something), it is plural (not one of something).

All values will be positive integers or floats, or zero."""


# Rozwiązanie
def plural(n):
    return True if n > 1 or n == 0 else False


#####################################################################################
###############   ZADANIE 121     ###################################################
#####################################################################################
"""Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]"""


# Rozwiązanie
def greet(name):
    return f"Hello, {name} how are you doing today?"


#####################################################################################
###############   ZADANIE 122     ###################################################
#####################################################################################
"""Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade."""


def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3

    if 0 <= score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score <= 100:
        return "A"


#####################################################################################
###############   ZADANIE 123     ###################################################
#####################################################################################
"""Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more."""


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"


#####################################################################################
###############   ZADANIE 124     ###################################################
#####################################################################################
"""The purpose of this kata is to write a program that can do some algebra.

Write a function expand that takes in an expression with a single, one character variable, and expands it. The expression is
in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single character variable, and n is a natural number.
If a = 1, no coefficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, 
x is the original one character variable that was passed in the original expression and b, d, and f, are the powers that x is being
raised to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one, the coefficient should not be included.
If the coefficient of a term is -1, only the "-" should be included. If the power of the term is 0, only the coefficient should be included.
 If the power of the term is 1, the caret and power should be excluded."""


# To niestety jest jeszcze do dopacowania
def expand(expression):
    import re

    match = re.match(r"\((-?\d*)([a-zA-Z])([-+]?\d+)\)\^(\d+)", expression)
    a = int(match.group(1)) if match.group(1) else 1
    x = match.group(2)
    b = int(match.group(3))
    n = int(match.group(4))

    expanded_terms = []
    if n == 0:
        return "1"
    elif n == 1:
        if b == 0:
            return str(a) if a != 1 else x
        else:
            return str(a + b) + x if a + b != 1 else x
    else:
        for i in range(n + 1):
            coefficient = str((b**i) * (a ** (n - i)))
            power = str(n - i) if n - i > 1 else ""
            if coefficient != "0":
                if coefficient == "1" or coefficient == "-1":
                    coefficient = "" if power != "" else coefficient
                if coefficient != "":
                    if coefficient == "1" and power == "":
                        expanded_terms.append(x)
                    elif coefficient == "-1" and power == "":
                        expanded_terms.append("-" + x)
                    else:
                        expanded_terms.append(
                            coefficient + x + ("^" + power if power != "" else "")
                        )
    return "+".join(expanded_terms)


#####################################################################################
###############   ZADANIE 125     ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 126     ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 127     ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 128     ###################################################
#####################################################################################
