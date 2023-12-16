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


##ZADANIE 18
#start_num = 500 #provide some start number
#end_num = 100 #provide some end number that you stop when you hit
#count_by = 2 #provide some number to count by
#break_num = start_num
#result = ()
## write a while loop that uses break_num as the ongoing number to
##   check against end_num
#if start_num > end_num:
#    result = "Oops! Looks like your start value is greater than the end value. Please try again."
#else:
#    break_num = start_num
#    while break_num < end_num:
#        break_num += count_by
#    result = break_num
#print(result)
##------------------------------------------------------------------------



##ZADANIE 19
#limit = 40
#number = 0
#nearest_square = 1
## write your while loop here
#while (number+1)**2 < limit:
#    number += 1
#    #square = number**2
#    nearest_square = number**2

#print(nearest_square)
##---------------------------------------------------------------------------


##ZADANIE 20

#num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
#count_odd = 0
#list_sum = 0
#i = 0
#len_num_list = len(num_list)
#while (count_odd < 5) and (i < len_num_list):
#    if num_list[i] % 2 !=0:
#        list_sum += num_list[i]
#        count_odd += 1
#    i += 1
#print ("The numbers of odd numbers added are: {}".format(count_odd))
#print ("The sum of the odd numbers added is: {}".format(list_sum))
##------------------------------------------------------


##ZADANIE 21
#headlines = ["Local Bear Eaten by Man",
#             "Legislature Announces New Laws",
#             "Peasant Discovers Violence Inherent in System",
#             "Cat Rescues Fireman Stuck in Tree",
#             "Brave Knight Runs Away",
#             "Papperbok Review: Totally Triffic"]

#news_ticker = ""
#for headline in headlines:
#    news_ticker += headline + " "
#    if len(news_ticker) >= 140:
#        news_ticker = news_ticker[:140]
#        break

#print(news_ticker)
##-------------------------------------------------------------


##ZADANIE 22
## Your code should check if each number in the list is a prime number
#check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

#for prime in check_prime:
#    if prime % 2 != 0 and prime % 3 != 0 and prime % 5 != 0 and prime % 7 != 0:
#        print("{} isa prime number".format(prime))
#    else:
#        print('is NOT a prime number because 2 is factor of {}'.format(prime))
##-------------------------------------------------------------


##ZADANIE 23
#x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
#y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
#z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
#labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

#points = []
# write your for loop here
#for x_coord, y_coord, z_coord, labels in zip(x_coord, y_coord, z_coord, labels):
#    points.append("point:{}, {}, {}, {}".format(x_coord, y_coord, z_coord, labels))

#for point in points:
#    print(point)

##-------------------------------------------------------------------


##ZADANIE 24

## write your function here
#def population_density(num_of_people, area):
#    return num_of_people / area


## test cases for your function
#test1 = population_density(10, 1)
#expected_result1 = 10
#print("expected result: {}, actual result: {}".format(expected_result1, test1))

#test2 = population_density(864816, 121.4)
#expected_result2 = 7123.6902801
#print("expected result: {}, actual result: {}".format(expected_result2, test2))

##-----------------------------------------------------------------



## ZADANIE 25

## write your function here
#def readable_timedelta(days):
#    weeks = days // 7
#    day_s = days % 7
#    return "{} week(s) and {} day(s).".format(weeks, day_s)

## test your function
#print(readable_timedelta(10))
##---------------------------------------------------------------------


##ZADANIE 26

#numbers = [
#              [34, 63, 88, 71, 29],
#              [90, 78, 51, 27, 45],
#              [63, 37, 85, 46, 22],
#              [51, 22, 34, 11, 18]
#           ]

#averages = lambda num_list :sum(num_list) / len(num_list)

#def mean(num_list):
#    return sum(num_list) / len(num_list)

#averages = list(map(mean, numbers))
#print(averages)
##--------------------------------------------------------------------


##ZADANIE 27

#cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#is_short = lambda name: len(name) < 10

#def is_short(name):
#   return len(name) < 10

#short_cities = list(filter(is_short, cities))
#print(short_cities)
##---------------------------------------------------------------------


## ZADANIE 28
#how_many_snakes = 1
#snake_string = """
#Welcome to Python3!

#             ____
#            / . .\\
#            \  ---<
#             \  /
#   __________/ /
#-=:___________/

#<3, Juno
#"""


#print(snake_string * how_many_snakes)
##-------------------------------------------------------------------


##ZADANIE 29

#names = input('Enter names separated by commas: ').title().split(",") # get and process input for a list of names
#assignments =  input('Enter assignment counts separated by commas: ').split(",")# get and process input for a list of the number of assignments
#grades =  input('Enter grades separated by commas: ').split(",") # get and process input for a list of grades

## message string to be used for each student
## HINT: use .format() with this string in your for loop
#message = ("Hi {},\n\nThis is a reminder that you have {} assignments left to \
#submit before you can graduate. You're current grade is {} and can increase \
#to {} if you submit all assignments before the due date.\n\n")

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
#for name, assignment, grade in zip(names, assignments, grades):
#    print(message.format(name, assignment, grade, int(grade) +int(assignment)*2))
##----------------------------------------------------------------------

