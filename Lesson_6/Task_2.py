import time
import datetime

def time_counter(func):
    def wrapper(*args, **kwargs)
        count = 3
        while count > 0
            time.sleep(1)
            print(count)
            count -= 1
        return wrapper()

@time_counter
def what_time_is_it_now():
    task_counter = datetime.datetime.now()
    current_time = task_counter.strftime('%H:%M')
    print(current_time)
    return current_time

what_time_is_it_now()
