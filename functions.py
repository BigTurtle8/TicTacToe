# Python program to convert a list
# to string using list comprehension
def list_to_str(lst, sep=''):
    # using list comprehension
    new = sep.join([str(elem) for elem in lst])

    return new
