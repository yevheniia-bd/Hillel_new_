some_list = [2,7,93,28,11,37,482,87,3,78]
def change_funk() -> list:
    for i, v in enumerate(some_list):
        if v % 2 == 0:
            some_list[i] = 0
    print(some_list)


change_funk()