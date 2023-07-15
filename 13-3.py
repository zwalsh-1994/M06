# Zachary Walsh
# 13-3.py - Outputs date from 'today.txt'
# Last edited July 15, 2023

import datetime
file_ptr = open('today.txt', 'r')
today_date = file_ptr.read()
today = datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print('Today is ', today)