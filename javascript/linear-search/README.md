# Algorithm Drill Linear Search

## Summary

In computer science, there are many different ways to search through collections of data. Understanding the various algorithms and patterns for searching and sorting data sets is an essential part of computer science.

While modern programming languages such as Python abstract many of the lower-level functions of programming by providing us with function like `index()`(Javascript equivalent method `indexOf()`), it is important to know what is going on underneath the hood. Employers look for people who understand how to put a car together, not someone who knows how to drive. Aside from being important to your knowledge of theory, the searching and sorting algorithms you use will have a significant impact on your program's performance (how long it takes to execute and how much memory it uses). We'll be talking about Big O notation soon.

One of the most basic searching algorithms is the **linear search**.  In this challenge, you will build a `linear_search` function using very basic programming constructs.

Linear search (also called *sequential* search) is an algorithm for finding a particular value in a list by checking every one of its elements, one at a time and in sequence, until the desired one is found. *Source: [Wikipedia](http://en.wikipedia.org/wiki/Linear_search)*


#### Note: 
For the Javascript portion of this challenge, you will need to install this 3rd-party npm package to get the global linear search tests to run correctly: [Shallow-equal](https://www.npmjs.com/package/shallow-equal).  In order to use a 3rd-party npm package, you will need to initialize a npm project.  How do you to that?  [Here](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/) is a good place to start.
HINT: `npm init` will probably be the first step.


## Releases
### Release 0 : Basic linear search

Write a function `linear_search` that takes two arguments: the object (i.e., string or number) you are searching for, and the array you're searching in. You will also want to add some driver code. Driver code is instructions that exists outside of your function definition(s). On larger applications, it can even be used to call multiple scripts for multiple functions. Think of it as the main logic of your program after you've defined all the operations needed.  

#### Guidelines

 * It should return an integer representing the index of the object in the array by going through each element in sequence and returning the index of the first instance of the object.
 * If the object searched for does not exist in the array, it should return `None`(Python) or `undefined`(Javascript).

Here's the catch: for the Python portion, you can't use any built-in `list` or `Enumerable` methods *except* for `list()`.  You will have to use the keywords `for`, or `while`.
There are two tests already in the spec file, but you should add more to prove that your code works correctly. Are there any edge cases you need to consider? Did you hit any bugs that should have had tests?

### Release 1 : Global linear search

Write a new function `global_linear_search` that returns an array of *all the indices* for the object it searches for.  In other words, if the object `x` is in more than one place in the array, `global_linear_search` will return an array containing the index of each occurrence of `x`.

Here's an example of what that might look like.

```python
bananas_list = list('bananas')
# => ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_list)
# => [ 1, 3, 5 ]
```

There are no tests for `global_linear_search` right now. Maybe the example above is a good starting point?
