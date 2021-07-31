def clean_dict():
    dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
    dict = {k: v for k, v in dict.items() if v is not None}
    print(dict)



# print(dict.get('key3')[2])

print(clean_dict())





#