def list_of_numbers_input():
    list_of_numbers = []
    while True:
        numbers_input = int(input('Enter number: '))
        if numbers_input == 0:
            break
        list_of_numbers.append(numbers_input)
    return list_of_numbers
print(list_of_numbers_input())

def amount_entered_numbers(list_of_numbers: list) -> int:
    return len(list_of_numbers)
# amount_entered_numbers()

def summ_entered_numbers(list_of_numbers: list) -> int:
    summ = 0
    for number in list_of_numbers:
        summ += number
    return 'Sum of elements:', summ
# summ_entered_numbers()

import numpy as np

def array_entered_numbers(list_of_numbers: list) -> int:
    result = np.prod(np.array(list_of_numbers))
    return result

def max_number(list_of_numbers: list) -> int:
    max_number = max(list_of_numbers)
    print(max_number)
    return max(list_of_numbers)

def second_max(list_of_numbers: list) -> int:
    max_number = max(list_of_numbers)
    list_of_numbers.pop(list_of_numbers.index(max_number))
    return max(list_of_numbers)