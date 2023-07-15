# Zachary Walsh
# 13-2.py - Reads 'today.txt' from current directory
# Last edited July 15, 2023

file_ptr = open('today.txt', 'r')
today_date = file_ptr.read()
file_ptr.close()