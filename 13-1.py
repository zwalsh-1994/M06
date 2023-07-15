# Zachary Walsh
# 13-1.py - Writes current date to a text file
# Last edited July 15, 2023

import datetime
today = datetime.date.today()
file_ptr = open('today.txt', 'w')
file_ptr.write(str(today))
file_ptr.close()