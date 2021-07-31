one_side = int(input('Enter side: '))
def square():
    result = (4 * one_side, one_side * one_side,((one_side ** 2) / 2) ** 0.5)
    return result
print(square())
