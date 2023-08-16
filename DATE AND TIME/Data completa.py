from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d') % (now.month, now.day, now.year)
# Essa é a maneira em que a data será exibida: mm-dd-yyyy