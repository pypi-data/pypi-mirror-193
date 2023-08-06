#  Package

A python library containing useful functions.

Installation:
	
pip install epydz


# Example usage
from epydz import *

result = 5

lokan(result == 5, lambda: werili(result))




Functions: 


werili: #takes any number of arguments and concatenates them into a string separated by sep. The resulting string is then printed to the console followed by end.

dekhel: #prompts the user for input and returns the user's response as a string.

lokan:# takes a boolean condition and a function result_fn. If condition is True, the function result_fn is called and its result is returned. Otherwise, None is returned.

ilokan: #similar to lokan, but returns a default value instead of None if the condition is false.

tsema: #returns a default value for use in ilokan.

akesam: #splits a string into a list of items based on a separator.

akelab: #returns a reversed list of items.

motawasit: #returns the average of a list of numbers.

nisf: #returns the median of a list of numbers

ahseb: #returns the number of words in a string.

dirr: #Loop for the specified maximum number (100) of iterations or until a non-None value is returned.



