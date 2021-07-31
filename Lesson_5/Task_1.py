number = int(input('Enter num > 0 and num < 1000: '))
def is_prime(number):

    if number % 2 == 0 and number != 2:
        return False
    else:
        return True
number = int(input('Enter num > 0 and num < 1000: '))
print(is_prime(number))