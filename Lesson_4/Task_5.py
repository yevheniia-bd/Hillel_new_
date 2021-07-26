string = input('Enter something: ')

def string_slices():
    print(string[2])
    print(string[-2])
    print(string[:4])
    print(string[:-2])
    print(string[::2])
    print(string[1::2])
    print(string[::-1])
    print(string[::-2])
    print(len(string))
string_slices()