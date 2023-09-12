# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong = []

    if type(numbers) == int:
        sum = 0
        power = int(len(str(numbers)))
        for digit in str(numbers):
            sum += int(digit) ** power
            if sum == numbers:
                armstrong.append(numbers)

    elif type(numbers) == list:
        for number in numbers:
            sum = 0
            power = int(len(str(number)))
            for digit in str(number):
                sum += int(digit) ** power
                if sum == number:
                    armstrong.append(number)

    else:
        return "Invalid Input."

    return armstrong


print(find_armstrong_numbers(list(range(0, 999))))
