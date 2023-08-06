#This function prompts the user to enter input and returns the input string.
def werili(*args, sep=' ', end='\n'):
    output = ''
    for arg in args:
        output += str(arg) + sep
    output = output[:-len(sep)] + end
    print(output, end='')
    
#This function outputs the user's input .
def dekhel(prompt=''):
    return input(prompt)

#This function takes a boolean condition and a function as arguments. If the condition is true, it calls the function and returns its result. Otherwise, it returns None.
def lokan(condition, result_fn):
    return result_fn() if condition else None
    
#This function is similar to lokan, but it calls the function if the condition is false.
def ilokan(condition, result_fn):
    return result_fn() if condition else None

#This function takes a value as an argument and returns it. It is often used as a placeholder when an 'if' statement requires an 'else' branch that does nothing.
def tsema(result_false):
    return result_false
    
#This function takes a string and a separator as arguments and splits the string into a list of substrings at each occurrence of the separator.
def akesam(string, separator):
    return string.split(separator)
    
#This function takes a list of items and returns a new list with the items in reverse order.
def akelab(items):
    return list(reversed(items))

#This function takes a list of numbers and returns their average (mean) value.
def motawasit(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
    
 #This function takes a list of numbers and returns their median value.
def nisf(numbers):
    n = len(numbers)
    if n == 0:
        return None
    numbers_sorted = sorted(numbers)
    if n % 2 == 0:
        mid = n // 2
        return (numbers_sorted[mid-1] + numbers_sorted[mid]) / 2
    else:
        return numbers_sorted[n // 2]
       
 # this function takes a string as input and returns the number of words in the string
def ahseb(string):
    return len(string.split())
 
 # Loop for the specified maximum number of iterations or until a non-None value is returned.
def dirr(fn, *args, max_iter=100):
    for i in range(max_iter):
        result = fn(*args)
        if result is not None:
            return result
    return None
