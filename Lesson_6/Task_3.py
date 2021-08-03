list_nums = ['a', 'b', 'c', 'd', 'e']
def key_value(list_nums):
    return dict(enumerate(list_nums))

print(key_value(list_nums))