import datetime
now = datetime.datetime.now()
# print(now)

#will show just today's date
# today_date = datetime.date.today()
# print(today_date)

#we can get just time like this:
# today_date = datetime.datetime.now().time()
# print(today_date)

#we can print custom date
# custom_date = datetime.datetime(2025,5,26,7,29,0)
# print(custom_date)

#formatted date time:
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
formatted_date = now.strftime("%d/%B/%y %I:%M:%S")
formatted_date = now.strftime("%d/%b/%y %I:%M:%S: %p")
formatted_date = now.strftime("%d/%b/%y -%A- %I:%M:%S -%p")
print(formatted_date)

#date string to real date conversion
date = "25-09-2030 12:00:00"
perse_date = datetime.datetime.strptime(date,"%d-%m-%Y %H:%M:%S")
print(perse_date)
