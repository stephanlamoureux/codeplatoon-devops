# Deaf Grandma

This small challenge comes from Chris Pine's "Learn to Program". Ensure that you read everything and click every link before starting the work.
 
## Premise

Write a program which can imitate a Grandma who's hard of hearing and follows
these constraints:

* If you don't input anything (just hit enter) she responds with `WHAT?!`
* If you ask a question with any lower-case letters, she responds with
`SPEAK UP, KID!`
* If you talk to her in all upper-case letters, she responds with
`NO, NOT SINCE 1946!`

* The first time you say `GOODBYE!` she says `LEAVING SO SOON?`
* The second time you say `GOODBYE!` she says `LATER, SKATER!` and the program
exits.

## Example

```
HEY KID!
> hi, grandma
SPEAK UP, KID!
> I SAID HI, GRANDMA
NO, NOT SINCE 1946!
>
WHAT?!
> Goodbye!
SPEAK UP, KID!
> GOODBYE!
LEAVING SO SOON?
> GOODBYE!
LATER, SKATER!
```

## Considerations (Python)
* In your code you'll definitely need to use `if` and likely an `elif` and `else`.
* Also remember that `input()` is the "inverse" method of `print()` -- while `print()` outputs information to the terminal, `input('command Prompt')` captures information from the user by presenting a command prompt and allowing them to type input.
* If you have an infinite loop, how might you break out of it?

## Considerations (Javascript)
* Just a heads up: this is extraordinarily difficult to do in JS
* In your code you'll definitely need to use `if` and likely an `else if` and `else`.
* Will you need [prompt](http://www.w3schools.com/jsref/met_win_prompt.asp) or [prompt](https://github.com/flatiron/prompt)? [Google](https://www.google.com/search?q=javascript+how+to+prompt+user+from+the+command+line&oq=javascript+how+to+prompt+user+from+the+command+line&gs_l=psy-ab.3..33i22i29i30k1.3662.8926.0.9212.42.28.0.0.0.0.278.3644.0j16j5.21.0....0...1.1.64.psy-ab..34.1.135.W7Xo9Rq5nKY) it!

## Challenge Yourself

For a little extra fun, try refactoring your code to use regular expressions.
