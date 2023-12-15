## ZADANIE 1 DATA TYPES
#month = 8
#days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

## use list indexing to determine the number of days in month
#num_days = days_in_month[month-1]

#print(num_days)
##---------------------------------------------------------------------



##ZADANIE 2
## Define a Dictionary, population,
## that provides information
## on the world's largest cities.
## The key is the name of a city
## (a string), and the associated
## value is its population in
## millions of people.

##   Key     |   Value
## Shanghai  |   17.8
## Istanbul  |   13.3
## Karachi   |   13.0
## Mumbai    |   12.5

#population = {"Shanghai":17.8,"Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}
#print(population["Shanghai"])
##------------------------------------------------------------------------



##ZADANIE 3
#elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
#            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

## todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
## hint: helium is a noble gas, hydrogen isn't
#elements['hydrogen']['is_noble_gas'] = False
#elements['helium']['is_noble_gas'] = True
#print(elements['hydrogen']['is_noble_gas'])
#print(elements['helium']['is_noble_gas'])
##-------------------------------------------------------


##ZADANIE 4
#verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
#print(verse, '\n')

## split verse into list of words
#verse_list = verse.split()
#print(verse_list, '\n')

## convert list to a data structure that stores unique elements
#verse_set =set(verse_list)
#print(verse_set, '\n')

## print the number of unique words
#num_unique = len(verse_set)
#print(num_unique, '\n')
##--------------------------------------------------------------


##ZADANIE 5
# verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
# print(verse_dict, '\n')

# # find number of unique keys in the dictionary
# num_keys = len(set(verse_dict))
# print(num_keys)

# # find whether 'breathe' is a key in the dictionary
# contains_breathe = list(verse_dict).count("breath")
# print(contains_breathe)

# # create and sort a list of the dictionary's keys
# sorted_keys = sorted(verse_dict.keys())

# # get the first element in the sorted list of keys
# print(sorted_keys[0])

# # find the element with the highest value in the list of keys
# print(max(sorted_keys))
##-----------------------------------------------------------------------------


##ZADANIE 6
# points = 174  # use this input to make your submission

## write your if statement here
# if points <= 50:
#    result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#    result = "Oh dear, no prize this time."
# elif points <= 180:
#    result = "Congratulations! You won a wafer-thin mint!"
# elif points <= 200:
#    result = "Congratulations! You won a penguin!"
# print(result)
##-----------------------------------------------------------------------------


##ZADANIE 7
## '''
## You decide you want to play a game where you are hiding
## a number from someone.  Store this number in a variable
## called 'answer'.  Another user provides a number called
## 'guess'.  By comparing guess to answer, you inform the user
## if their guess is too high or too low.

## Fill in the conditionals below to inform the user about how
## their guess compares to the answer.
## '''
# answer = input("Prowide answer: ")
# guess =  input("Prowide guess: ")

# if answer > guess:
#    result = "Oops!  Your guess was too low."
# elif answer < guess:
#    result = "Oops!  Your guess was too high."
# elif answer == guess:
#    result = "Nice!  Your guess matched the answer!"

# print(result)
##-----------------------------------------------------------------------------


##ZADANIE 8
## '''
## Depending on where an individual is from we need to tax them
## appropriately.  The states of CA, MN, and
## NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
## Use this information to take the amount of a purchase and
## the corresponding state to assure that they are taxed by the right
## amount.
## '''
# state = "NY"
# purchase_amount = 500

# if state == "CA":
#    tax_amount = .075
#    total_cost = purchase_amount*(1+tax_amount)
#    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# elif state == "MN":
#    tax_amount = .095
#    total_cost = purchase_amount*(1+tax_amount)
#    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# elif state == "NY":
#    tax_amount = .089
#    total_cost = purchase_amount*(1+tax_amount)
#    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# print(result)
##-----------------------------------------------------------------------------------


##ZADANIE 9

##~~~~~~~JAK JA ZROBIŁEM~~~~~~~~~~~###
# points = 174  # use this as input for your submission

## establish the default prize value to None
# prize = ()

## use the points value to assign prizes to the correct prize names
# if points <= 50:
#    prize = "wooden rabbit"
# elif points <= 150:
#    prize = 0
# elif points <= 180:
#    prize = "wafer-thin mint"
# else:
#    prize = "penguin"

## use the truth value of prize to assign result to the correct prize
# if prize == 0:
#    result ="Oh dear, no prize this time."
# else:
#    result = "Congratulations! You won a {}!".format(prize)
# print(result)


##~~~~~~JAK ONI ZROBILI~~~~~~~##
# points = 174

# points = 174  # use this input when submitting your answer

## set prize to default value of None
# prize = None

## use the value of points to assign prize to the correct prize name
# if points <= 50:
#    prize = "wooden rabbit"
# elif 151 <= points <= 180:
#    prize = "wafer-thin mint"
# elif points >= 181:
#    prize = "penguin"

## use the truth value of prize to assign result to the correct message
# if prize:
#    result = "Congratulations! You won a {}!".format(prize)
# else:
#    result = "Oh dear, no prize this time."

# print(result)
##------------------------------------------------------------------------------------


##ZADANIE 10
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

## write your for loop here
# for name in names:
#    name = name.lower().replace(" ","_")
#    usernames.append(name)
# print(usernames)
##--------------------------------------------------------------------------


##ZADANIE 11
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# # write your for loop here
# for names in range(len(usernames)):
#    usernames[names] = usernames[names].lower().replace(" ", "_")

# print(usernames)
##--------------------------------------------------------


##ZADANIE 12
# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# count = 0

## write your for loop here
# for token in tokens:
#    if token[0] == "<"and token[-1] == ">":
#        count += 1

# print(count)
##-----------------------------------------------------------------------


##ZADANIE 13
# items = ['first string', 'second string']
# html_str = ()  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

## write your code here
# for item in items:
#    html_str = "<ul>\n" + "<li>"+'first string'+"</li>\n" + "<li>"+'second string'+"</li>\n" +"</ul>"

# print(html_str)
##------------------------------------------------------------------------------


##ZADANIE 14
## You would like to count the number of fruits in your basket.
## In order to do this, you have the following dictionary and list of
## fruits.  Use the dictionary and list to count the total number
## of fruits, but you do not want to count the other items in your basket.

# result = 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

##Iterate through the dictionary
# for object, count in basket_items.items():
#        if object in basket_items and object in fruits:
#            result += count
##if the key is in the list of fruits, add the value (number of fruits) to result


# print(result)
##--------------------------------------------------


##ZADANIE 15
## You would like to count the number of fruits in your basket.
## In order to do this, you have the following dictionary and list of
## fruits.  Use the dictionary and list to count the total number
## of fruits and not_fruits.

# fruit_count, not_fruit_count = 0, 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
# for object, count in basket_items.items():
#        if object in fruits:
#            fruit_count += count
#        else:
#            not_fruit_count += count
##if the key is in the list of fruits, add to fruit_count.

##if the key is not in the list, then add to the not_fruit_count


# print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))
##------------------------------------------------------------------------------


##ZADANIE 16
## number to find the factorial of
# number = 6

# start with our product equal to one
# product = 1

# track the current number being multiplied
# current = 1

# write your while loop here
# while current <= number:

#    # multiply the product so far by the current number
#        product *= current

#    # increment current with each iteration until it reaches number
#        current += 1

## print the factorial of number
# print(product)
##-----------------------------------------------------------


##ZADANIE 17
# start_num = 1 #provide some start number
# end_num = 500#provide some end number that you stop when you hit
# count_by =  5#provide some number to count by
# break_num = start_num
## write a while loop that uses break_num as the ongoing number to
##   check against end_num
# while break_num < end_num:
#    break_num += count_by

# print(break_num)
##-----------------------------------------------------------
