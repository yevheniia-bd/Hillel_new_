n = int(input('Enter number: '))

def stairs(n):
    if n <= 9:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, sep='', end='')
            print()
stairs(n)
