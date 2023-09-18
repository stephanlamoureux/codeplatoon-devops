"""Reading Errors Assignment

errors.py is riddled with different types of errors.

1. Run the script: `python errors.py`
2. Review the error message (Traceback AKA Stack trace) in your terminal.
3. Attempt to fix the specified error on the specified line.
4. Repeat Step 1 through 3 until the script runs without error.

> This "traceback" is also called a stack trace. In many cases the most
relevant lines of the stack trace will be the last few lines. It will
show the ErrorType, File Name, and Line Number of the where that raised
the error occurred. In this case the errors should always be occurring in
errors.py but in more complex applications you could have many `.py`
files involved.

SOMETHING TO THINK ABOUT:
One of the errors below occurs because of the order of execution.
When you run this script Python will read AND execute the file from top
to bottom in order. This is important when trying to reference something
that has yet to set to exist.
"""


"""
Expectation: This code should have printed out: how are you


Documentation:
https://docs.python.org/3/library/exceptions.html#SyntaxError
"""
# ---- Fix the SyntaxError below ----
print("how are you")


"""
Expectation: This code should have printed out: hello there

Documentation:
https://docs.python.org/3/library/exceptions.html#NameError
"""
# ---- Fix the NameError below ----
print("hello there")


"""
Expectation: Calling my_func should have printed out the message that
was passed in as the argument. In this case:

I'm fine

Should have been printed to the terminal.

Documentation:
https://docs.python.org/3/library/exceptions.html#NameError

"""
# ---- Fix the NameError below ----


def my_func(message):
    """When called with an `message` argument, this function should
    just print that `message` that was passed in.

    Even though everything in this function is valid,
    something about this function is still incorrect.
    """
    print(message)


print(my_func("I'm fine"))

"""
Expectation: This code should have printed the value mapped to the
dictionary key of 'first', which should have been 1.

Documentation:
https://docs.python.org/3/library/exceptions.html#AttributeError
"""
# ---- Fix the AttributeError below ----
my_obj = {"first": 1, "second": 2}
print(my_obj["first"])


"""
Expectation: This code should have printed the value mapped to the
dictionary key of 'three'

Documentation:
https://docs.python.org/3/library/exceptions.html#KeyError
"""
# ---- Fix the KeyError below ----
my_obj = {"one": 1, "two": 2, "three": 3}
print(my_obj["three"])


"""
Expectation: This code should have printed the 4th item from
my_list, which should have been 7.

Documentation:
https://docs.python.org/3/library/exceptions.html#IndexError
"""
# ---- Fix the IndexError below ----
my_list = [4, 5, 6, 7]
print(my_list[3])


"""
Expectation: This code should print the concatenation of '5' to 9.
So we should ideally see '59' printed out.

Documentation:
https://docs.python.org/3/library/exceptions.html#TypeError
"""
# ---- Fix the TypeError below ----
print("5" + str(9))


"""
Expectation: This code should loop 4 times printing out each value
from 0 to 4. Such as:
0
1
2
3

Documentation:
https://docs.python.org/3/library/exceptions.html#TypeError
"""
# ---- Fix the TypeError below ----
my_int = range(4)
for i in my_int:
    print(i)


"""
Expectation: This code should print out: Code Platoon!

Documentation:
https://docs.python.org/3/library/exceptions.html#IndentationError
"""
# ---- Fix the Indentation Error below ----
print("Code Platoon!")
