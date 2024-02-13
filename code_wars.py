#####################################################################################
###############   ZADANIE 1      ####################################################
#####################################################################################

# from preloaded import MORSE_CODE

MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}


def decode_morse(morse_code):
    morse_code = morse_code.strip()  # Remove leading and trailing whitespaces
    morse_words = morse_code.split("   ")  # Split the Morse code into words

    decoded_words = []
    for word in morse_words:
        morse_chars = word.split(" ")  # Split the Morse word into characters
        decoded_word = "".join(
            [
                key
                for char in morse_chars
                for key, value in MORSE_CODE.items()
                if value == char
            ]
        )
        decoded_words.append(decoded_word)

    decoded_sentence = " ".join(decoded_words)
    return decoded_sentence


# Example usage:
morse_code_input = "... --- ..."
decoded_string = decode_morse(morse_code_input)
print(decoded_string)

#####################################################################################
###############   ZADANIE 2      ####################################################
#####################################################################################
# Write a function that will return the count of distinct case-insensitive alphabetic characters and
# numeric digits that occur more than once in the input string. The input string can be assumed to
# contain only alphabets (both uppercase and lowercase) and numeric digits.


from ast import Index


def duplicate_count(text):
    # Your code goes here
    count = 0
    seen_chars = set()

    for char in text.lower():
        if char.isalnum() and text.lower().count(char) > 1 and char not in seen_chars:
            count += 1
            seen_chars.add(char)

    return count


text = "aabfbbsbdbs165131"

print(duplicate_count(text))

#####################################################################################
###############   ZADANIE 3      ####################################################
#####################################################################################


# Create a function that returns the sum of the two lowest positive numbers given an array
#  of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
# [10, 343445353, 3453445, 3453545353453] should return 3453455.


def sum_two_smallest_numbers(numbers):
    # Your code here
    if len(numbers) < 4:
        raise ValueError("Input list should have at least 4 positive integers.")

    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Sum the two smallest numbers
    sum_of_two = sum(sorted_numbers[:2])

    return sum_of_two


# Example usage:
numbers = [19, 5, 42, 2, 77]
result = sum_two_smallest_numbers(numbers)
print(result)


#####################################################################################
###############   ZADANIE 4      ####################################################
#####################################################################################

# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8


def row_sum_odd_numbers(n):
    # your code here
    return n**3


# mój poboczny eksperymrnt żeby zobaczyć so będzie większe
n = 9
x = n**n
current = 1
count = 1

while current < n:
    count *= current
    current += 1


solution = x > count
print(x)
print(count)
print(solution)

#####################################################################################
###############   ZADANIE 5      ####################################################
#####################################################################################


def is_isogram(string):
    # your code
    # Convert the string to lowercase to ignore letter case
    string = string.lower()

    # Check if the length of the set of characters is equal to the length of the string
    return len(set(string)) == len(string)


# Examples:
print(is_isogram("Dermatoglyphics"))  # Output: True
print(is_isogram("aba"))  # Output: False
print(is_isogram("moOse"))  # Output: False

#####################################################################################
###############   ZADANIE 6      ####################################################
#####################################################################################


def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in sentence.split(""):
        for vowel in vowels:
            if letter == vowel:
                count += 1
    return count


#####################################################################################
###############   ZADANIE 6      ####################################################
#####################################################################################


def solution(number):
    if number < 0:
        return 0  # Return 0 for negative numbers

    count = 0
    for j in range(number):
        if j % 3 == 0 or j % 5 == 0:
            count += j

    return count


# drugie rozwiązanie
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


#####################################################################################
###############   ZADANIE 6      ####################################################
#####################################################################################


def count_smileys(arr):
    sf = ":;-~)D"
    count = 0
    if sf in arr:
        count += 1 / 2


#####################################################################################
###############   ZADANIE 7      ####################################################
#####################################################################################


def cakes(recipe, available):
    number_of_cakes = float("inf")  # Set initially to positive infinity

    for ingredient, amount_required in recipe.items():
        if ingredient in available:
            cakes_possible = available[ingredient] // amount_required
            number_of_cakes = min(number_of_cakes, cakes_possible)
        else:
            return 0  # If any ingredient is missing, return 0 cakes

    return number_of_cakes


# Examples
print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)
# Output: 2

print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)
# Output: 0

# Tutaj spróbuje zrobić list comprihension


def cakes(recipe, available):
    return min(
        [
            available[ingredient] // amount_required if ingredient in available else 0
            for ingredient, amount_required in recipe.items()
        ],
        default=float("inf"),
    )


# Examples
print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)
# Output: 2

print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)


#####################################################################################
###############   ZADANIE 8      ####################################################
#####################################################################################

# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

# This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.


def narcissistic(value):
    num_digits = len(str(value))
    narc_num = 0
    temp_value = value

    while temp_value > 0:
        digit = temp_value % 10
        narc_num += digit**num_digits
        temp_value //= 10

    return narc_num == value


# Test cases
print(narcissistic(153))  # True
print(narcissistic(1652))  # False


#####################################################################################
###############   ZADANIE 8      ####################################################
#####################################################################################

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


def count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


# Test case
print(count("aba"))
print(count(""))

#####################################################################################
###############   ZADANIE 9      ####################################################
#####################################################################################

# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.


# rozwiązanie 1
def paperwork(n, m):
    k = 0
    if n < 0 or m < 0:
        n, m = 0, 0
    else:
        k = n * m
    return k


# rozwiązanie 2
def paperwork(n, m):
    return max(n * m, 0) if n >= 0 and m >= 0 else 0


# Testy
print(paperwork(5, 10))  # Oczekiwane: 50
print(paperwork(-5, 10))  # Oczekiwane: 0
print(paperwork(5, -10))  # Oczekiwane: 0
print(paperwork(-5, -10))  # Oczekiwane: 0

#####################################################################################
###############   ZADANIE 10      ####################################################
#####################################################################################

# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.


def binary_array_to_number(arr):
    decimal_num = int("".join(map(str, arr)), 2)
    return decimal_num


# Przykłady użycia
binary_array1 = [1, 0, 1, 0, 1]
binary_array2 = [1, 1, 0, 0, 1]

result1 = binary_array_to_number(binary_array1)
result2 = binary_array_to_number(binary_array2)

print(result1)  # Oczekiwane: 21
print(result2)  # Oczekiwane: 25
#####################################################################################
###############   ZADANIE 11      ####################################################
#####################################################################################

# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in


def century(year):
    # Calculate the century using integer division
    century_num = (year - 1) // 100 + 1
    return century_num


# Examples
print(century(1705))  # Expected output: 18
print(century(1900))  # Expected output: 19
print(century(2000))  # Expected output: 20
print(century(2001))  # Expected output: 21

#####################################################################################
###############   bonus      ####################################################
#####################################################################################

# Szpanersko napisane "hello world!"


def greet():
    binDict = {
        "0b1000001": "0110000101100011011001010111010001111001011011000110001101101000011011110110110001101001011011100110010101110011011101000110010101110010011000010111001101100101",
        "0b1000010": "0110001001110101011000110110101101101101011010010110111001110011011101000110010101110010011001100111010101101100011011000110010101110010011001010110111001100101",
        "0b1000011": "0110001101101000011011000110111101110010011011110110011001101100011101010110111101110010011011110110110101100101011101000110100001100001011011100110010101110011",
        "0b1000100": "0110010001100101011010010110111001110011011101000110100101110100011101010111010001101001011011110110111001100001011011000110100101111010011010010110111001100111",
        "0b1000101": "0110011001101111011100100110010101110100011010000110111101110101011001110110100001110100011001100111010101101100011011100110010101110011011100110110010101110011",
        "0b1000110": "011001000110100101110011011101000110100101101110011001110111010101101001011100110110100000100000011000010110001001101001011011000110100101110100011010010110010101110011",
        "0b1000111": "011100110111010001110010011000010110100101100111011010000111010001100110011011110111001001110111011000010111001001100100011011100110010101110011011100110110010101110011",
        "0b1001000": "011011010111010101101100011101000110100101100100011010010110110101100101011011100111001101101001011011110110111001100001011011000110100101110100011010010110010101110011",
        "0b1001001": "011010010110110101101101011101010110111001101111011001010110110001100101011000110111010001110010011011110111000001101000011011110111001001100101011101000110100101100011",
        "0b1001010": "011100000110100001101111011101000110111101110000011010000110111101110011011100000110100001101111011100100111100101101100011000010111010001101001011011110110111001110011",
        "0b1001011": "011100000110100001101111011100110111000001101000011011110110011101101100011110010110001101100101011100100110000101101100011001000110010101101000011110010110010001100101",
        "0b1001100": "01110000011100110111100101100011011010000110111101110100011010000110010101110010011000010111000001100101011101010111010001101001011000110110000101101100011011000111100100100001",
    }
    sR = ""
    posRefL = [7, 9, 7, 14, 6, 11, 11, 12, 16, 14, 19, 21]
    for i in range(65, 77):
        sR += binDropper(binDict[binDropper(chr(i))], True)[posRefL[i - 65]]
    return sR


def binDropper(pL, ship=False):
    if ship:
        return int(pL, 2).to_bytes((int(pL, 2).bit_length() + 7) // 8, "big").decode()
    return bin(int.from_bytes(pL.encode(), "big"))


print(greet())

# jak to działa

# Funkcja greet:

# binDict to słownik, gdzie klucze to binarne reprezentacje wartości ASCII ('0b1000001', '0b1000010', ..., '0b1001100'), a wartości to odpowiadające im ciągi binarne.

# posRefL to lista liczb całkowitych reprezentujących pozycje, z których będą pobierane znaki z ciągów binarnych.

# Funkcja iteruje po wartościach ASCII od 65 do 76 (odpowiadających literom 'A' do 'L') przy użyciu pętli for i in range(65, 77). W każdej iteracji konwertuje wartość ASCII na znak (chr(i)) i używa go jako klucza do uzyskania odpowiadającego ciągu binarnego z binDict.

# Następnie funkcja przekazuje uzyskany ciąg binarny do funkcji binDropper, która wyciąga konkretny znak na podstawie określonych pozycji zdefiniowanych w posRefL. Wyciągnięte znaki są konkatenowane, tworząc ostateczny ciąg sR.

# Ostateczny ciąg sR jest zwracany.

# Funkcja binDropper:

# Jeśli ship jest True, konwertuje ciąg binarny pL na liczbę całkowitą, następnie konwertuje tę liczbę na bajty, a ostatecznie dekoduje bajty na ciąg znaków. W zasadzie dokonuje konwersji danych binarnych na ciąg znaków.

# Jeśli ship jest False, konwertuje wejściowy ciąg znaków pL na bajty, a następnie konwertuje te bajty na reprezentację binarną.

# Instrukcja print(greet()) wywołuje funkcję greet i drukuje uzyskany ciąg znaków.

# Ogólnie rzecz biorąc, kod wydaje się być kreatywnym sposobem kodowania wiadomości przy użyciu ciągów binarnych i wyciągania konkretnych znaków na podstawie wcześniej zdefiniowanych pozycji. Funkcja binDropper służy do obsługi

# konwersji z binarnego na tekstowy i odwrotnie. Funkcja greet wykorzystuje te konwersje do stworzenia konkretnej zakodowanej wiadomości na podstawie wartości ASCII i pozycji.


#####################################################################################
###############   ZADANIE 12      ####################################################
#####################################################################################

# sposób 1 nie do końca poprawny ponieważ nie działa na 3
from math import sqrt


def is_square(n):
    is_sq = False
    # sprawdza czy pierwiastek drugiego stopnia jest intigerem tylko, że bardzo łopatologicznie
    if n < 0:
        is_sq = "Negative numbers cannot be square numbers"
    elif sqrt(n) is not float:
        is_sq = True
    else:
        is_sq = False
    return is_sq


print(is_square(3))

# Sposób 2 ten już działa perfekcyjnie na wszystko

import math


def is_square(n):
    # sprawdza czy pierwiastek drugiego stopnia jest intigerem
    return n > 0 and math.isqrt(n) ** 2 == n


#####################################################################################
###############   ZADANIE 13      ####################################################
#####################################################################################
# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
#  In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]

        result = ""
        for numeral, value in roman_numerals:
            while val >= value:
                result += numeral
                val -= value

        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(roman_num)):
            if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i - 1]]:
                result += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i - 1]]
            else:
                result += roman_dict[roman_num[i]]

        return result


# Examples
print(RomanNumerals.to_roman(1990))  # Expected output: 'MCMXC'
print(RomanNumerals.to_roman(2008))  # Expected output: 'MMVIII'
print(RomanNumerals.from_roman("MCMXC"))  # Expected output: 1990
print(RomanNumerals.from_roman("MMVIII"))  # Expected output: 2008


# to_roman(val: int) -> str:

# to_roman przyjmuje liczbę całkowitą val i zamienia ją na reprezentację liczby rzymskiej. Do tego celu używa listy
#  krotek roman_numerals, gdzie każda krotka zawiera parę: rzymski numeral (np. "M", "CM", "D") oraz odpowiadająca mu wartość liczby.

# Następnie, korzystając z pętli for, przechodzi przez listę roman_numerals od największego rzymskiego numerala do najmniejszego.
#  W każdym kroku sprawdza, ile razy można odjąć daną wartość od val, dodaje odpowiadający rzymski numeral do wyniku i odejmuje odpowiednią ilość od val.
# Proces ten powtarza się do momentu, gdy val staje się równy 0.

# Ostatecznie zwraca zbudowany rzymski numeral jako string.

# from_roman(roman_num: str) -> int:

# from_roman przyjmuje rzymski numeral jako string roman_num i zamienia go na liczbę całkowitą. W tym celu korzysta z mapy roman_dict, gdzie każdemu rzymskiemu numeralowi przypisana jest jego wartość liczby.

# Następnie przechodzi przez każdy znak rzymskiego numerala używając pętli for. Jeżeli wartość liczby odpowiadającej aktualnemu znakowi jest większa niż wartość liczby odpowiadającej poprzedniemu znakowi, to odejmuje dwukrotność wartości poprzedniego znaku (uwzględniając notację odjęcia) od wyniku. W przeciwnym razie dodaje wartość liczby odpowiadającej aktualnemu znakowi do wyniku.

# Ostatecznie zwraca uzyskaną liczbę całkowitą.


#####################################################################################
###############   ZADANIE 14      ###################################################
#####################################################################################
"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases."""


# rozwiązanie 1 - to działa w wersji konsolowej
def likes(names):
    if len(names) == 0:
        print("no one likes this")
    elif len(names) == 1:
        print(f"{names[0]} likes this")
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3:
        print(f"{names[0]}, {names[1]}, and {names[2]} like this")
    else:
        print(f"{names[0]}, {names[1]}, and {len(names) - 2} others like this")


# rozwiązanie 2 - to działa tak żebby zaliczyć katę na codewars
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# Example usage:
likes(["Alice"])
likes(["Bob", "Charlie"])
likes(["Dave", "Eve", "Frank"])
likes(["Grace", "Hank", "Ivy", "Jack"])


#####################################################################################
###############   ZADANIE 15      ###################################################
#####################################################################################

"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""


def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num


# Examples
print(find_it([7]))  # Output: 7
print(find_it([0]))  # Output: 0
print(find_it([1, 1, 2]))  # Output: 2
print(find_it([0, 1, 0, 1, 0]))  # Output: 0
print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  # Output: 4

# This find_it function iterates through each element in the input sequence (seq) and checks
# if the count of that element in the sequence is odd. If so, it returns that element. This way, it
#  finds the integer that appears an odd number of times in the given array.


#####################################################################################
###############   ZADANIE 16      ###################################################
#####################################################################################
"""Turn boolean to string"""


def boolean_to_string(b):
    return str(b)


#####################################################################################
###############   ZADANIE 17      ###################################################
#####################################################################################

"""Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flower
s has an even number of petals and the other has an odd number of petals it means they are in love.
Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't."""


# Rozwiązanie 1
def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 0 or (flower1 % 2 != 0 and flower2 % 2 != 0):
        return False
    elif (flower1 % 2 != 0 and flower2 % 2 == 0) or (
        flower1 % 2 == 0 and flower2 % 2 != 0
    ):
        return True


# Rozwiązaanie 2
def lovefunc(flower1, flower2):
    # Check if one flower has even petals and the other has odd petals
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (
        flower1 % 2 != 0 and flower2 % 2 == 0
    ):
        return True  # They are in love
    else:
        return False  # They aren't in love


# Rozwiązanie 3
def lovefunc(f1, f2):
    return (
        True
        if (f1 % 2 == 0 and f2 % 2 != 0) or (f2 % 2 == 0 and f1 % 2 != 0)
        else False
    )


# Rozwiązanie 4
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2


#####################################################################################
###############   ZADANIE 18      ###################################################
#####################################################################################
"""Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:"""


def litres(time):
    return time // 2


#####################################################################################
###############   ZADANIE 19      ###################################################
#####################################################################################
"""We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):"""


def number_to_string(num):
    return str(num)


#####################################################################################
###############   ZADANIE 20      ###################################################
#####################################################################################
"""Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds."""


# rozwiązanie 1
def format_duration(seconds):
    if seconds == 0:
        return "now"

    years, seconds = divmod(seconds, 31536000)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    time_units = [
        ("year", years),
        ("day", days),
        ("hour", hours),
        ("minute", minutes),
        ("second", seconds),
    ]
    result = []

    for unit, value in time_units:
        if value == 1:
            result.append(f"{value} {unit}")
        elif value > 1:
            result.append(f"{value} {unit}s")

    return (
        ", ".join(result[:-1]) + " and " + result[-1] if len(result) > 1 else result[0]
    )


# Example usage:
print(format_duration(3662))  # Output: "1 hour, 1 minute and 2 seconds"
print(format_duration(0))  # Output: "now"

"""This code takes a number of seconds as input and converts it into a human-readable format, expressing the duration in years, days,
 hours, minutes, and seconds. The function handles singular and plural forms appropriately and returns the formatted string."""


# Rozwiązanie 2

times = [
    ("year", 365 * 24 * 60 * 60),
    ("day", 24 * 60 * 60),
    ("hour", 60 * 60),
    ("minute", 60),
    ("second", 1),
]


def format_duration(seconds):
    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return (
        ", ".join(chunks[:-1]) + " and " + chunks[-1] if len(chunks) > 1 else chunks[0]
    )


#####################################################################################
###############   ZADANIE 21      ###################################################
#####################################################################################

"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!"""


# first attempt - it does not work as solution in code wars
def square_digits(num):
    for i in str(num):
        square_digit = str(int(i) ** 2)
    result = int("".join(square_digit))
    return result


# second attmpt - it does work as solution in code wars
def square_digits(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)

    # Use a list comprehension to square each digit and concatenate
    squared_digits = [str(int(digit) ** 2) for digit in num_str]

    # Join the squared digits and convert back to an integer
    result = int("".join(squared_digits))

    return result


# Test cases
print(square_digits(9119))  # Output: 811181
print(square_digits(765))  # Output: 493625

#####################################################################################
###############   ZADANIE 22      ###################################################
#####################################################################################

"""Consider an array/list of sheep where some sheep may be missing from their place.
 We need a function that counts the number of sheep present in the array (true means present)."""


# Rozwiązanie 1 - it does work as solution in code wars
def count_sheeps(sheep):
    for i in sheep:
        if i != (True or False):
            i = 0
        elif i == (True or False):
            i = sheep.count(True)
    result = i
    return result


# Rozwiązanie 2 - it does work as solution in code wars
def count_sheeps(sheep):
    return sheep.count(True)


sheep = [
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    True,
]
result = count_sheeps(sheep)
print(result)

#####################################################################################
###############   ZADANIE 23      ###################################################
#####################################################################################

"""Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers."""


def dig_pow(n, p):
    # Convert the number n to a list of its digits
    digits = [int(digit) for digit in str(n)]

    # Calculate the sum of consecutive powers
    power_sum = sum([digit ** (p + i) for i, digit in enumerate(digits)])

    # Check if there is an integer k such that power_sum = n * k
    if power_sum % n == 0:
        return power_sum // n  # Return k
    else:
        return -1  # No such k exists


# Test cases
print(dig_pow(89, 1))  # Output: 1
print(dig_pow(695, 2))  # Output: 2
print(dig_pow(46288, 3))  # Output: 51
print(dig_pow(92, 1))  # Output: -1 (

#####################################################################################
###############   ZADANIE 24      ###################################################
#####################################################################################


"""There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop."""


def number_of_people(bus_stops):
    # Calculate the net change in the number of people at each bus stop
    net_change = [stop[0] - stop[1] for stop in bus_stops]

    # Return the sum of the net changes, representing the remaining people on the bus
    return sum(net_change)


# Test cases
bus_stops_1 = [(10, 0), (3, 5), (5, 8)]
bus_stops_2 = [(5, 0), (2, 2), (7, 3)]

print(number_of_people(bus_stops_1))  # Output: 5
print(number_of_people(bus_stops_2))  # Output: 10

#####################################################################################
###############   ZADANIE 25      ###################################################
#####################################################################################
"""Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]"""


# Rozwiązanie 1
def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        # Calculate the number of spaces and asterisks for each floor
        spaces = " " * (n_floors - i - 1)
        asterisks = "*" * (2 * i + 1)
        # Combine spaces and asterisks to form a floor and add it to the tower
        floor = spaces + asterisks + spaces
        tower.append(floor)
    return tower


# Test cases
tower_3_floors = tower_builder(3)
tower_6_floors = tower_builder(6)

print(tower_3_floors)
print(tower_6_floors)


# Rozwiązanie 2
def tower_builder(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


#####################################################################################
###############   ZADANIE 26      ###################################################
#####################################################################################

"""Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

"""


# Rozwiązanie 1
def even_or_odd(number):
    i = number
    if i % 2 != 0:
        return "Odd"
    elif i % 2 == 0:
        return "Even"


# Rozwiąznie 2
def even_or_odd(number):
    return "Odd" if number % 2 != 0 else "Even"


#####################################################################################
###############   ZADANIE 27      ###################################################
#####################################################################################

"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""


# Rozwiązanie 1
def validate_pin(pin):
    if (len(pin) == 6 or len(pin) == 4) and pin.isdigit():
        return True
    else:
        return False


# Rozwiązanie 2
def validate_pin(pin):
    return (len(pin) == 6 or len(pin) == 4) and pin.isdigit()


#####################################################################################
###############   ZADANIE 28      ###################################################
#####################################################################################

"""There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!"""


# Rozwiązanie 1
def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    if your_points > average:
        return True
    else:
        return False


# Rozwiązanie 2


def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return True if your_points > average else False


# Rozwiązanie 3
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


# Rozwiązanie 4
import statistics


def better_than_average(class_points, your_points):
    return your_points > statistics.mean(class_points)


#####################################################################################
###############   ZADANIE 29      ###################################################
#####################################################################################

"""Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element i
s sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array."""


def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []

    positive_count = sum(1 for num in arr if num > 0)
    negative_sum = sum(num for num in arr if num < 0)

    return [positive_count, negative_sum]


result_1 = count_positives_sum_negatives([1, -2, 3, 4, 0])
result_2 = count_positives_sum_negatives([-1, -2, -3, -4, 0])
result_3 = count_positives_sum_negatives([])

print(result_1)  # Output: [3, -2]
print(result_2)  # Output: [0, -10]
print(result_3)  # Output: []

#####################################################################################
###############   ZADANIE 30      ###################################################
#####################################################################################

"""Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"""


# Rozwiązanie 1
def longest(a1, a2):
    s1 = "".join(a1 + a2)
    s2 = "".join(sorted(set(s1)))
    return s2


# Rozwiązanie 2
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


"""was tested through this code which I for some reason find very clever 
import codewars_test as test
    
@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        test.assert_equals(longest("lordsofthefallen", "gamekult"), "adefghklmnorstu")
        test.assert_equals(longest("codewars", "codewars"), "acdeorsw")
        test.assert_equals(longest("agenerationmustconfrontthelooming", "codewarrs"), "acdefghilmnorstuw")

from random import randint

@test.describe("longest")
def random_tests():
    #-----------------
    def do_ex(k):
        i, res = 0, ""
        while (i < 15):
            res += chr(randint(97+k, 122)) * randint(1, 10)
            i += 1
        return res
    def longest_sol(a1, a2):
        return "".join(sorted(set(a1 + a2)))
    #-----------------
    @test.it("Random tests")
    def random():
        for _ in range(0, 200):
            s1 = do_ex(randint(0, 10))
            s2 = do_ex(randint(0, 8))
            sol = longest_sol(s1, s2)
            test.assert_equals(longest(s1, s2), sol)
"""

#####################################################################################
###############   ZADANIE 31      ###################################################
#####################################################################################

"""It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
 You're given one parameter, the original string.
 You don't have to worry about strings with less than two characters."""


# Rozwiązanie 1
def remove_char(s):
    return s[1:-1]


#####################################################################################
###############   ZADANIE 32      ###################################################
#####################################################################################

"""Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"""


def bmi(weight, height):
    bmi = weight / (height**2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"


#####################################################################################
###############   ZADANIE 33      ###################################################
#####################################################################################

"""Our football team has finished the championship.

Our team's match results are recorded in a collection of strings.
 Each match is represented by a string in the format "x:y",
 where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points
 our team (x) got in the championship by the rules given above."""


def points(games):
    result_x = 0
    result_y = 0

    for match in games:
        x, y = map(int, match.split(":"))

        if x > y:
            result_x += 3
        elif x < y:
            result_y += 3
        else:
            result_x += 1
            result_y += 1

    return result_x


# Przykład użycia:
match_results = ["3:1", "2:2", "0:1"]
total_points = points(match_results)
print(f"Total points: {total_points}")

#####################################################################################
###############   ZADANIE 34      ###################################################
#####################################################################################

"""You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the opportunity
to go for a short walk. The city provides its citizens with a Walk Generating App on their
phones -- everytime you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block
 for each letter (direction) and you know it takes you one minute to traverse one city block, so create
 a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
 and will, of course, return you to your starting point. Return false otherwise."""


# Rozwiązanie 1 - działa ale nie dokońca
def is_valid_walk(walk):
    directions = ["n", "s", "e", "w"]
    time = 0
    for direction in directions:
        for direction in walk:
            time += 1
            if (direction in walk) != 0 or time != 10:
                return False
            else:
                return True


# Rozwiązanie 2 - działa wpełni
def is_valid_walk(walk):
    if len(walk) != 10:  # Sprawdzamy, czy ilość kroków wynosi dokładnie 10
        return False

    # Sprawdzamy, czy dla każdego kierunku mamy przeciwny kierunek
    return walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")


# Rozwiązanie 3
def isValidWalk(walk):
    return (
        len(walk) == 10
        and walk.count("n") == walk.count("s")
        and walk.count("e") == walk.count("w")
    )


# Przykład użycia:
example_walk = ["n", "s", "e", "w", "n", "s", "e", "w", "n", "s"]
result = is_valid_walk(example_walk)
print(result)

#####################################################################################
###############   ZADANIE 35      ###################################################
#####################################################################################

"""In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them"""


def parse_int(s):
    # Define a dictionary to map words to their numeric values
    word_to_num = {
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
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
    }

    # Split the input string into words
    words = s.replace("-", " ").replace(" and ", " ").split()

    # Initialize variables to track the result
    result = 0
    current_number = 0

    # Process each word in the input string
    for word in words:
        # Convert the word to its numeric value
        num = word_to_num[word]

        # Update the result based on the current word
        if num == 100:
            current_number *= num
        elif num == 1000 or num == 1000000:
            result += current_number * num
            current_number = 0
        else:
            current_number += num

    # Add the last current_number to the result
    result += current_number

    return result


# Examples
print(parse_int("one"))  # Output: 1
print(parse_int("twenty"))  # Output: 20
print(parse_int("two hundred forty-six"))  # Output: 246
print(
    parse_int("seven hundred eighty-three thousand nine hundred and nineteen")
)  # Output: 783919

#####################################################################################
###############   ZADANIE 36      ###################################################
#####################################################################################

"""Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link."""


def validate_battlefield(field):
    # Define the counts of ships of different sizes
    ship_counts = {4: 1, 3: 2, 2: 3, 1: 4}

    # Helper function to check if a ship of given size can be placed at a specific position
    def can_place_ship(size, row, col, direction):
        if direction == "horizontal":
            for i in range(size):
                if field[row][col + i] != 0:
                    return False
        else:  # direction == 'vertical'
            for i in range(size):
                if field[row + i][col] != 0:
                    return False
        return True

    # Helper function to mark cells occupied by a ship
    def mark_ship(size, row, col, direction):
        if direction == "horizontal":
            for i in range(size):
                field[row][col + i] = 1
        else:  # direction == 'vertical'
            for i in range(size):
                field[row + i][col] = 1

    # Iterate through the field and validate ships
    for row in range(10):
        for col in range(10):
            if field[row][col] == 1:
                for size in ship_counts:
                    if ship_counts[size] > 0:
                        if can_place_ship(size, row, col, "horizontal"):
                            mark_ship(size, row, col, "horizontal")
                            ship_counts[size] -= 1
                            break
                        elif can_place_ship(size, row, col, "vertical"):
                            mark_ship(size, row, col, "vertical")
                            ship_counts[size] -= 1
                            break
                        else:
                            return False

    # Check if all ships are placed
    return all(count == 0 for count in ship_counts.values())


# Example usage:
battleship_field = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print(validate_battlefield(battleship_field))  # Output: True

#####################################################################################
###############   ZADANIE 37      ###################################################
#####################################################################################


# Rozwiązanie 1 - niedziała tylko na tym jednym sprawdzeniu poniżej
def solution(text, ending):
    return True if ending in text else False


"""Incorrect answer for:
    text = 'samurai'
  ending = 'ra'
Assertion failed: True should equal False"""


# Rozwiązanie 2
def solution(string, ending):
    return ending in string[-len(ending) :]


# Rozwiązanie 3
def solution(text, ending):
    return text.endswith(ending)


print(solution("abc", "bc"))  # Output: True
print(solution("abc", "d"))  # Output: False
print(solution("samurai", "ra"))  # Output: True


#####################################################################################
###############   ZADANIE 38      ###################################################
#####################################################################################

"""Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output."""


# Rozwiązanie 1
def friend(x):
    fren_list = []
    for i in x:
        if len(i) == 4:
            fren_list.append(i)
    return fren_list


# Rozwiązanie 2
def friend(x):
    return [friend for friend in x if len(friend) == 4]


#####################################################################################
###############   ZADANIE 39      ###################################################
#####################################################################################
"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)"""


# Rozwiązanie
def persistence(num):
    if num < 10:
        return 0

    count = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        count += 1

    return count


# Example usage:
# print(persistence(39))  # Output: 3
# print(persistence(999))  # Output: 4
# print(persistence(4))  # Output: 0


#####################################################################################
###############   ZADANIE 40      ###################################################
#####################################################################################

"""Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7"""


# Rozwiązanie 1 - Przyznaję po najprostszej linii oporu ale od czegoś trzeba wyjść :D
def basic_op(operator, value1, value2):
    solution = 0
    if operator == "+":
        solution = value1 + value2
        return solution
    elif operator == "-":
        solution = value1 - value2
        return solution
    elif operator == "*":
        solution = value1 * value2
        return solution
    elif operator == "**":
        solution = value1 / value2
        return solution
    elif operator == "/":
        solution = value1 / value2
        return solution
    elif operator == "//":
        solution = value1 / value2
        return solution
    elif operator == "%":
        solution = value1 % value2
        return solution


# Rozwiązanie 2
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


"""WAŻNE MOŻE SIĘ KIEDYŚ PRZYDAĆ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
The eval function in Python is a built-in function that evaluates
a string as a Python expression. In this case, the basic_op function
uses eval to dynamically construct a string representing
a mathematical expression and then evaluates it to obtain the result."""

#####################################################################################
###############   ZADANIE 41      ###################################################
#####################################################################################
"""A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)"""


# Rozwiązanie
def hero(bullets, dragons):
    return True if bullets >= dragons * 2 else False


#####################################################################################
###############   ZADANIE 42      ###################################################
#####################################################################################
"""Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'"""


# Rozwiązanie 1
def solution(string):
    rev_str = string[::-1]
    return rev_str


# Rozwiązanie 2
def solution(string):
    return string[::-1]


#####################################################################################
###############   ZADANIE 43      ###################################################
#####################################################################################
"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))"""


# Rozwiązanie 2
def zero(func=None):
    return 0 if func is None else func(0)


def one(func=None):
    return 1 if func is None else func(1)


def two(func=None):
    return 2 if func is None else func(2)


def three(func=None):
    return 3 if func is None else func(3)


def four(func=None):
    return 4 if func is None else func(4)


def five(func=None):
    return 5 if func is None else func(5)


def six(func=None):
    return 6 if func is None else func(6)


def seven(func=None):
    return 7 if func is None else func(7)


def eight(func=None):
    return 8 if func is None else func(8)


def nine(func=None):
    return 9 if func is None else func(9)


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: x // num


# Rozwiązanie 2
def identity(a):
    return a


def zero(f=identity):
    return f(0)


def one(f=identity):
    return f(1)


def two(f=identity):
    return f(2)


def three(f=identity):
    return f(3)


def four(f=identity):
    return f(4)


def five(f=identity):
    return f(5)


def six(f=identity):
    return f(6)


def seven(f=identity):
    return f(7)


def eight(f=identity):
    return f(8)


def nine(f=identity):
    return f(9)


def plus(b):
    return lambda a: a + b


def minus(b):
    return lambda a: a - b


def times(b):
    return lambda a: a * b


def divided_by(b):
    return lambda a: a // b


# Examples
# print(seven(times(five())))       # Output: 35
# print(four(plus(nine())))          # Output: 13
# print(eight(minus(three())))       # Output: 5
# print(six(divided_by(two())))       # Output: 3


#####################################################################################
###############   ZADANIE 45      ###################################################
#####################################################################################
"""Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"""


# Rozwiązanie 1
def DNA_strand(dna):
    sec_strand = ""
    for i in dna:
        if i == "A":
            sec_strand += "T"
        elif i == "T":
            sec_strand += "A"
        elif i == "C":
            sec_strand += "G"
        elif i == "G":
            sec_strand += "C"

    return sec_strand


# Rozwiązanie 2
def DNA_strand(dna):
    complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement_strand = "".join(complement_dict[n] for n in dna)
    return complement_strand


# Examples
# print(DNA_strand("ATTGC"))  # Output: "TAACG"
# print(DNA_strand("GTAT"))   # Output: "CATA"

#####################################################################################
###############   ZADANIE 46      ###################################################
#####################################################################################
"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"""


# Rozwiązanie 1
def get_middle(s):
    length = len(s)

    if length % 2 == 1:
        mid = length // 2
        result = s[mid]

    else:
        mid1 = length // 2 - 1
        mid2 = length // 2
        result = s[mid1 : mid2 + 1]

    return result


# Rozwiązanie 2

#####################################################################################
###############   ZADANIE 47      ###################################################
#####################################################################################
"""Write function RemoveExclamationMarks which removes all exclamation marks from a 
given string."""


# Rozwiązanie 1
def remove_exclamation_marks(s):
    if len(s) > 0:
        result = s.replace("!", "")
    else:
        result = s

    return result


# Rozwiązanie 2
def remove_exclamation_marks(s):
    return s.replace("!", "") if len(s) > 0 else s


# Rozwiązanie 3
def remove_exclamation_marks(s):
    return s.replace("!", "")


#####################################################################################
###############   ZADANIE 48      ###################################################
#####################################################################################
"""Given a random non-negative number, you have to return the digits of this number 
within an array in reverse order."""


# Rozwiązanie 1 -  code wars nie przyjmuje takiego rozwiązania jako poprawne
def digitize(n):
    i = str(n)
    j = i[::-1]
    k = []
    k.append("".split)
    return j


# Rozwiązanie 2 - Te rozwiązanie już mu odpowiada
def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]


#####################################################################################
###############   ZADANIE 49      ###################################################
#####################################################################################
"""Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)"""


# Rozwiązanie 1
def summation(num):
    n = 0
    result = 0
    for i in range(num):
        n += 1
        result += n

    return result


# Rozwiązanie 2
def summation(num):
    return (num * (num + 1)) // 2


#####################################################################################
###############   ZADANIE 50      ###################################################
#####################################################################################
"""After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d)."""


# Rozwiązanie 1
def rental_car_cost(d):
    cash = 40
    if d >= 7:
        cash = d * 40 - 50
    elif d >= 3:
        cash = d * 40 - 20
    elif d > 1:
        d * 40

    return cash


# Rozwiązanie 2
def rental_car_cost(d):
    daily_rate = 40

    if d >= 7:
        return d * daily_rate - 50
    elif d >= 3:
        return d * daily_rate - 20
    else:
        return d * daily_rate


# Rozwiązanie 3
def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30


#####################################################################################
###############   ZADANIE 51      ###################################################
#####################################################################################
"""Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]"""


# Rozwiązanie 1
def string_to_array(s):
    if not s:
        return [""]

    words = s.split()
    return words


# Rozwiązanie 2
def string_to_array(s):
    return s.split(" ")


#####################################################################################
###############   ZADANIE 52      ###################################################
#####################################################################################
"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""


# Rozwiązanie
def grow(arr):
    result = 1
    for number in arr:
        result *= number
    return result


#####################################################################################
###############   ZADANIE 53      ###################################################
#####################################################################################
"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


# Rozwiązanie
def array_diff(a, b):
    return [x for x in a if x not in b]


#####################################################################################
###############   ZADANIE 54     ###################################################
#####################################################################################
"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""


def reverse_words(string):
    words = string.split(" ")
    reversed_words = [word[::-1] for word in words]
    reversed_string = " ".join(reversed_words)
    return reversed_string


#####################################################################################
###############   ZADANIE 55      ###################################################
#####################################################################################
"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"""


# Rozwiązanie 1
def high_and_low(numbers):
    a = numbers.split(" ")
    sol = []
    result = ""
    for i in a:
        j = int(i)
        sol.append(j)

    ma = max(sol)
    mi = min(sol)
    result = f"{str(ma)} {str(mi)}"

    return result


# Rozwiązanie 2
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    max_num = str(max(num_list))
    min_num = str(min(num_list))
    return f"{max_num} {min_num}"


#####################################################################################
###############   ZADANIE 56      ###################################################
#####################################################################################
"""In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0"""


# Rozwiązanie 1
def make_negative(number):
    return number * (-1) if number > 0 else number


# Rozwiązanie 2
def make_negative(number):
    return -abs(number)


#####################################################################################
###############   ZADANIE 57      ###################################################
#####################################################################################
"""Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of 
 , the cube above will have volume of 

  and so on until the top which will have a volume of 

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as 

 =m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45

findNb(91716553919377) --> -1"""


# Rozwiązanie
def find_nb(m):
    current = 0
    n = 1
    while current < m:
        current += n**3
        n += 1

    if current == m:
        return n - 1
    else:
        return -1


#####################################################################################
###############   ZADANIE 58      ###################################################
#####################################################################################
"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""


# Rozwiązanie
def high(x):
    alph = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    max_word = ""
    max_score = 0

    words = x.split()

    for word in words:
        current_score = sum(alph[letter] for letter in word)

        if current_score > max_score:
            max_score = current_score
            max_word = word

    return max_word


#####################################################################################
###############   ZADANIE 59      ###################################################
#####################################################################################
"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance."""


# Rozwiązanie 1
def find_uniq(arr):
    unique = set(arr)
    n = 0
    for i in unique:
        if arr.count(i) == 1:
            n += i
    return n


# Rozwiązanie 2
def find_uniq(arr):
    i, n = set(arr)
    return i if arr.count(i) == 1 else n


#####################################################################################
###############   ZADANIE 60      ###################################################
#####################################################################################
"""Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list."""


# Rozwiązanie 1
def invert(lst):
    result = []
    for i in lst:
        i *= -1
        result.append(i)
    return result


# Rozwiązanie 2
def invert(lst):
    return [i * -1 for i in lst]


#####################################################################################
###############   ZADANIE 61      ###################################################
#####################################################################################
"""You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

Example(Input1, Input2 --> Output):

6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if
 its length and width are equal, otherwise it is a rectangle"""


# Rozwiązanie 1
def area_or_perimeter(l, w):
    result = 0
    if l != w:
        result += 2 * l + 2 * w
    else:
        result += l**2

    return result


# Rozwiązanie 2
def area_or_perimeter(l, w):
    return (2 * l + 2 * w) if l != w else l**2


#####################################################################################
###############   ZADANIE 62      ###################################################
#####################################################################################
"""Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted). """


# Rozwiązanie 1
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# Rozwiązanie 2
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


#####################################################################################
###############   ZADANIE 63      ###################################################
#####################################################################################
"""You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0."""


# Rozwiązanie
def find_even_index(arr):
    for idx in range(len(arr)):
        if sum(arr[:idx]) == sum(arr[idx + 1 :]):
            return idx
    return -1


#####################################################################################
###############   ZADANIE 64      ###################################################
#####################################################################################
"""You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not."""


# Rozwiązanie 1
def check(a, x):
    if x in a:
        return True
    else:
        return False


# Rozwiązanie 2
def check(a, x):
    return True if x in a else False


# Rozwiązanie 3
def check(a, x):
    return x in a


#####################################################################################
###############   ZADANIE 65      ###################################################
#####################################################################################
"""Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero)."""


# Rozwiązanie 1
def odd_or_even(arr):
    a = sum(arr)
    if a % 2 != 0:
        return "odd"
    else:
        return "even"


# Rozwiązanie 2
def odd_or_even(arr):
    return "odd" if sum(arr) % 2 != 0 else "even"


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested."""


# Rozwiązanie 1
def other_angle(a, b):
    solution = 180 - (a + b)
    return solution


# Rozwiązanie 2
def other_angle(a, b):
    return 180 - (a + b)


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""Complete the method that takes a boolean value and return a "Yes" string for true,
 or a "No" string for false."""


# Rozwiązanie 1
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# Rozwiązanie 2
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whethe
r the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member
 is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared,
 regardless of the order."""


# Rozwiązanie 1
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    return sorted([x**2 for x in array1]) == sorted(array2)


# Rozwiązanie 2
def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""Your task is to make two functions ( max and min, or maximum and minimum, etc.,
 depending on the language ) that receive a list of integers as input, and return the
 largest and lowest number in that list, respectively."""


# Rozwiązanie
def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
 You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. """
""" 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
  
   Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"] """


# Rozwiązanie
def wave(people):
    result = []

    for i in range(len(people)):
        if people[i].isalpha():
            result.append(people[:i] + people[i].upper() + people[i + 1 :])

    return result


#####################################################################################
###############   ZADANIE 66      ###################################################
#####################################################################################
"""Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter."""


# Rozwiązanie 1 - kod łatwiejszy do zrozumienia
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    elif month <= 12:
        return 4
    else:
        return ValueError


# Rozwiązanie 2
def quarter_of(month):
    return (month - 1) // 3 + 1


#####################################################################################
###############   ZADANIE 67      ###################################################
#####################################################################################
"""Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"""


# Rozwiązanie - 1
def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# Rozwiązanie - 2
def are_you_playing_banjo(name):
    return (
        f"{name} plays banjo"
        if name[0] == "r" or name[0] == "R"
        else f"{name} does not play banjo"
    )


# Rozwiązanie - 3 - Dobra bardzij już chyba tego nie uproszczę :)
def are_you_playing_banjo(name):
    return (
        f"{name} plays banjo"
        if name[0].lower() == "r"
        else f"{name} does not play banjo"
    )


#####################################################################################
###############   ZADANIE 68      ###################################################
#####################################################################################
"""Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34"""


# Rozwiązanie
def opposite(number):
    return number * (-1)


#####################################################################################
###############   ZADANIE 69      ###################################################
#####################################################################################
"""Write a function which converts the input string to uppercase."""


# Rozwiązanie 1 - the fuck i get today? - lvl 8 kyu kata as if! Ha tfu
def make_upper_case(s):
    return s.upper()


#####################################################################################
###############   ZADANIE 70      ###################################################
#####################################################################################
"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""


# Rozwiązanie - 1 - now it get better
def find_short(s):
    words = s.split()
    min_length = min(len(word) for word in words)
    return min_length


# Rozwiązanie - 2
def find_short(s):
    return min(len(x) for x in s.split())


#####################################################################################
###############   ZADANIE 71      ###################################################
#####################################################################################
"""Code as fast as you can! You need to double the integer and return it."""  # kek


def double_integer(i):
    return i * 2


#####################################################################################
###############   ZADANIE 72      ###################################################
#####################################################################################
"""Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array."""


# Rozwiązanie 1
def min_max(lst):
    min_max = [min(lst), max(lst)]
    return min_max


# Rozwiązanie 2
def min_max(lst):
    return [min(lst), max(lst)]


#####################################################################################
###############   ZADANIE 73      ###################################################
#####################################################################################
"""Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"""


# Rozwiązanie 1
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p2 == "scissors" and p1 == "paper":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p2 == "rock" and p1 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p2 == "paper" and p1 == "rock":
        return "Player 1 won!"
    else:
        return "Draw!"


# Rozwiązanie 2
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (
        (p1 == "rock" and p2 == "scissors")
        or (p1 == "scissors" and p2 == "paper")
        or (p1 == "paper" and p2 == "rock")
    ):
        return "Player 1 won!"
    else:
        return "Player 2 won!"


#####################################################################################
###############   ZADANIE 74      ###################################################
#####################################################################################
"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  """


# Rozwiązanie 1
def sort_array(source_array):

    odds = []
    answer = []

    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")

        else:
            answer.append(i)

    odds.sort()

    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer


# Rozwiązanie 2
def sort_array(source_array):
    # Wyciągam liczby nie parzyste z source array
    odd_numbers = sorted(x for x in source_array if x % 2 != 0)

    # zamieniam posortowane liczby nieparzyste w miejsca wcześniej występujących liczb nieparzystych
    result = [x if x % 2 == 0 else odd_numbers.pop(0) for x in source_array]

    return result


#####################################################################################
###############   ZADANIE 75      ###################################################
#####################################################################################
"""Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0."""


# Ropwiązanie - 1
def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return sum(numbers) / len(numbers)


# Rozwiązanie 2
def find_average(numbers):
    return 0 if numbers == [] else sum(numbers) / len(numbers)


#####################################################################################
###############   ZADANIE 76      ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 77      ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 78      ###################################################
#####################################################################################
