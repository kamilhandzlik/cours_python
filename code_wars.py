#####################################################################################
###############   ZADANIE 1      ####################################################
#####################################################################################

# from preloaded import MORSE_CODE

MORSE_CODE = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}


def decode_morse(morse_code):
    morse_code = morse_code.strip()  # Remove leading and trailing whitespaces
    morse_words = morse_code.split('   ')  # Split the Morse code into words

    decoded_words = []
    for word in morse_words:
        morse_chars = word.split(' ')  # Split the Morse word into characters
        decoded_word = ''.join([key for char in morse_chars for key, value in MORSE_CODE.items() if value == char])
        decoded_words.append(decoded_word)

    decoded_sentence = ' '.join(decoded_words)
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

text = 'aabfbbsbdbs165131'

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
    #your code here
    return n ** 3


# mój poboczny eksperymrnt żeby zobaczyć so będzie większe
n = 9
x = n ** n
current = 1
count = 1

while current < n:
    count *= current
    current += 1


solution = (x > count) 
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for letter in sentence.split(''):
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
        count += 1/2


#####################################################################################
###############   ZADANIE 7      ####################################################
#####################################################################################



def cakes(recipe, available):
    number_of_cakes = float('inf')  # Set initially to positive infinity

    for ingredient, amount_required in recipe.items():
        if ingredient in available:
            cakes_possible = available[ingredient] // amount_required
            number_of_cakes = min(number_of_cakes, cakes_possible)
        else:
            return 0  # If any ingredient is missing, return 0 cakes

    return number_of_cakes

# Examples
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
# Output: 2

print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
            {'sugar': 500, 'flour': 2000, 'milk': 2000}))
# Output: 0

# Tutaj spróbuje zrobić list comprihension

def cakes(recipe, available):
    return min([available[ingredient] // amount_required if ingredient in available else 0 for ingredient, amount_required in recipe.items()], default=float('inf'))


# Examples
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
# Output: 2

print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
            {'sugar': 500, 'flour': 2000, 'milk': 2000}))


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
        narc_num += digit ** num_digits
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
print(count('aba'))
print(count(''))

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

#rozwiązanie 2
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
        return int(pL, 2).to_bytes((int(pL, 2).bit_length() + 7) // 8, 'big').decode()
    return bin(int.from_bytes(pL.encode(), 'big'))


print(greet())

#jak to działa

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
        is_sq = 'Negative numbers cannot be square numbers'
    elif sqrt(n) is not float:
        is_sq = True
    else:
        is_sq = False
    return is_sq

print(is_square(3))

#Sposób 2 ten już działa perfekcyjnie na wszystko

import math

def is_square(n):
    # sprawdza czy pierwiastek drugiego stopnia jest intigerem
    return n > 0 and math.isqrt(n)**2 == n


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
            ("I", 1)
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
print(RomanNumerals.from_roman('MCMXC'))  # Expected output: 1990
print(RomanNumerals.from_roman('MMVIII'))  # Expected output: 2008


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

#rozwiązanie 1 - to działa w wersji konsolowej
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

#rozwiązanie 2 - to działa tak żebby zaliczyć katę na codewars
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

#Rozwiązanie 1
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 0 or (flower1 % 2 != 0 and flower2 % 2 != 0):
        return False
    elif (flower1 % 2 != 0 and flower2 % 2 == 0) or (flower1 % 2 == 0 and flower2 % 2 != 0):
        return True
    
#Rozwiązaanie 2
def lovefunc(flower1, flower2):
    # Check if one flower has even petals and the other has odd petals
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True  # They are in love
    else:
        return False  # They aren't in love
#Rozwiązanie 3
def lovefunc(f1, f2):
    return True if (f1 % 2 == 0 and f2 % 2 != 0) or (f2 % 2 == 0 and f1 % 2 != 0) else False
#Rozwiązanie 4 
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

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

