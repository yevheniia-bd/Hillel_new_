def clean_dict():
    dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
    values = dict.values()
    print(values)
    if values==None:
        dict.pop()
clean_dict()
