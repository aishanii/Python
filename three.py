#to print the number of days between two given dates

import datetime
from datetime import date


f_date = input("Enter first date in YYYY-MM-DD format: ")
year, month, day = map(int, f_date.split('-'))
f_date = datetime.date(year, month, day)

s_date = input("Enter second date in YYYY-MM-DD format: ")
year, month, day = map(int, s_date.split('-'))
s_date = datetime.date(year, month, day)

diff=s_date-f_date
print(diff.days)
