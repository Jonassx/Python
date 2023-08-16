from datetime import datetime
now = datetime.now()

print (('%02d/%02d/%04d') % (now.month, now.day, now.year), ('%02d:%02d:%02d') % (now.hour, now.minute, now.second))

OU

from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
