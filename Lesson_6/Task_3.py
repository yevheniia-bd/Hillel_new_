def key_value(list) -> list:
    ind = 0
    result = {}
    list =['a', 'b', 'c', 'd', 'e']
    for value in list:
        result[ind] = value
        ind += 1
print(key_value(list))