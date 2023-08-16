# from datetime import datetime
# print (datetime.now())

# Observe como a saída é 2013-11-25 23:45:14.317454. E se você não quiser a data e a hora inteiras?

from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print (current_day, current_month,  current_year)

