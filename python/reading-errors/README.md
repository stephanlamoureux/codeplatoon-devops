# Reading Errors

As a developer running into errors is unavoidable. As you practice writing code, running short scripts, and running other larger programs you will run into different types of Errors/Exceptions that are "raised" from that program. There are lots of different types of mistakes you can make with code below are some of the most common ones you will encounter.

Learning to recognize these errors are maybe one of the most crucial skills for a new developer to learn how to do. At first some of these errors will seem cryptic, but with practice and repetition you will eventually understand what the stack trace is telling you when you see these errors occur in the future.

## Assignment Instructions

`errors.py` is riddled with different types of errors. 

1. Run the script: `python errors.py`
2. Review the error message in your terminal
3. Attempt to fix the specified error on the specified line
4. Repeat all these steps until the script runs without error

> A "traceback" is also called a stack trace. In many cases the **most relevant lines** of the stack trace will be the last few lines. It will show the **ErrorType**, **File Name**, and **Line Number** of the where that raised the error occured. In this case the errors should always be occuring in `errors.py` but in more complex applications you could have many `.py` files involved.

### Something to keep in mind
One of the errors in `errors.py` occurs because of the order of execution. When you run this script Python will read AND execute the file from top to bottom in order. This is important when trying to reference something that has not yet been **defined** or set to exist.
