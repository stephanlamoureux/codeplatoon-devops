# Roman Numerals

## Part 1: Lazy Roman Numerals

Given a number in today's numbers, (Arabic Numeral), return its equivalent in Roman Numerals in the lazy way. Lazy Roman Numerals is where Roman Numerals are added together (9 is `VIIII`, 4 is `IIII`). Here are Roman Numerals with their Arabic Numeral counterparts:

```
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000
```


## Part 2: Modern Roman Numerals

If a smaller number appears before a larger number, you must subtract the smaller one. Here's a list for you:

```
IV -> 4
IX -> 9
XIV -> 14
XLIV -> 44
CMXLIV -> 944
```

### Sample output:
```
to_roman(4) # 'IV'
to_roman(944) # 'CMXLIV'
to_roman(150) # CL
```

### Hint: Consider the data structure(s) that can be used to store numerical values, and how it can relate to string representations. Break the problem down... how many combinations are there really to consider?


#### DO NOT concern yourself with very large numbers. Your algorithm should keep appending 'M' for each thousand. (Numbers over 3000 have different numerical representations)
