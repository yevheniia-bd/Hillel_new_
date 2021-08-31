from uuid import uuid4

class BancAccount:

    account_name = 0
    uuid = None
    balance = 0
    transactions = 0

    def __init__(self):
        self.uuid = uuid4()
        self.print_uuid()
    #
    # def deposit(self):
    # #
    # # def withdrawal(self):
    # #
    # # def get_balance(self):
    bancaccount_class = BancAccount(1)
    print(bancaccount.balance)
