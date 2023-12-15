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

