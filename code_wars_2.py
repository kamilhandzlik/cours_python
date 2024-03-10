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


#####################################################################################
###############   ZADANIE 106     ###################################################
#####################################################################################
