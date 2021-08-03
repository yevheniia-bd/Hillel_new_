import json

def get_duration():
    with open('acdc.json', 'r') as file:
        file_dict = json.load(file)
        return [int(track['duration']) for
                track in file_dict['track']]
print(file_dict)
# result.append(int(duration['duration'])]
# return result

def sum_duration():
    for item in file_dict.items():
        print(item)
    values = file_dict.values()
    print(values)
    total_duration = 0
    for value in file_dict.values():
        total_duration += value

print(total_duration)
get_duration()
# # sum(file_dict.values())


# import datetime
# sum_all_track_duration = datetime.datetime.second()
# print(sum_all_track_duration)



# with open('acdc.json', 'r+') as f:
#     file_dict = json.load(f)
#     print(file_dict)
#     print(file_dict['name']['url']['duration'])
#     file_dict['name']['url']['duration'] = 'track'
#     f.writelines('')
#     json.dump(file_dict, f)