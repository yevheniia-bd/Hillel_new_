q = int(input('Enter number: '))
w = int(input('Enter number: '))
def figure_area(q, w, e=1):
    if e == 1:
        print('Area of a triangle:', q * w / 2)
    if e == 2:
        print('Square area:', q * w)
figure_area(q, w, e=1)