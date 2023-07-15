# Zachary Walsh
# 15-1.py - Utilizes multiprocessing to run multiple processes concurrently
# Last edited July 15, 2023

import multiprocessing
from datetime import datetime
import time
import random

def print_time():
    now = datetime.now()
    print("Today's date and time is ",format(now))
    time.sleep(random.random())
    
if __name__ == '__main__':
    proc1 = multiprocessing.Process(target=print_time())
    proc2 = multiprocessing.Process(target=print_time())
    proc3 = multiprocessing.Process(target=print_time())
    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()
    
    print('Job is done.')