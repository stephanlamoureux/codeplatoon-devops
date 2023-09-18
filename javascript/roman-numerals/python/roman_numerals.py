def lazy_roman(num):
    numeral = ""
    number = num
    while num > 0:
        if num >= 1000:
            numeral += "M"
            num -= 1000
        elif num >= 500:
            numeral += "D"
            num -= 500
        elif num >= 100:
            numeral += "C"
            num -= 100
        elif num >= 50:
            numeral += "L"
            num -= 50
        elif num >= 10:
            numeral += "X"
            num -= 10
        elif num >= 5:
            numeral += "V"
            num -= 5
        else:
            numeral += "I"
            num -= 1
    return f"The LAZY Roman Numeral of {number} is: {numeral}."


# tests
print(lazy_roman(300))  # CCC
print(lazy_roman(9))  # VIIII
print(lazy_roman(2333))  # MMCCCXXXIII

print("-----------------------------------")


def to_roman(num):
    roman_numeral = ""
    number = num

    numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    for key in numerals:
        while num >= key:
            roman_numeral += numerals[key]
            num -= key
    return f"The Roman Numeral of {number} is: {roman_numeral}."


# tests
print(to_roman(944))  # CMXLIV
print(to_roman(4))  # IV
print(to_roman(9))  # IX
print(to_roman(14))  # XIV
print(to_roman(44))  # XLIV
print(to_roman(3944))  # MMMCMXLIV
