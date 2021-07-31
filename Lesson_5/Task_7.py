import datetime
d=int(input("Enter day: "))
m=int(input("Enter month: "))
y=int(input("Enter year: "))
date = datetime.date(d,m,y)
def is_date():
    try:
        date = datetime.datetime.strptime(input_string, "%d.%m.%Y")
        print(date)
        print("This date exist" - True)
    except:
        print("This date doesn't exist" - False)

is_date()