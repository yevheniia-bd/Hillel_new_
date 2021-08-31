import argparse
import requests

def get_data(start_date):
    result = requests.get('https://api.exchangerate.host/convert',
                          params={'from': args.currency_from,
                                  'to': args.currency_to,
                                  'amount': args.amount}).json()

    print(result)

    if __name__=='__main__':
        parser = argparse.ArgumentParser(discription='Exchange rates')
        parser.add_argument('currency_from', default='USD', nargs='?')
        parser.add_argument('currency_to', default='UAH', nargs='?')
        parser.add_argument('amount', default=100, type=int, help='Amount of currency for exchange', nargs='?')
        parser.add_argument('-sd', '--start_date')
        parser.add_argument('-sf', '--save_to_file', type=bool)
        parser.add_argument('--slist', action='append')

        args = parser.parse_args()
        print(args.currency_from)
        print(args.currency_to)
        print(args.amount)
        if hasattr(args, 'save_to_file'):
            if args.save_to_file:
                print('Saving.....')
                 print(args.slist)
        get_data()