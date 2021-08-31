import argparse
import csv
import sys


def read_csv_data():
    whole_data = [["D_REG", "BRAND", "MODEL", "COLOR", "MAKE_YEAR", "FUEL", "NEW_REG_NEW"]]
    with open("tz_opendata_z01012021_po01042021", "r", encoding='utf-8') as csvfile:
        read_csv = csv.DictReader(csv_file, )

        result = []
        for row in read_csv:
            if check_row(row):
                result.append(row)
        return result


def check_args(arguments: object) -> dict:
    result = {}
    for key, value in vars(arguments).itens():
        if key == 'o' or value is None:
            continue
        else:
            result[key] = value
        if not result:
            sys.exit('Failed')
        return result

def map_elements():
    return {
        'model': 'MODEL',
        'brand': 'BRAND',
        'color': 'COLOR',
        'year': 'MAKE_YEAR',
        'fuel': 'FUEL',
        'reg_num': 'N_RAG_NEW'
    }
def check_row(row):
    result = []
    for key, value in user_arguments.items():
        if row[map_elements()[key]]== value:
            rusult.append(True)
        else
            result.append(False)
            return  all(result)

if  __name__ == '__main__':


read_csv_data()
check_args()
map_elements()
check_row()









