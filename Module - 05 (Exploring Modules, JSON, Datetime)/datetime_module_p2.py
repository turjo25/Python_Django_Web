from datetime import datetime,timedelta

#date addition and substraction
today = datetime.today().date()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(today)
print(tomorrow)
print(yesterday)

#time er addition and substraction
now = datetime.today()
new_time = now + timedelta(hours=5,minutes=30)
print(now)
print(new_time)

#date can be directly substracted
date1 = datetime(2000,9,25)
date2 = datetime(2025,5,26)
subs = (date2 - date1)
print(subs)

#making days into years,months and days
from dateutil.relativedelta import relativedelta

date1 = datetime(2000, 9, 25)
date2 = datetime(2025, 5, 26)

# Calculate the difference using relativedelta
diff = relativedelta(date2, date1)

print(f"The difference is: {diff.years} years, {diff.months} months, and {diff.days} days.")