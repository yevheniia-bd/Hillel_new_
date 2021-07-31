import time

def what_time_is_it_now():
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    time.sleep(3)
    print(time.sleep())
    print(current_time)
what_time_is_it_now()