#####################################################################################
###############   ZADANIE 1      ####################################################
#####################################################################################

# # from preloaded import MORSE_CODE

# MORSE_CODE = {'A': '.-', 'B': '-...',
#                    'C': '-.-.', 'D': '-..', 'E': '.',
#                    'F': '..-.', 'G': '--.', 'H': '....',
#                    'I': '..', 'J': '.---', 'K': '-.-',
#                    'L': '.-..', 'M': '--', 'N': '-.',
#                    'O': '---', 'P': '.--.', 'Q': '--.-',
#                    'R': '.-.', 'S': '...', 'T': '-',
#                    'U': '..-', 'V': '...-', 'W': '.--',
#                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                    '1': '.----', '2': '..---', '3': '...--',
#                    '4': '....-', '5': '.....', '6': '-....',
#                    '7': '--...', '8': '---..', '9': '----.',
#                    '0': '-----', ',': '--..--', '.': '.-.-.-',
#                    '?': '..--..', '/': '-..-.', '-': '-....-',
#                    '(': '-.--.', ')': '-.--.-', ' ': '/'}


# def decode_morse(morse_code):
#     morse_code = morse_code.strip()  # Remove leading and trailing whitespaces
#     morse_words = morse_code.split('   ')  # Split the Morse code into words

#     decoded_words = []
#     for word in morse_words:
#         morse_chars = word.split(' ')  # Split the Morse word into characters
#         decoded_word = ''.join([key for char in morse_chars for key, value in MORSE_CODE.items() if value == char])
#         decoded_words.append(decoded_word)

#     decoded_sentence = ' '.join(decoded_words)
#     return decoded_sentence


# # Example usage:
# morse_code_input = "... --- ..."
# decoded_string = decode_morse(morse_code_input)
# print(decoded_string)

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