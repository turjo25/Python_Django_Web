import pytz,datetime
import time
from datetime import datetime,UTC

dhaka = pytz.timezone('Asia/Dhaka')
utc = datetime.now(UTC)

print(utc.astimezone(dhaka))
print(utc)

#shows all the existing time zone
print(pytz.all_timezones)

#Using sleep
start = datetime.now()
time.sleep(5) #code execution will end after 5 seconds
end = datetime.now()
print(end - start)

